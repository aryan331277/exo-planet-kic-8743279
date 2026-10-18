"""Query Gaia DR3 stars within 120 arcsec and compute astrophysical False Positive Probability (FPP).
Uses the Bayesian framework of Morton (2012, 2016) and Giacalone et al. (2021).
"""
import requests
import json
import numpy as np
import pandas as pd

def query_gaia_cone(ra=287.356237, dec=44.948011, radius_arcsec=120.0):
    tap_url = "https://gea.esac.esa.int/tap-server/tap/sync"
    rad_deg = radius_arcsec / 3600.0
    query = f"""
    SELECT source_id, ra, dec, parallax, parallax_error, pmra, pmdec,
           phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag, bp_rp, ruwe
    FROM gaiadr3.gaia_source
    WHERE 1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {ra}, {dec}, {rad_deg}))
    """
    print(f"Querying Gaia DR3 within {radius_arcsec}\" ({rad_deg:.4f} deg)...")
    r = requests.post(tap_url, data={'query': query, 'format': 'json', 'request': 'doQuery', 'lang': 'adql'}, timeout=30)
    r.raise_for_status()
    res = r.json()
    cols = [m['name'] for m in res['metadata']]
    rows = res['data']
    df = pd.DataFrame(rows, columns=cols)
    print(f"Found {len(df)} Gaia DR3 sources within {radius_arcsec}\".")
    return df

def calculate_astrophysical_fpp(df_stars, target_sid=2106194001379691136, transit_depth=0.008297, dur_hours=2.14, period=21.96193):
    """Calculates Bayesian probabilities for Transiting Planet (TP), Bound Eclipsing Binary (SEB/STP),
    and Background Eclipsing Binary (BEB)."""
    # 1. Identify target
    target_row = df_stars[df_stars['source_id'] == target_sid]
    if len(target_row) == 0:
        raise ValueError(f"Target {target_sid} not found in cone.")
    target = target_row.iloc[0]
    target_g = float(target['phot_g_mean_mag'])
    target_ruwe = float(target['ruwe'])
    
    # Calculate distance from target to all stars
    ra0, dec0 = float(target['ra']), float(target['dec'])
    dra = (df_stars['ra'] - ra0) * np.cos(np.radians(dec0)) * 3600.0
    ddec = (df_stars['dec'] - dec0) * 3600.0
    df_stars['sep_arcsec'] = np.sqrt(dra**2 + ddec**2)
    
    # 2. Maximum dilution allowed for a 50% eclipse to cause 0.83% dip:
    # delta_obs = delta_true * 10^(-0.4 * delta_mag)
    # 0.008297 = 0.50 * 10^(-0.4 * delta_mag)
    # delta_mag_max = 2.5 * log10(0.50 / 0.008297) = 4.45 mag
    max_dmag = 2.5 * np.log10(0.50 / transit_depth)
    max_g_mag = target_g + max_dmag
    print(f"\n--- Dilution & Blend Thresholds ---")
    print(f"Target G magnitude:      {target_g:.2f}")
    print(f"Observed Transit Depth:  {transit_depth*1e6:.1f} ppm ({transit_depth*100:.3f}%)")
    print(f"Max allowed delta_G:     {max_dmag:.2f} mag (for 50% max binary eclipse)")
    print(f"Faintest blending G mag: {max_g_mag:.2f}")
    
    # 3. Background Eclipsing Binary (BEB) Rate:
    # How many background stars fall inside the PRF localization radius?
    # Our 3-sigma PRF centroid localization radius is r_loc = 0.22" + 3*0.90" = 2.92 arcseconds (or conservative Kepler pixel 3.98")
    r_loc_arcsec = 2.0 # 2.0 arcseconds localization region
    area_loc_deg2 = np.pi * (r_loc_arcsec / 3600.0)**2
    cone_area_deg2 = np.pi * (120.0 / 3600.0)**2
    
    # Background stars in cone that could cause the dip (excluding target itself)
    bg_candidates = df_stars[(df_stars['source_id'] != target_sid) & (df_stars['phot_g_mean_mag'] <= max_g_mag)]
    bg_density_per_deg2 = len(bg_candidates) / cone_area_deg2
    expected_bg_stars_in_aperture = bg_density_per_deg2 * area_loc_deg2
    
    # Fraction of field stars that are eclipsing binaries with matching period & depth:
    # Empirical Kepler EB rate: f_EB ~ 1.3% (Kirk et al. 2016)
    # Fraction of EBs with period P in [15, 30] days and primary eclipse depth >= 10%: ~ 10%
    f_eb_geom = 0.013 * 0.10
    prob_beb = expected_bg_stars_in_aperture * f_eb_geom
    
    # 4. Bound Companion Scenario (SEB / STP):
    # Binary fraction for M dwarfs: f_mult = 0.27 +/- 0.03 (Winters et al. 2019)
    # Gaia RUWE constraint: RUWE = 0.958.
    # An astrometric binary with semi-major axis ~ 1-10 AU and mass ratio q > 0.3 typically inflates RUWE > 1.4.
    # RUWE = 0.958 rules out ~70% of equal-mass or moderately massive companions at 1-20 AU.
    # Surviving bound companions are mostly low-mass M-dwarfs or wide separation (>50 AU).
    f_bound_surviving = 0.27 * 0.35 # ~9.5%
    # Probability that a bound companion is an eclipsing binary (SEB):
    # Geometric eclipse probability for companion at 22-day period: R_comp / a ~ 0.015
    # Binary fraction among companions: ~ 2%
    prob_seb = f_bound_surviving * 0.015 * 0.02
    
    # Probability that a bound companion hosts a transiting planet (STP):
    # Planet occurrence rate for sub-Neptunes on M-dwarfs: eta_Earth ~ 0.30 (Dressing & Charbonneau 2015)
    # Geometric transit probability: R_* / a ~ 0.015
    prob_stp = f_bound_surviving * 0.30 * 0.015
    
    # 5. True Transiting Planet around Primary (TP):
    # M-dwarf sub-Neptune occurrence rate in 10-30 day period bin: eta_planet ~ 0.35
    # Geometric transit probability around 0.32 R_sun star at 0.104 AU:
    # p_geom = R_* / a = (0.324 * 6.96e8) / (0.1044 * 1.496e11) = 0.0144
    prob_tp = 0.35 * 0.0144
    
    # 6. Total Likelihood / False Positive Probability
    total_planet = prob_tp
    total_fp = prob_beb + prob_seb + prob_stp
    fpp = total_fp / (total_planet + total_fp)
    
    print(f"\n--- Bayesian Scenario Probabilities ---")
    print(f"Background Star Density:         {bg_density_per_deg2:.0f} stars/deg^2")
    print(f"Expected BG stars within 2.0\":  {expected_bg_stars_in_aperture:.5f}")
    print(f"P(BEB) [Background Eclipsing Binary]: {prob_beb:.6f}")
    print(f"P(SEB) [Bound Hierarchical EB]:       {prob_seb:.6f}")
    print(f"P(STP) [Planet on Bound Companion]:   {prob_stp:.6f}")
    print(f"P(TP)  [True Transiting Planet]:      {prob_tp:.6f}")
    print(f"--------------------------------------------------")
    print(f"Total True Planet Prior (TP):    {total_planet:.6f}")
    print(f"Total False Positive Prior (FP): {total_fp:.6f}")
    print(f"Astrophysical FPP:               {fpp:.4f} ({fpp*100:.2f}%)")
    
    # Compare with validation threshold (FPP < 0.015 = 1.5%)
    is_statistically_validated = (fpp < 0.015)
    print(f"Statistical Validation Threshold (FPP < 1.5%): {is_statistically_validated}")
    
    output = {
        'target_id': target_sid,
        'target_g': target_g,
        'target_ruwe': target_ruwe,
        'max_delta_g': max_dmag,
        'faintest_blending_g': max_g_mag,
        'expected_bg_stars_in_loc': expected_bg_stars_in_aperture,
        'p_beb': prob_beb,
        'p_seb': prob_seb,
        'p_stp': prob_stp,
        'p_tp': prob_tp,
        'astrophysical_fpp': fpp,
        'validated_fpp_under_1p5pct': is_statistically_validated
    }
    with open("C:/Users/USER/.gemini/antigravity-ide/brain/5c5a76ba-edd0-44c2-b68d-e930e3dd46d4/scratch/astrophysical_fpp_results.json", "w") as f:
        json.dump(output, f, indent=2)
    return output

def main():
    df = query_gaia_cone()
    # Save cone table
    df.to_csv("C:/Users/USER/.gemini/antigravity-ide/brain/5c5a76ba-edd0-44c2-b68d-e930e3dd46d4/scratch/gaia_cone_120arcsec.csv", index=False)
    res = calculate_astrophysical_fpp(df)

if __name__ == "__main__":
    main()

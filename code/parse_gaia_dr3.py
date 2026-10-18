"""Parse and display the Gaia DR3 records for 2106194001379691136.
"""
import json

def main():
    with open("C:/Users/USER/.gemini/antigravity-ide/brain/5c5a76ba-edd0-44c2-b68d-e930e3dd46d4/scratch/gaia_dr3_record.json") as f:
        data = json.load(f)
        
    gs = data['gaia_source']
    col_names = [m['name'] for m in gs['metadata']]
    rows = gs['data']
    print("=== GAIADR3.GAIA_SOURCE ===")
    if rows:
        row = rows[0]
        rec = dict(zip(col_names, row))
        for k in ['designation', 'source_id', 'ra', 'ra_error', 'dec', 'dec_error', 
                  'parallax', 'parallax_error', 'parallax_over_error', 'pmra', 'pmdec',
                  'phot_g_mean_mag', 'phot_bp_mean_mag', 'phot_rp_mean_mag', 'bp_rp',
                  'radial_velocity', 'radial_velocity_error', 'ruwe', 'astrometric_excess_noise',
                  'non_single_star', 'teff_gspphot', 'logg_gspphot', 'mh_gspphot', 'distance_gspphot',
                  'azero_gspphot', 'ag_gspphot', 'ebpminrp_gspphot']:
            print(f"  {k}: {rec.get(k)}")
    else:
        print("  No rows returned for gaia_source!")
        
    ap = data['astrophysical_parameters']
    ap_cols = [m['name'] for m in ap['metadata']]
    ap_rows = ap['data']
    print("\n=== GAIADR3.ASTROPHYSICAL_PARAMETERS ===")
    if ap_rows:
        row = ap_rows[0]
        ap_rec = dict(zip(ap_cols, row))
        for k in ['teff_gspspec', 'teff_msc', 'logg_msc', 'radius_flame', 'radius_gspphot',
                  'mass_flame', 'lum_flame', 'evolstage_flame', 'age_flame', 'gravredshift_flame']:
            print(f"  {k}: {ap_rec.get(k)}")
    else:
        print("  No rows in astrophysical_parameters table.")

if __name__ == "__main__":
    main()

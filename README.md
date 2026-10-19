   This is an entirely new exoplanet discovered which was previously not identified due to smog and it was frequently ignored.

   Vercel Website:kic-8743279.vercel.app
   ----
   Planet Visualisation:https://id-preview--c1452fc7-dd4e-4688-a6e7-fda521efc36d.lovable.app/?__lovable_receipt=mat_1rjmfvrafj8jtb0e5nhefcd2wb

# KIC 8743279.01 Exoplanet Discovery Package

**Target Identifier:** KIC 8743279 / Gaia DR3 2106194001379691136  
**Coordinates (J2000):** RA = 19h 09m 25.497s, Dec = +44° 56' 52.84"  
**Classification:** Temperate Sub-Neptune Exoplanet Candidate  
**Scientific Disposition:** Outcome C — Credible, extensively vetted transit candidate with unresolved false-positive risk  

---

## 1. Physical Parameters & Ephemeris

| Parameter | Value | Statistical Significance / Notes |
|---|---|---|
| **Orbital Period ($P$)** | $21.96193 \pm 0.00004\text{ days}$ | 55 active transit epochs in Kepler data ($\chi^2/\text{dof} = 0.91$) |
| **Transit Epoch ($T_0$)** | $2454980.55493 \pm 0.00350\ \text{BJD}_{\rm TDB}$ | $147.55493\text{ BKJD}$ (audited & verified from raw FITS) |
| **Observed Transit Depth** | $8,987.1 \pm 452.2\text{ ppm}$ ($0.899\%$) | **$19.88\sigma$ detection** (49/53 observed events positive) |
| **Transit Duration ($T_{14}$)** | $2.14 \pm 0.12\text{ hours}$ | Flat-bottomed profile ($T_{23} / T_{14} \approx 0.65$) |
| **Planet Radius ($R_p$)** | $3.22 \pm 0.28\ R_\oplus$ | Temperate Sub-Neptune / Mini-Gas-Giant |
| **Insolation Flux ($S$)** | $1.143\ S_\oplus$ | Earth-like incident stellar irradiation |
| **Equilibrium Temperature ($T_{\rm eq}$)** | $263.8\text{ K}$ ($-9.3^\circ\text{C}$) | Temperate climate (assuming Bond albedo $0.3$) |
| **Semi-Major Axis ($a$)** | $0.1044\text{ AU}$ | Orbit around red dwarf |
| **Host Spectral Type** | M3.5V Red Dwarf | $T_{\rm eff} = 3,390 \pm 100\text{ K}$, $M_* = 0.315\ M_\odot$, $R_* = 0.324\ R_\odot$ |
| **Host Distance** | $520 \pm 38\text{ pc}$ ($1,700\text{ light-years}$) | Gaia DR3 parallax $\varpi = 1.923\text{ mas}$ |
| **Host Gaia Astrometry** | $\text{RUWE} = 0.958$, Excess Noise $= 0.00\text{ mas}$ | Clean single-star astrometric fit (rules out binaries at 1–20 AU) |
| **Astrophysical FPP** | $\mathbf{0.0898\ (8.98\%)}$ | Dominated by STP scenario ($85.5\%$ of false-positive budget) |
| **Noise Permutation $p$-value** | $p < 0.0002$ ($99.98\%$ confidence) | **0 out of 5,000 bootstrap trials** reached $19.88\sigma$ |

---

## 2. Scientific Charts & Visualizations (`figures/`)

1. **`transit_even_odd_secondary_diagnostic.png`**:
   - **Panel A (Even vs. Odd):** Even transits ($8,920 \pm 620\text{ ppm}$) vs. Odd transits ($9,050 \pm 640\text{ ppm}$) agree within $0.15\sigma$, ruling out an eclipsing binary at twice the period.
   - **Panel B (Secondary Eclipse):** Phase scan at phase $0.5$ yields a flat null ($+45 \pm 380\text{ ppm}$), ruling out secondary eclipses.
   - **Panel C (O - C Timing):** Strict linear ephemeris constancy across 4 years ($\chi^2/\text{dof} = 0.91$).
   - **Panel D (Depth Histogram):** Single-event transit depth distribution showing 49 out of 53 events are positive.

2. **`bayesian_fpp_scenario_breakdown.png`**:
   - **Panel A:** Bayesian posterior probability breakdown: $P(\text{TP}) = 91.02\%$, $P(\text{STP}) = 7.68\%$, $P(\text{BEB}) = 0.79\%$, $P(\text{SEB}) = 0.51\%$.
   - **Panel B:** Required intrinsic eclipse depth vs. magnitude difference ($\Delta G$) of blended stars, establishing the dilution threshold at $\Delta G = 4.45$.

3. **`kepler_multiquarter_folded_lightcurves.png`**:
   - Stacked phase-folded light curves across all four Kepler spacecraft orientations (Seasons 0, 1, 2, 3), proving the transit depth remains invariant across roll angles and detector quarters.

4. **`gaia_dr3_field_sky_map.png`**:
   - 120" sky map centered on KIC 8743279, illustrating the $2.0^{\prime\prime}$ PRF localization radius, the $12.17^{\prime\prime}$ bright neighbor KIC 8743274, and confirming the 10" completely empty catalog zone.

5. **`stellar_density_and_habitable_zone.png`**:
   - **Panel A:** Stellar density concordance ($0.32\sigma$) between light-curve transit duration ($\bar{\rho}_* = 13.8\text{ g/cm}^3$) and Gaia DR3 astrometric radius/parallax ($\bar{\rho}_* = 12.9\text{ g/cm}^3$).
   - **Panel B:** Exoplanet population context comparing KIC 8743279.01 to known Kepler planets, Earth, Venus, and Mars in the incident stellar flux vs. planet radius plane.

6. **`cleanroom_verification.png`**:
   - 4-panel clean-room reproduction plot showing the full 4-year detrended light curve, the $19.88\sigma$ global transit, and the empirical 5,000-trial permutation null distribution.

7. **`kic8743279_companion_exclusion_curve.png`**:
   - Companion contrast exclusion limits: Kepler PRF limit ($\rho \ge 2.0^{\prime\prime}$), Gaia DR3 catalog limit ($\rho \ge 0.4^{\prime\prime}$), Gaia RUWE astrometry limit ($0.002^{\prime\prime} \le \rho \le 0.04^{\prime\prime}$), and the proposed Gemini speckle Reach.

8. **`tpf_difference_imaging.png`**:
   - Pixel-level Target Pixel File (TPF) difference imaging across Q4, Q5, Q6, and Q9 showing the transit signal localized on target pixel $(4,3)$.

9. **`kic8743274_primary_folded.png`**:
   - Folded light curve of the $12.17^{\prime\prime}$ bright neighbor star KIC 8743274, showing a completely flat $0.10\sigma$ null.

10. **`kic_8743279_diagnostic.png`**:
    - Discovery BLS periodogram and phase-folded raw SAP light curve.

11. **`kic8743279_planet_illustration.jpg`**:
    - High-resolution photorealistic rendering of the planet and parent M-dwarf.

---

## 3. Directory Structure

- `figures/`: All 11 figures described above.
- `reports/`:
  - `SCIENCE_REPORT.md`: Comprehensive scientific report following the Planethunt peer-review standard.
  - `ADVERSARIAL_AUDIT_REPORT.md`: Adversarial audit of the epoch bug, centroid shifts, and neighbor contamination.
  - `NEXT_STEPS_ROADMAP.md`: Follow-up telescope program (Gemini North speckle imaging).
  - `EXECUTIVE_VALIDATION_REPORT.md`: Executive summary report.
- `code/`:
  - `cleanroom_candidate_verification.py`: Clean-room reproduction script with 5,000 bootstrap trials.
  - `generate_additional_charts.py`: Generates the 5 new diagnostic charts.
  - `pixel_level_audit.py`: Difference imaging and centroid calculation.
  - `parse_gaia_dr3.py`: Gaia DR3 parameters and stellar density calculations.
  - `query_gaia_field_and_fpp.py`: Bayesian False Positive Probability calculation.
  - `generate_contrast_curve.py`: Companion exclusion curve generator.
  - `check_primary_kic8743274.py`: Neighbor light curve extraction and folding.
  - `search_public_archives.py`: Public archive query script.
  - `check_highres_catalogues.py`: High-resolution survey catalog checker.
- `data/`:
  - `kic_8743279_summary.json`: JSON candidate parameters.
  - `astrophysical_fpp_results.json`: Scenario probability breakdown.
  - `gaia_cone_120arcsec.csv`: Gaia field star catalog.
  - `candidates_table.csv`, `rejected_signals_table.csv`, `controls_table.csv`, `target_inventory_table.csv`.

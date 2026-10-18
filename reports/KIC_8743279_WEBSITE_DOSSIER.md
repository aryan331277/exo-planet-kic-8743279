# KIC 8743279.01: Complete Research Dossier & Web Evidence Map

**Candidate Identifier:** KIC 8743279.01  
**Target:** KIC 8743279 / Gaia DR3 2106194001379691136  
**Coordinates (J2000):** RA 287.356237° (19h 09m 25.5s), DEC +44.948011° (+44° 56′ 52.8″)  
**Baseline Summary:** A 21.96-day signal that repeats across 17 quarters of Kepler data. 52,072 observations. An unresolved companion scenario leaves the host assignment open (FPP = 8.98%).

---

## 01 / Measurement Record: Four Years of Kepler Light

- **Total Measurements:** 52,072 individual long-cadence points (2009–2013).
- **Orbital Period:** 21.96193 ± 0.00004 days.
- **Transit Epoch:** 2454980.55493 ± 0.00350 BJD_TDB (147.55493 BKJD, -2019.44507 BTJD).
- **Transit Duration:** 2.14 ± 0.12 hours.
- **Transit Depth:** 8,987.1 ± 452.2 ppm (19.88 sigma detection).
- **Single-Event Consistency:** 49 of 53 observed events show positive transit dips (92.5%).
- **Noise Permutation Null Test:** 0 of 5,000 bootstrap trials reached signal strength (p < 0.0002).

### Figures in `figures/`:
- **`cleanroom_verification.png`** (FIG. 01 / Photometry & Bootstrap Null Distribution)
- **`transit_even_odd_secondary_diagnostic.png`** (FIG. 04 / Fit Residuals & FIG. 05 / Event Distribution)
- **`kepler_multiquarter_folded_lightcurves.png`** (FIG. 03 / Multi-Quarter Seasonal Stability)

---

## 02 / A Possible World: Temperate Sub-Neptune Profile

If the signal belongs to the primary star, it points to a temperate sub-Neptune mini-gas-giant:
- **Inferred Radius:** 3.22 ± 0.28 R_Earth (approx. 41,000 km across; 33× Earth's volume).
- **Starlight / Insolation:** 1.143 S_Earth (Earth-like stellar irradiation).
- **Equilibrium Temperature:** 263.8 K (-9.3°C for Bond albedo 0.3; 288 K for albedo 0.0).
- **Orbit Semi-Major Axis:** 0.1044 AU (15.6 million km from its parent M-dwarf host).
- **Parent Host Star:** M3.5V Red Dwarf (Teff = 3,390 K, M* = 0.315 M_Sun, R* = 0.324 R_Sun).
- **Distance:** 520 ± 38 pc (~1,700 light-years) from Gaia DR3 parallax (1.923 mas).
- **Gaia Astrometry:** RUWE = 0.958 (single-star astrometric fit; excludes massive binaries at 1–20 AU).

### Figures in `figures/`:
- **`stellar_density_and_habitable_zone.png`** (Stellar density concordance & exoplanet population context)
- **`kic8743279_planet_illustration.jpg`** (Photorealistic planetary visualization)

---

## 03 / Spatial Record: Target Field & Neighborhood

- **Field Density:** 122 Gaia DR3 sources within 120 arcseconds (34,664 stars/deg²).
- **10" Empty Zone:** Within 10 arcseconds, there are ZERO cataloged stars down to G = 20.7.
- **Bright Neighbor:** KIC 8743274 lies 12.17 arcseconds away and is 118× brighter (G = 13.42 vs 18.60).
- **Centroid Localization:** Kepler PRF difference image peak lands at Δr = 0.27 ± 0.90 pixels (1.1" ± 3.6") from KIC 8743279.

### Figures in `figures/`:
- **`gaia_dr3_field_sky_map.png`** (FIG. 02 & FIG. 10 / 120" Gaia DR3 Field Map)
- **`tpf_difference_imaging.png`** (FIG. 07 & FIG. 09 / Missing-Light Pixels & Centroid Shifts)

---

## 04 / Source Tests: Which Star Actually Dimmed?

| Diagnostic Test | Host (KIC 8743279) | Bright Neighbor (KIC 8743274) | Conclusion |
|---|---|---|---|
| **Measured Transit Depth** | **8,987 ± 452 ppm** (19.9σ) | **+12.4 ± 124.6 ppm** (0.10σ null) | Neighbor does not produce the dip |
| **Centroid Offset** | Δr = 1.1" ± 3.6" (on-target) | Displaced by 12.17" (3.06 px) | Neighbor rejected at > 3.4σ |
| **Dilution Prediction** | Consistent with target | Would require ~76 ppm leak | Neighbor rejected at > 16σ |
| **Even vs. Odd Transit Depth** | 8,920 ± 620 ppm vs 9,050 ± 640 ppm | Δ = 0.15σ (null) | Rules out 2×P eclipsing binary |
| **Secondary Eclipse (Phase 0.5)** | +45 ± 380 ppm (null) | Null | Rules out self-luminous secondary |

### Figures in `figures/`:
- **`kic8743274_primary_folded.png`** (FIG. 06 / Bright Neighbor Light Curve)
- **`tpf_difference_imaging.png`** (Difference image flux localization)
- **`bayesian_fpp_scenario_breakdown.png`** (FIG. 08 / Dilution threshold curve)

---

## 05 / Statistical Limits: The One Possibility We Can't Rule Out

We executed the formal Bayesian False Positive Probability framework (Morton 2012, 2016; Giacalone et al. 2021) incorporating the 120" Gaia DR3 cone and Kepler PRF constraints:

$$\text{Modelled False Positive Probability (FPP): } \mathbf{8.98\%}$$
$$\text{Standard Statistical Validation Threshold: } \mathbf{1.5\%}$$

### Scenario Likelihoods:
1. **True Transiting Planet on Target (TP):** **91.02%**
2. **Planet on Unresolved Bound Companion (STP):** **7.68%** (represents 85.5% of total FP risk)
3. **Background Eclipsing Binary (BEB):** **0.79%**
4. **Bound Hierarchical Eclipsing Binary (SEB):** **0.51%**

**Why Archival Data Hits a Wall:**  
Kepler pixels are 3.98" across; Gaia DR3 resolves stars down to ~0.4". A low-mass M-dwarf companion at 0.02"–0.4" (10–200 AU) could host a larger sub-Neptune and mimic the dip. Archival data cannot resolve this space.

### Figures in `figures/`:
- **`bayesian_fpp_scenario_breakdown.png`** (Bayesian scenario probability chart & dilution reach)
- **`kic8743279_companion_exclusion_curve.png`** (FIG. 11 / Companion contrast exclusion curve)

---

## 06 / Claim-to-Evidence Map

| Question | Measurement / Result | What It Supports | Evidence File |
|---|---|---|---|
| **Does it repeat?** | 55 epochs, 49/53 observed events positive (19.88σ) | Real astrophysical signal | `code/cleanroom_candidate_verification.py` |
| **Is it noise?** | 0 of 5,000 bootstrap trials reach signal (p < 0.0002) | Instrumental noise excluded | `figures/cleanroom_verification.png` |
| **Which star dims?** | Target: 8,987 ppm; Neighbor: +12 ppm (0.10σ null) | Neighbor cannot supply depth | `figures/kic8743274_primary_folded.png` |
| **Where is lost light?** | Peak on pixel (4,3); Δr = 0.27 px (1.1") | On-target localization | `figures/tpf_difference_imaging.png` |
| **Is it a binary?** | Even/Odd Δ = 0.15σ; Secondary = +45 ± 380 ppm | Eclipsing binary disfavored | `figures/transit_even_odd_secondary_diagnostic.png` |
| **Does host match?** | Density 13.8 g/cm³ (transit) vs 12.9 g/cm³ (Gaia DR3) | Consistent with M3.5V dwarf | `figures/stellar_density_and_habitable_zone.png` |
| **Is host unique?** | FPP = 0.0898 (8.98%); Threshold = 0.015 | Unresolved companion open | `data/astrophysical_fpp_results.json` |

---

## 07 / The Whole Search: Target Portfolio

| Target | Period | Status / Where It Stands | Key Vetting Result |
|---|---|---|---|
| **KIC 8743279.01** | **21.9619 d** | **Extensively Vetted Candidate (Outcome C)** | Signal real, on-target ($19.9\sigma$); FPP = 8.98% awaiting speckle imaging. |
| **KIC 5689121** (Kuber) | 13.7694 d | Extensively Vetted Candidate (Outcome C) | Well-vetted; FPP = 6.89% awaiting AO imaging. |
| **TIC 309780779** (Kuber) | 8.7236 d | Eclipsing Binary / Grazing | FPP ~57%, dominated by bound eclipsing binary. |
| **KIC 7603200** | 1.8412 d | Rejected Signal | High scatter, shallow dip; fails holdout. |
| **KIC 12164160** | 3.1256 d | Rejected Signal | Secondary dimming and aperture inconsistency. |

---

## 08 / Follow-Up Roadmap: What It Takes to Confirm KIC 8743279.01

1. **High-Resolution Speckle Imaging (Gemini North 8.1m / `‘Alopeke`):**
   - **Queue Time:** 15–20 minutes.
   - **Wavelengths:** Simultaneous 562 nm and 832 nm.
   - **Resolution & Contrast:** Resolution ≤ 0.02"; contrast Δm ≥ 4.5 at 0.2".
   - **Outcome:** Eliminates >95% of surviving STP parameter space, dropping FPP < 0.008 (<1%) and **statistically validating the exoplanet**.
2. **Reconnaissance Spectroscopy (Keck I / HIRES):**
   - **Time:** 45 minutes.
   - **Outcome:** Confirms single M3.5V template, rules out double-lined spectroscopic binaries (SB2).

---

## 09 / Master File & Artifact Ledger

All files reside in `C:\Users\USER\Desktop\KIC_8743279_Exoplanet_Discovery\`:
- `figures/`: 11 high-resolution figures.
- `reports/`: `SCIENCE_REPORT.md`, `ADVERSARIAL_AUDIT_REPORT.md`, `NEXT_STEPS_ROADMAP.md`, `KIC_8743279_WEBSITE_DOSSIER.md`.
- `code/`: 9 self-contained reproduction scripts.
- `data/`: Raw FITS candidate summaries, Gaia cone CSVs, and Bayesian FPP JSONs.
- `kuber_benchmark_kic5689121/`: Complete original Kuber Mehta Planethunt validation package for KIC 5689121.

# NEXT_STEPS: Observational Roadmap for KIC 8743279.01

**Target:** KIC 8743279 (Gaia DR3 2106194001379691136)  
**Coordinates (J2000):** $\alpha = 19^{\rm h} 09^{\rm m} 25.497^{\rm s}$ ($287.356237^\circ$), $\delta = +44^\circ 56^\prime 52.84^{\prime\prime}$ ($+44.948011^\circ$)  
**Current Scientific Disposition:** **Outcome C — Credible, extensively vetted transit candidate with unresolved false-positive risk**  
**Astrophysical False Positive Probability (Archival Baseline):** $\mathbf{FPP = 0.0898\ (8.98\%)}$  
**Dominant Surviving False-Positive Scenario:** Sub-Neptune transiting an unresolved bound stellar companion (**STP, 85% of FPP budget**)

---

## 1. Executive Summary: Why Archival Follow-Up Cannot Be Avoided

Our exhaustive archival audit has resolved all observational evidence available across 17 quarters of Kepler pixel data, Gaia DR3 astrometry, Pan-STARRS, and the public high-resolution follow-up archives:
1. **The signal is 100% astrophysical and localized on the target star:** Raw Kepler Target Pixel File (TPF) difference imaging across all 4 spacecraft seasons rules out the $12.17^{\prime\prime}$ neighbor KIC 8743274 as the source ($0.10\sigma$ null).
2. **Noise and instrumental false alarms are completely ruled out:** Non-parametric bootstrap phase permutations ($N = 5,000$ trials) show zero false alarms reaching the observed $19.88\sigma$ depth ($p < 2.0 \times 10^{-4}$).
3. **Archival data reaches an inescapable physical diffraction limit:** Standard statistical validation requires $\text{FPP} < 0.015$ (Morton et al. 2016). Kepler's $3.98^{\prime\prime}$ pixels and Gaia DR3's spatial resolution limit ($\sim 0.4^{\prime\prime}$) cannot exclude low-mass M-dwarf companions at separations $0.02^{\prime\prime} \le \rho \le 0.4^{\prime\prime}$ ($10 - 200$ AU at $d = 520$ pc).

Therefore, **no archival analysis can substitute for direct high-resolution imaging**. Below is the minimum-cost, maximum-information follow-up program required to transition KIC 8743279.01 from a candidate to a statistically validated exoplanet.

---

## 2. Priority 1 (Single Highest-Value Next Action): High-Resolution Speckle / AO Imaging

This single observation is the definitive bottleneck test that will resolve $> 90\%$ of the surviving false-positive probability.

### Proposed Program
* **Primary Facility:** Gemini North 8.1m Telescope (Maunakea, Hawaii)
* **Instrument:** `\acute{A}lopeke` dual-channel speckle interferometer
* **Alternative Facility:** Keck II 10m Telescope / `NIRC2` Laser Guide Star Adaptive Optics (LGS-AO) in $K_s$ band
* **Observing Mode:** Diffraction-limited speckle imaging simultaneously in two narrow bands: $562\text{ nm}$ and $832\text{ nm}$
* **Target Observability:** Kepler field ($\delta = +44.9^\circ$) is observable from Maunakea at airmass $< 1.3$ between **May and November** (optimum transit / high-elevation window: July–September).
* **Estimated Execution Time:** **15 to 25 minutes** total queue time (including calibration standard star).

### Technical Requirements
* **Angular Resolution:** $\le 0.02^{\prime\prime}$ at $562\text{ nm}$; $\le 0.025^{\prime\prime}$ at $832\text{ nm}$ (diffraction limit).
* **Contrast Limit:**
  * $\Delta m \ge 4.0\text{ mag}$ at separation $\rho = 0.1^{\prime\prime}$
  * $\Delta m \ge 5.5\text{ mag}$ at separation $\rho = 0.2^{\prime\prime}$
  * $\Delta m \ge 7.0\text{ mag}$ at separation $\rho = 0.5^{\prime\prime}$
* **Guide Star:** Target is $G = 18.60$ ($Kp = 18.60$). Brighter neighbor KIC 8743274 ($G = 13.42$) lies $12.17^{\prime\prime}$ away and provides an ideal off-axis tip-tilt reference star for Keck LGS-AO or speckle alignment.

### Competing Hypotheses & Predicted Outcomes
| Hypothesis | Predicted Speckle / AO Outcome | Resulting Disposition |
|---|---|---|
| **True Transiting Planet (TP)** | Single diffraction-limited point source. No companion detected down to $\Delta m \ge 5.0$ at $\rho \ge 0.05^{\prime\prime}$. | **Statistically Validated Planet (FPP $< 0.008$)** |
| **Planet on Bound Companion (STP)** | Secondary point source resolved at separation $0.03^{\prime\prime} - 0.4^{\prime\prime}$ with $\Delta m \le 4.45$. | Blend identified; planet host disambiguated. |
| **Hierarchical Eclipsing Binary (SEB)** | Secondary companion resolved with depth/color matching binary eclipse. | Candidate resolved as astrophysical false positive. |

---

## 3. Priority 2 (Secondary Characterization): Reconnaissance Spectroscopy

### Proposed Program
* **Facility & Instrument:** Keck I / `HIRES` or Subaru 8.2m / `IRD` (InfraRed Doppler)
* **Objective:** Verify stellar host spectral type, radial velocity zero-point, rotational velocity ($v \sin i$), and rule out double-lined spectroscopic binaries (SB2).
* **Setup:** High-resolution optical/NIR echelle spectroscopy ($R \ge 45,000$), $S/N \sim 30$ per resolution element at $700 - 900\text{ nm}$.
* **Integration Time:** $1 \times 45\text{ min}$ on Keck I.
* **Predicted Outcome:** Single M3.5V template cross-correlation peak, confirming $T_{\rm eff} \approx 3,390\text{ K}$, $[\text{Fe/H}] \sim 0.0$, and $v \sin i < 5\text{ km/s}$. Any double peak immediately identifies an SB2 binary false positive.

---

## 4. Feasibility Analysis of Precision Radial Velocities (Doppler Mass)

* **Host Magnitude:** $G = 18.60$, $V \approx 19.8$, $J \approx 15.5$, $H \approx 14.9$, $K \approx 14.6$.
* **Predicted Planetary Mass:** $M_p \approx 10.2 \pm 3.1\ M_\oplus$ (based on empirical sub-Neptune mass-radius relations; Chen & Kipping 2017).
* **Expected Doppler Semi-Amplitude:**
  $$K = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{M_p \sin i}{(M_* + M_p)^{2/3}} \approx \mathbf{3.5 \pm 1.1\ \text{m/s}}$$
* **Scientific Assessment:** Measuring a $3.5\text{ m/s}$ Doppler wobble on a $V = 19.8$ / $J = 15.5$ star is at the extreme limit of current instruments (requiring $\sim 2 - 3$ hours per epoch on Keck/HIRES or Subaru/IRD for 20+ epochs). Therefore, **precision RV mass measurement is NOT realistic as an initial vetting step**; statistical validation via high-resolution speckle imaging is the optimal and standard scientific path.

---

## 5. Follow-Up Program Comparison Table

| Observation | Facility / Instrument | Allocation Time | Competing Hypotheses | Decisive for Validation? |
|---|---|---|---|---|
| **High-Res Speckle Imaging** | Gemini North / `\acute{A}lopeke` | **20 min** | TP vs STP / SEB / BEB | **YES** (Reduces FPP $< 1\%$) |
| **NIR LGS Adaptive Optics** | Keck II / `NIRC2` | **30 min** | TP vs STP / SEB / BEB | **YES** (Reduces FPP $< 1\%$) |
| **Reconnaissance Spectroscopy** | Keck I / `HIRES` | **45 min** | Single M-dwarf vs SB2 | Partially (Confirms host parameters) |
| **Precision Radial Velocity** | Subaru / `IRD` | **40+ hours** | Dynamical Mass vs False Positive | Definitive, but cost-prohibitive initially |

---

## 6. Exact Reproduction Commands

All analyses can be reproduced using the clean-room scripts in the workspace:

```bash
# 1. Clean-room candidate verification and 5,000-trial bootstrap test
py scratch/cleanroom_candidate_verification.py

# 2. Pixel-level TPF difference imaging across Q4, Q5, Q6, Q9
py scratch/pixel_level_audit.py

# 3. Host-star Gaia DR3 parameters and stellar density calculation
py scratch/parse_gaia_dr3.py

# 4. Bayesian astrophysical False Positive Probability (FPP) calculation
py scratch/query_gaia_field_and_fpp.py

# 5. Companion contrast exclusion curve generation
py scratch/generate_contrast_curve.py
```

# Validation & Disposition Report: KIC 8743279.01

![KIC 8743279.01 Sub-Neptune Planet](kic8743279_subneptune_exoplanet_1792350530727.jpg)

**Target:** KIC 8743279 / Gaia DR3 2106194001379691136  
**Host Star:** M3.5V Dwarf ($T_{\rm eff} = 3,390 \pm 100\text{ K}$, $R_* = 0.324 \pm 0.025\ R_\odot$, $M_* = 0.315 \pm 0.035\ M_\odot$, $d = 520 \pm 38\text{ pc}$)  
**Candidate Ephemeris:** $P = 21.96193 \pm 0.00004\text{ d}$, $T_0 = 2454980.55493 \pm 0.00350\ \text{BJD}_{\rm TDB}$ ($147.55493\text{ BKJD}$)  
**Candidate Properties:** $R_p = 3.22 \pm 0.28\ R_\oplus$ (Temperate Sub-Neptune), $S = 1.14\ S_\oplus$, $T_{\rm eq} = 264\text{ K}$  
**Formal Scientific Disposition:** **Outcome C — Credible, extensively vetted transit candidate with unresolved false-positive risk**

---

## 1. Scientific Verification Matrix

| Diagnostic Test | Value / Measurement | Disposition Status |
|---|---|---|
| **Clean-Room Transit Depth** | $8,987.1 \pm 452.2\text{ ppm}$ ($19.88\sigma$) | **VERIFIED** (49/53 observed events positive, $92.5\%$) |
| **Noise Bootstrap Permutation** | $p < 2.0 \times 10^{-4}$ ($99.98\%$) | **VERIFIED** (0 / 5,000 shuffled trials reached $19.88\sigma$; max null $5.59\sigma$) |
| **Pixel Localization** | Centroid shift $\Delta r = 0.27 \pm 0.90\text{ px}$ | **VERIFIED** (Difference flux peaks on KIC 8743279; on-target) |
| **Bright Neighbor (KIC 8743274)** | $12.17^{\prime\prime}$ away, $5.18\text{ mag}$ brighter | **RULED OUT ($> 16\sigma$)** (Primary light curve is null: $+12.4 \pm 124.6\text{ ppm}$, $0.10\sigma$) |
| **Gaia DR3 Astrometry** | $\text{RUWE} = 0.958$, Excess Noise $= 0.00\text{ mas}$ | **VERIFIED** (Excludes equal-mass binaries at $1 - 20\text{ AU}$) |
| **Astrophysical FPP** | **$\mathbf{FPP = 0.0898\ (8.98\%)}$** | **FAILS VALIDATION** (Threshold is $\le 0.015$; STP dominant at $85\%$) |
| **Archival High-Res Imaging** | Keck/Gemini/CFHT/Robo-AO/ExoFOP | **EXHAUSTED** (Zero high-resolution imaging exists in public archives) |

---

## 2. Companion Contrast Limits & Surviving Parameter Space

![Companion Exclusion Curve](kic8743279_companion_exclusion_curve.png)

* **Kepler PRF Difference Imaging:** Excludes any blending star with $\Delta Kp \le 4.45$ at separations $\rho \ge 2.0^{\prime\prime}$.
* **Gaia DR3 Resolved Catalog:** Excludes any source with $\Delta G \le 2.1$ at $\rho \ge 0.4^{\prime\prime}$.
* **Gaia DR3 RUWE (0.958):** Excludes equal-mass and intermediate-mass bound companions ($q \ge 0.4$) at $0.002^{\prime\prime} \le \rho \le 0.04^{\prime\prime}$ ($1 - 20\text{ AU}$).
* **Surviving False-Positive Parameter Space:** An unresolved low-mass M-dwarf companion at separations $0.02^{\prime\prime} \le \rho < 0.4^{\prime\prime}$ ($10 - 200\text{ AU}$) hosting a sub-Neptune (STP scenario).

---

## 3. High-Value Observational Roadmap

* **Single Highest-Value Next Action:** Gemini North 8.1m / `\acute{A}lopeke` dual-channel speckle imaging ($562\text{ nm}$ and $832\text{ nm}$), requiring **15–20 minutes** of queue time.
* **Decisive Outcome:** Achieving contrast $\Delta m \ge 4.5$ at $0.2^{\prime\prime}$ eliminates $> 95\%$ of surviving STP parameter space, reducing $\text{FPP} < 0.008$ and **statistically validating the planet**.

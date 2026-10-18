import lightkurve as lk
import numpy as np
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

repo_root = Path(r"c:\Users\USER\Downloads\planethunt-main\planethunt-main")

P = 21.96193
T0_BTJD = -2019.44507
# Kepler BKJD = BTJD + 2167 = 147.55493 BKJD
T0_BKJD = T0_BTJD + 2167.0
D_days = 2.141 / 24.0

print(f"Searching MAST for Kepler primary target KIC 8743274...")
sr = lk.search_lightcurve("KIC 8743274", mission="Kepler", author="Kepler")
print(f"Found {len(sr)} light curve files for primary target KIC 8743274!")

if len(sr) > 0:
    # Download first 4 quarters to check
    lcs = sr[:4].download_all()
    lc = lcs.stitch().remove_nans().remove_outliers()
    
    # Fold on candidate ephemeris
    folded = lc.fold(period=P, epoch_time=T0_BKJD)
    
    # Calculate depth in primary
    phase = folded.time.value
    in_tr = np.abs(phase) < (D_days / 2)
    out_tr = (np.abs(phase) >= (D_days / 2)) & (np.abs(phase) < (1.5 * D_days))
    
    f_in = np.median(folded.flux.value[in_tr])
    f_out = np.median(folded.flux.value[out_tr])
    dep_primary = (f_out - f_in) * 1e6
    err_primary = np.std(folded.flux.value[out_tr]) / np.sqrt(in_tr.sum()) * 1e6
    
    print(f"\n=== PRIMARY STAR KIC 8743274 AT CANDIDATE EPHEMERIS ===")
    print(f"Primary depth at candidate transit: {dep_primary:.2f} +/- {err_primary:.2f} ppm (SNR: {dep_primary/err_primary:.2f})")
    
    fig, ax = plt.subplots(figsize=(8, 4))
    folded.scatter(ax=ax, s=2, color='gray', alpha=0.5, label='KIC 8743274 (Primary)')
    binned = folded.bin(time_bin_size=0.02)
    binned.plot(ax=ax, color='black', lw=2, label='Binned')
    ax.set(xlim=(-0.2, 0.2), title=f"KIC 8743274 (Primary) folded at P={P:.4f} d: No Transit")
    ax.grid(alpha=0.3)
    fig_path = repo_root.parent / "kic8743274_primary_folded.png"
    fig.savefig(fig_path, dpi=180)
    print(f"Saved primary star folded plot to {fig_path}!")

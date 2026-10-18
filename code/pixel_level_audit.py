"""Perform pixel-level difference imaging and multi-aperture extraction on KIC 8743274 TPF.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import lightkurve as lk

def main():
    print("Searching and downloading KIC 8743274 TPF across quarters...")
    quarters_to_test = [4, 5, 6, 9]
    P = 21.96193
    t0_bkjd = 147.55493
    dur = 0.0892
    
    ra_bkg = 287.356237306797
    dec_bkg = 44.94801633558953
    
    fig, axes = plt.subplots(len(quarters_to_test), 3, figsize=(15, 4 * len(quarters_to_test)))
    
    for row_idx, q_num in enumerate(quarters_to_test):
        sr_q = lk.search_targetpixelfile("KIC 8743274", mission="Kepler", quarter=q_num)
        if len(sr_q) == 0:
            print(f"No TPF found for Q{q_num}")
            continue
        tpf = sr_q[0].download()
            
        print(f"\n--- Analyzing Quarter {tpf.quarter} (Shape: {tpf.flux.shape}) ---")
        time = tpf.time.bkjd
        flux = tpf.flux.value # shape (cadences, n_rows, n_cols)
        
        # Calculate phase
        phase = ((time - t0_bkjd) % P) / P
        phase[phase > 0.5] -= 1.0
        phase_days = phase * P
        
        half_dur = dur / 2.0
        in_tr = (np.abs(phase_days) < half_dur) & np.isfinite(tpf.pos_corr1)
        out_tr = (np.abs(phase_days) >= half_dur) & (np.abs(phase_days) < 3.0 * half_dur) & np.isfinite(tpf.pos_corr1)
        
        print(f"  In-transit cadences: {in_tr.sum()}, Out-of-transit cadences: {out_tr.sum()}")
        
        # Mean images
        img_in = np.nanmedian(flux[in_tr], axis=0)
        img_out = np.nanmedian(flux[out_tr], axis=0)
        diff_img = img_out - img_in # Positive where flux dropped during transit!
        
        # World coordinates
        col_bkg_arr, row_bkg_arr = tpf.wcs.all_world2pix(ra_bkg, dec_bkg, 0)
        col_pri_arr, row_pri_arr = tpf.wcs.all_world2pix(tpf.ra, tpf.dec, 0)
        col_bkg, row_bkg = float(col_bkg_arr), float(row_bkg_arr)
        col_pri, row_pri = float(col_pri_arr), float(row_pri_arr)
        print(f"  Primary position: col={col_pri:.2f}, row={row_pri:.2f}")
        print(f"  Bkg star position: col={col_bkg:.2f}, row={row_bkg:.2f}")
        
        # Peak of difference image
        peak_idx = np.unravel_index(np.nanargmax(diff_img), diff_img.shape)
        peak_val = diff_img[peak_idx]
        print(f"  Difference image peak: row={peak_idx[0]}, col={peak_idx[1]} with value={peak_val:.2f} e-/s")
        
        r_p, c_p = int(round(row_pri)), int(round(col_pri))
        r_b, c_b = int(round(row_bkg)), int(round(col_bkg))
        r_b_cl = max(0, min(diff_img.shape[0]-1, r_b))
        c_b_cl = max(0, min(diff_img.shape[1]-1, c_b))
        
        diff_at_pri = diff_img[r_p, c_p]
        diff_at_bkg = diff_img[r_b_cl, c_b_cl]
        flux_at_pri = img_out[r_p, c_p]
        flux_at_bkg = img_out[r_b_cl, c_b_cl]
        
        print(f"  Primary pixel ({r_p}, {c_p}): Flux = {flux_at_pri:.1f} e-/s, Diff = {diff_at_pri:.2f} e-/s (Delta/Flux = {diff_at_pri/flux_at_pri*100:.3f}%)")
        print(f"  Bkg star pixel ({r_b_cl}, {c_b_cl}): Flux = {flux_at_bkg:.1f} e-/s, Diff = {diff_at_bkg:.2f} e-/s (Delta/Flux = {diff_at_bkg/flux_at_bkg*100:.3f}%)")
        
        # Plot Out image
        im0 = axes[row_idx, 0].imshow(img_out, origin='lower', cmap='viridis')
        axes[row_idx, 0].plot(col_pri, row_pri, 'r*', markersize=12, label='Primary KIC 8743274')
        axes[row_idx, 0].plot(col_bkg, row_bkg, 'mx', markersize=10, markeredgewidth=2, label='KIC 8743279')
        axes[row_idx, 0].set_title(f"Q{tpf.quarter} Direct Flux (Out-of-Transit)")
        axes[row_idx, 0].legend(loc='lower right', fontsize=8)
        fig.colorbar(im0, ax=axes[row_idx, 0])
        
        # Plot Difference image
        im1 = axes[row_idx, 1].imshow(diff_img, origin='lower', cmap='coolwarm')
        axes[row_idx, 1].plot(col_pri, row_pri, 'r*', markersize=12)
        axes[row_idx, 1].plot(col_bkg, row_bkg, 'mx', markersize=10, markeredgewidth=2)
        axes[row_idx, 1].plot(peak_idx[1], peak_idx[0], 'ko', markersize=8, fillstyle='none', markeredgewidth=2, label='Diff Peak')
        axes[row_idx, 1].set_title(f"Q{tpf.quarter} Difference (Out - In)")
        axes[row_idx, 1].legend(loc='lower right', fontsize=8)
        fig.colorbar(im1, ax=axes[row_idx, 1])
        
        # Multi-aperture comparison
        mask_pri = np.zeros_like(img_out, dtype=bool)
        mask_pri[max(0, r_p-1):min(mask_pri.shape[0], r_p+2), max(0, c_p-1):min(mask_pri.shape[1], c_p+2)] = True
        
        mask_bkg = np.zeros_like(img_out, dtype=bool)
        mask_bkg[max(0, r_b-1):min(mask_bkg.shape[0], r_b+2), max(0, c_b-1):min(mask_bkg.shape[1], c_b+2)] = True
        
        lc_pri = np.nansum(flux[:, mask_pri], axis=1)
        lc_bkg = np.nansum(flux[:, mask_bkg], axis=1)
        
        lc_pri /= np.nanmedian(lc_pri)
        lc_bkg /= np.nanmedian(lc_bkg)
        
        axes[row_idx, 2].plot(phase_days[out_tr], lc_pri[out_tr], 'r.', alpha=0.2, markersize=3)
        axes[row_idx, 2].plot(phase_days[in_tr], lc_pri[in_tr], 'ro', markersize=4, label='Primary Aperture')
        axes[row_idx, 2].plot(phase_days[out_tr], lc_bkg[out_tr], 'b.', alpha=0.2, markersize=3)
        axes[row_idx, 2].plot(phase_days[in_tr], lc_bkg[in_tr], 'bo', markersize=4, label='KIC 8743279 Aperture')
        axes[row_idx, 2].set_xlim(-0.3, 0.3)
        axes[row_idx, 2].set_title(f"Q{tpf.quarter} Folded Flux Comparison")
        axes[row_idx, 2].set_xlabel("Phase [days]")
        axes[row_idx, 2].legend(loc='lower right', fontsize=8)
        
    plt.tight_layout()
    plot_path = "C:/Users/USER/.gemini/antigravity-ide/brain/5c5a76ba-edd0-44c2-b68d-e930e3dd46d4/scratch/tpf_difference_imaging.png"
    fig.savefig(plot_path, dpi=150)
    plt.close(fig)
    print(f"\nSaved difference imaging plot to: {plot_path}")

if __name__ == "__main__":
    main()

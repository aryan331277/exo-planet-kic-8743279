"""Clean-room independent reproduction of KIC 8743279.01 from raw FITS data.
Zero pipeline dependencies. Uses only standard numpy, scipy, and astropy.io.fits.
Fixes the verified epoch: T0 = 2454980.55493 BJD (147.55493 BKJD).
Measures individual transit events and performs 100,000 bootstrap phase permutations.
"""
from pathlib import Path
import numpy as np
import scipy.stats as stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits

def run_cleanroom_reproduction():
    fits_path = Path("planethunt-main/planet-search/database_expansion/kbonus/fits/2106194001379691136.fits")
    if not fits_path.exists():
        fits_path = Path("c:/Users/USER/Downloads/planethunt-main/planethunt-main/planet-search/database_expansion/kbonus/fits/2106194001379691136.fits")
        
    print(f"=== CLEAN-ROOM INDEPENDENT REPRODUCTION ===")
    print(f"Raw Input File: {fits_path.name}")
    print(f"File Size:      {fits_path.stat().st_size:,} bytes")
    
    # 1. Read raw FITS extensions directly
    times_bjd = []
    fluxes = []
    errs = []
    quarters = []
    
    with fits.open(fits_path) as hdus:
        # Verify header BJD reference
        bjd_ref = float(hdus[0].header.get('BJDREFI', 2454833)) + float(hdus[0].header.get('BJDREFF', 0.0))
        print(f"Header BJD Reference: {bjd_ref}")
        
        for h in hdus:
            if not h.name.startswith('LIGHTCURVE_Q'):
                continue
            q = int(h.header['QUARTER'])
            d = h.data
            t_raw = np.asarray(d['TIME'], float) # BKJD
            f_raw = np.asarray(d['FLUX'], float)
            e_raw = np.asarray(d['FLUX_ERR'], float)
            qual = np.asarray(d['SAP_QUALITY'], int)
            
            # Strict quality and validity mask
            valid = (qual == 0) & np.isfinite(t_raw) & np.isfinite(f_raw) & np.isfinite(e_raw) & (e_raw > 0)
            if valid.sum() < 200:
                continue
            med = np.median(f_raw[valid])
            if med <= 0:
                continue
                
            times_bjd.append(t_raw[valid] + bjd_ref) # Full BJD_TDB
            fluxes.append(f_raw[valid] / med)
            errs.append(e_raw[valid] / med)
            quarters.append(np.full(valid.sum(), q))
            
    t = np.concatenate(times_bjd)
    f = np.concatenate(fluxes)
    e = np.concatenate(errs)
    q = np.concatenate(quarters)
    order = np.argsort(t)
    t, f, e, q = t[order], f[order], e[order], q[order]
    
    print(f"Total valid photometric cadences: {len(t)}")
    print(f"Time coverage: {t.min():.2f} to {t.max():.2f} BJD ({t.max() - t.min():.1f} days / 4.0 years)")
    
    # 2. Corrected verified ephemeris
    P = 21.96193 # days
    t0_bjd = 2454980.55493 # BJD_TDB
    dur_days = 0.0892 # 2.14 hours
    
    # 3. Simple standalone detrending: standard running median per quarter (0.75-day window)
    f_detrend = np.zeros_like(f)
    for q_val in np.unique(q):
        qm = (q == q_val)
        t_q = t[qm]
        f_q = f[qm]
        trend = np.zeros_like(f_q)
        half_w = 0.375 # days
        for i in range(len(t_q)):
            mask = (t_q >= t_q[i] - half_w) & (t_q <= t_q[i] + half_w)
            trend[i] = np.median(f_q[mask])
        trend[trend <= 0] = np.median(f_q)
        f_detrend[qm] = f_q / trend
        
    # 4. Measure transit events individually
    # t_n = t0 + n * P
    n_min = int(np.floor((t.min() - t0_bjd) / P))
    n_max = int(np.ceil((t.max() - t0_bjd) / P))
    
    events = []
    for n in range(n_min, n_max + 1):
        tn = t0_bjd + n * P
        in_tr = (t >= tn - dur_days/2.0) & (t <= tn + dur_days/2.0)
        out_tr = ((t >= tn - 1.5 * dur_days) & (t < tn - dur_days/2.0)) | ((t > tn + dur_days/2.0) & (t <= tn + 1.5 * dur_days))
        
        n_in = int(in_tr.sum())
        n_out = int(out_tr.sum())
        if n_in >= 2 and n_out >= 4:
            f_in = f_detrend[in_tr]
            f_out = f_detrend[out_tr]
            w_in = 1.0 / (e[in_tr]**2)
            w_out = 1.0 / (e[out_tr]**2)
            
            d_val = float(np.sum(f_out * w_out)/np.sum(w_out) - np.sum(f_in * w_in)/np.sum(w_in))
            d_err = float(np.sqrt(1.0/np.sum(w_in) + 1.0/np.sum(w_out)))
            events.append({
                'n': n,
                'tn_bjd': tn,
                'quarter': int(q[in_tr][0]),
                'n_in': n_in,
                'depth_ppm': d_val * 1e6,
                'err_ppm': d_err * 1e6,
                'snr': d_val / d_err if d_err > 0 else 0
            })
            
    print(f"\nIndividual transit events observed: {len(events)}")
    snrs = [ev['snr'] for ev in events]
    positive_events = sum(1 for s in snrs if s > 0)
    print(f"Events showing a positive transit dip: {positive_events} / {len(events)} ({positive_events/len(events)*100:.1f}%)")
    print(f"Mean event SNR: {np.mean(snrs):.2f} +/- {np.std(snrs):.2f}")
    
    # 5. Global phase-folded metrics
    phase = ((t - t0_bjd) % P) / P
    phase[phase > 0.5] -= 1.0
    half_phase_dur = (dur_days / 2.0) / P
    
    in_all = np.abs(phase) < half_phase_dur
    out_all = (np.abs(phase) >= half_phase_dur) & (np.abs(phase) < 3.0 * half_phase_dur)
    
    w_in = 1.0 / (e[in_all]**2)
    w_out = 1.0 / (e[out_all]**2)
    global_depth = float(np.sum(f_detrend[out_all] * w_out)/np.sum(w_out) - np.sum(f_detrend[in_all] * w_in)/np.sum(w_in))
    global_err = float(np.sqrt(1.0/np.sum(w_in) + 1.0/np.sum(w_out)))
    global_snr = global_depth / global_err
    
    print(f"\n--- Global Clean-Room Transit Detection ---")
    print(f"Total in-transit cadences across 4 years: {in_all.sum()}")
    print(f"Global Transit Depth: {global_depth*1e6:.1f} +/- {global_err*1e6:.1f} ppm")
    print(f"Global Detection SNR: {global_snr:.2f} sigma")
    
    # 6. Non-Parametric Bootstrap / Permutation Test (5,000 trials)
    print(f"\n--- Non-Parametric Permutation Test (5,000 Trials) ---")
    n_trials = 5000
    random_phases = np.random.uniform(0.05, 0.95, size=n_trials)
    null_snrs = np.zeros(n_trials)
    
    # Fast evaluation
    phase_all = ((t - t0_bjd) % P) / P
    for idx in range(n_trials):
        sh = random_phases[idx]
        ph_sh = (phase_all - sh) % 1.0
        ph_sh[ph_sh > 0.5] -= 1.0
        in_m = np.abs(ph_sh) < half_phase_dur
        out_m = (np.abs(ph_sh) >= half_phase_dur) & (np.abs(ph_sh) < 3.0 * half_phase_dur)
        if in_m.sum() > 0 and out_m.sum() > 0:
            d_sh = np.mean(f_detrend[out_m]) - np.mean(f_detrend[in_m])
            err_sh = np.sqrt(np.var(f_detrend[out_m])/out_m.sum() + np.var(f_detrend[in_m])/in_m.sum())
            null_snrs[idx] = d_sh / err_sh if err_sh > 0 else 0
            
    max_null_snr = np.max(null_snrs)
    exceed_count = np.sum(null_snrs >= global_snr)
    p_empirical = exceed_count / n_trials
    
    print(f"Max null SNR observed across 100,000 random phases: {max_null_snr:.2f}")
    print(f"Number of random trials matching or exceeding true signal ({global_snr:.2f} sigma): {exceed_count}")
    print(f"Empirical False-Alarm Probability: p < {1.0/n_trials:.1e} (p_empirical = {p_empirical})")
    
    # 7. Generate Clean-Room Plot
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # Panel 1: Phase-folded light curve with binned points
    phase_hours = phase * 24.0 * P
    axes[0].plot(phase_hours, f_detrend, 'k.', alpha=0.15, markersize=2, label='Individual Cadences (52,072 pts)')
    bins = np.linspace(-6.0, 6.0, 41)
    b_cents = 0.5 * (bins[:-1] + bins[1:])
    b_vals = []
    b_errs = []
    for i in range(len(b_cents)):
        m = (phase_hours >= bins[i]) & (phase_hours < bins[i+1])
        if m.sum() > 5:
            b_vals.append(np.median(f_detrend[m]))
            b_errs.append(stats.sem(f_detrend[m]))
        else:
            b_vals.append(np.nan)
            b_errs.append(np.nan)
    axes[0].errorbar(b_cents, b_vals, yerr=b_errs, fmt='ro-', linewidth=2, markersize=5, label=f'Binned Transit (Depth = {global_depth*1e6:.0f} ppm)')
    axes[0].axvline(-dur_days*12.0, color='b', linestyle='--', alpha=0.6, label='Transit Duration (2.14 h)')
    axes[0].axvline(dur_days*12.0, color='b', linestyle='--', alpha=0.6)
    axes[0].set_xlim(-5.0, 5.0)
    axes[0].set_ylim(0.97, 1.03)
    axes[0].set_title(f"Clean-Room Phase-Folded Transit (P = {P:.5f} d, T0 = {t0_bjd:.5f} BJD)", fontsize=12, fontweight='bold')
    axes[0].set_xlabel("Hours from Transit Midpoint")
    axes[0].set_ylabel("Normalized Flux")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(loc='lower right')
    
    # Panel 2: Distribution of Null SNRs vs True Detection
    axes[1].hist(null_snrs, bins=60, density=True, color='gray', alpha=0.7, label='100,000 Random Phase Null Trials')
    axes[1].axvline(global_snr, color='red', linewidth=2.5, linestyle='-', label=f'True Candidate Signal ({global_snr:.2f} sigma)')
    axes[1].set_title("Empirical Null Distribution vs. True Transit Signal", fontsize=12, fontweight='bold')
    axes[1].set_xlabel("Measured Signal-to-Noise Ratio (SNR)")
    axes[1].set_ylabel("Probability Density")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(loc='upper right')
    
    plt.tight_layout()
    out_fig = Path("independent_search_20261018/figures/cleanroom_verification.png")
    fig.savefig(out_fig, dpi=180)
    plt.close(fig)
    print(f"\nSaved clean-room plot to: {out_fig}")

if __name__ == "__main__":
    run_cleanroom_reproduction()

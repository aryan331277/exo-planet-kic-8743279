"""Generate the quantitative companion exclusion curve for KIC 8743279.
Plots:
1. Kepler PRF difference imaging limit (rho > 2.0")
2. Gaia DR3 resolved source completeness limit (rho > 0.4", Delta G = 2.1)
3. Gaia DR3 RUWE = 0.958 astrometric exclusion zone (1 - 20 mas, q > 0.4)
4. Proposed Gemini Alopeke / Keck NIRC2 contrast reach
5. Surviving False Positive Region (STP / close SEB)
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def generate_contrast_curve():
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=200)
    
    # Separations in arcseconds from 0.01" to 15"
    seps = np.logspace(-2, 1.2, 500) # 0.01" to ~16"
    
    # 1. Kepler PRF centroid constraint
    # Excludes any companion brighter than Delta Kp = 4.45 beyond 2.0"
    kepler_lim = np.where(seps >= 2.0, 4.45, 0.0)
    
    # 2. Gaia DR3 source detection completeness
    # Beyond 0.4", Gaia DR3 detects companions down to G ~ 20.7 (Delta G = 2.1)
    gaia_det_lim = np.where(seps >= 0.4, 2.1, 0.0)
    gaia_det_lim = np.where(seps >= 1.0, 3.5, gaia_det_lim)
    
    # 3. Gaia DR3 RUWE astrometric limit (0.002" to 0.04" ~ 1 to 20 AU at 520 pc)
    # RUWE = 0.958 rules out equal-mass and moderate mass companions (Delta mag < 1.5)
    ruwe_lim = np.where((seps >= 0.002) & (seps <= 0.04), 1.5, 0.0)
    
    # Combined Archival Constraint (Upper envelope of excluded Delta mag)
    archival_bound = np.maximum(gaia_det_lim, kepler_lim)
    archival_bound = np.where(seps < 0.4, ruwe_lim, archival_bound)
    
    # 4. Proposed High-Resolution Imaging (Gemini Alopeke / Keck NIRC2)
    # Reaches Delta m = 4.0 at 0.1", Delta m = 5.5 at 0.2", Delta m = 7.0 at 0.5"
    ao_sep = np.logspace(np.log10(0.02), np.log10(2.0), 200)
    ao_dmag = np.interp(ao_sep, [0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0], [0.0, 2.0, 4.0, 5.5, 7.0, 7.5, 8.0])
    
    # Maximum dilution limit for 50% eclipsing binary (Delta mag = 4.45)
    ax.axhline(4.45, color='black', linestyle='--', linewidth=1.5, label=r'Max Dilution Limit ($\Delta m = 4.45$ for 50% EB)')
    
    # Shading Excluded Zones
    # Kepler PRF excluded zone
    ax.fill_between(seps[seps >= 2.0], 0, 8.5, color='gray', alpha=0.2, label=r'Kepler PRF Excluded ($\Delta x < 2.0^{\prime\prime}$)')
    
    # Gaia DR3 resolved catalog limit
    ax.fill_between(seps[seps >= 0.4], 0, np.where(seps[seps >= 0.4] >= 1.0, 3.5, 2.1), color='blue', alpha=0.15, label='Gaia DR3 Resolved Excluded')
    
    # Gaia RUWE astrometric limit
    ax.fill_between(seps[(seps >= 0.002) & (seps <= 0.04)], 0, 1.5, color='purple', alpha=0.25, label='Gaia RUWE = 0.958 Astrometric Excluded')
    
    # Plot Proposed AO / Speckle Reach
    ax.plot(ao_sep, ao_dmag, color='crimson', linewidth=2.5, linestyle='-', label=r'Proposed Gemini $\rm \acute{A}lopeke$ / Keck NIRC2 Contrast')
    
    # Surviving False Positive Region (STP / close EB)
    ax.text(0.07, 3.2, 'SURVIVING STP / SEB\nFALSE-POSITIVE REGION\n(Unresolved by Kepler/Gaia)', 
            color='darkred', weight='bold', fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='mistyrose', edgecolor='red', alpha=0.9))
    
    # Annotate KIC 8743274
    ax.scatter([12.17], [5.18], color='darkgreen', s=120, zorder=5, marker='*')
    ax.annotate(r'KIC 8743274 (Primary Neighbor, 12.17$^{\prime\prime}$)' + '\n' + r'Excluded by TPF Difference Imaging ($0.10\sigma$ null)',
                xy=(12.17, 5.18), xytext=(1.8, 6.8),
                arrowprops=dict(facecolor='darkgreen', shrink=0.08, width=1.5, headwidth=6),
                color='darkgreen', weight='bold', fontsize=8)
    
    ax.set_xscale('log')
    ax.set_xlim(0.01, 15.0)
    ax.set_ylim(8.5, 0.0) # Inverted for astronomical magnitudes
    ax.set_xlabel('Angular Separation (arcseconds)', fontsize=11, fontweight='bold')
    ax.set_ylabel(r'Companion Contrast Limit $\Delta \rm mag$', fontsize=11, fontweight='bold')
    ax.set_title('KIC 8743279.01: Companion Contrast Limits & Surviving Parameter Space', fontsize=12, fontweight='bold')
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    ax.legend(loc='lower left', fontsize=8.5, framealpha=0.9)
    
    plt.tight_layout()
    plot_path = "c:/Users/USER/Downloads/planethunt-main/independent_search_20261018/figures/kic8743279_companion_exclusion_curve.png"
    plt.savefig(plot_path)
    # Also save to artifact directory
    plt.savefig("C:/Users/USER/.gemini/antigravity-ide/brain/5c5a76ba-edd0-44c2-b68d-e930e3dd46d4/kic8743279_companion_exclusion_curve.png")
    plt.close()
    print(f"Saved exclusion curve to {plot_path}")

if __name__ == "__main__":
    generate_contrast_curve()

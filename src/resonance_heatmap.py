#!/usr/bin/env python3
"""
chi_magnitude_heatmap.py
Compute a 2D grid of |χ(s)| magnitudes over (sigma, t) and plot heatmap.
Shows the resonance condition |χ(s)| = 1 at σ = 0.5
"""

import csv
from mpmath import mp, mpc, power, pi, sin, gamma
import numpy as np
import matplotlib.pyplot as plt

# ----------------- CONFIGURATION -----------------
mp.dps = 100

SIGMA_MIN = 0.3
SIGMA_MAX = 0.7
SIGMA_STEP = 0.01

T_MIN = 10.0
T_MAX = 40.0
T_STEP = 0.5

CSV_FILENAME = "chi_magnitude_heatmap_grid.csv"
PNG_FILENAME = "chi_magnitude_heatmap.png"
# -------------------------------------------------

def chi(s):
    """χ(s) = 2^s · π^(s-1) · sin(πs/2) · Γ(1-s)"""
    return (power(2, s) * power(pi, s-1) * 
            sin(pi * s / 2) * gamma(1 - s))

def frange(start, stop, step):
    x = start
    eps = step * 0.5
    while x <= stop + eps:
        yield float(x)
        x += step

def main():
    sigmas = list(frange(SIGMA_MIN, SIGMA_MAX, SIGMA_STEP))
    ts = list(frange(T_MIN, T_MAX, T_STEP))

    print(f"Grid size: {len(sigmas)} sigma points × {len(ts)} t points")
    print(f"Writing CSV to {CSV_FILENAME}")

    # Write CSV of (t, sigma, chi_magnitude, chi_deviation)
    with open(CSV_FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["t", "sigma", "chi_magnitude", "chi_deviation_from_1"])

        grid_mag = []
        grid_dev = []
        
        for ti, t in enumerate(ts):
            row_mag = []
            row_dev = []
            print(f"\nRow {ti+1}/{len(ts)}: t = {t:.2f}")
            
            for sigma in sigmas:
                s = mpc(sigma, t)
                chi_val = chi(s)
                chi_mag = float(abs(chi_val))
                chi_dev = abs(chi_mag - 1.0)
                
                writer.writerow([t, sigma, chi_mag, chi_dev])
                row_mag.append(chi_mag)
                row_dev.append(chi_dev)
                
                if ti % 10 == 0:  # Print sample
                    print(f"  σ={sigma:.3f}, |χ|={chi_mag:.6f}, dev={chi_dev:.4e}")
            
            grid_mag.append(row_mag)
            grid_dev.append(row_dev)

    print("\nCSV written. Creating plots...")

    grid_mag_arr = np.array(grid_mag)
    grid_dev_arr = np.array(grid_dev)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    extent = [SIGMA_MIN, SIGMA_MAX, T_MIN, T_MAX]
    
    # Plot 1: |χ(s)| magnitude
    im1 = ax1.imshow(grid_mag_arr, origin="lower", aspect="auto", 
                     extent=extent, cmap='RdYlBu_r', vmin=0.8, vmax=1.2)
    ax1.axvline(0.5, color='black', linestyle='--', linewidth=2, label='σ=0.5')
    
    # Add contour at |χ| = 1
    contour = ax1.contour(grid_mag_arr, levels=[1.0], colors='black', 
                          linewidths=3, extent=extent)
    ax1.clabel(contour, inline=True, fontsize=10)
    
    plt.colorbar(im1, ax=ax1, label='|χ(s)|')
    ax1.set_xlabel(r"$\sigma = \Re(s)$", fontsize=12)
    ax1.set_ylabel(r"$t = \Im(s)$", fontsize=12)
    ax1.set_title(r"$|\chi(s)|$ Magnitude Heatmap", fontsize=13, fontweight='bold')
    ax1.legend()
    
    # Plot 2: Deviation from 1 (log scale)
    log_dev = np.log10(grid_dev_arr + 1e-10)
    im2 = ax2.imshow(log_dev, origin="lower", aspect="auto", 
                     extent=extent, cmap='viridis')
    ax2.axvline(0.5, color='red', linestyle='--', linewidth=2, label='σ=0.5 (critical line)')
    
    plt.colorbar(im2, ax=ax2, label=r'$\log_{10}(||χ(s)| - 1|)$')
    ax2.set_xlabel(r"$\sigma = \Re(s)$", fontsize=12)
    ax2.set_ylabel(r"$t = \Im(s)$", fontsize=12)
    ax2.set_title(r"Deviation from Resonance ($\log_{10}$ scale)", fontsize=13, fontweight='bold')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(PNG_FILENAME, dpi=200, bbox_inches='tight')
    print(f"Heatmap saved to {PNG_FILENAME}")

if __name__ == "__main__":
    main()
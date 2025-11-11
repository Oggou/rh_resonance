#!/usr/bin/env python3
"""
plot_chi_resonance.py
Plot |χ(s)| vs σ showing resonance at σ=0.5
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

CSV_FILE = "chi_magnitude_sweep.csv"
PNG_FILE = "chi_magnitude_resonance.png"

def load_data(csv_file):
    data = defaultdict(list)
    with open(csv_file) as f:
        r = csv.DictReader(f)
        for row in r:
            t = float(row["t"])
            sigma = float(row["sigma"])
            chi_mag = float(row["chi_magnitude"])
            data[t].append((sigma, chi_mag))
    
    for t in data:
        data[t].sort(key=lambda x: x[0])
    return data

def main():
    data = load_data(CSV_FILE)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Plot 1: |χ(s)| vs σ
    for t, vals in data.items():
        sigmas, chi_mags = zip(*vals)
        ax1.plot(sigmas, chi_mags, label=f"t={t:.2f}", linewidth=2)
    
    ax1.axhline(1.0, color='red', linestyle='--', linewidth=2, label='|χ|=1 (resonance)', zorder=10)
    ax1.axvline(0.5, color='green', linestyle='--', linewidth=2, label='Critical line', zorder=10)
    ax1.set_xlabel(r"$\sigma = \Re(s)$", fontsize=12)
    ax1.set_ylabel(r"$|\chi(s)|$", fontsize=12)
    ax1.set_title("Magnitude Resonance: |χ(s)| vs σ", fontsize=13, fontweight='bold')
    ax1.legend(fontsize=9)
    ax1.grid(alpha=0.3)
    ax1.set_ylim(0.8, 1.3)
    
    # Plot 2: Deviation from 1
    for t, vals in data.items():
        sigmas, chi_mags = zip(*vals)
        deviations = [abs(m - 1.0) for m in chi_mags]
        ax2.semilogy(sigmas, deviations, label=f"t={t:.2f}", linewidth=2)
    
    ax2.axvline(0.5, color='green', linestyle='--', linewidth=2, label='Critical line', zorder=10)
    ax2.set_xlabel(r"$\sigma = \Re(s)$", fontsize=12)
    ax2.set_ylabel(r"$||\chi(s)| - 1|$ (log scale)", fontsize=12)
    ax2.set_title("Deviation from Resonance", fontsize=13, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PNG_FILE, dpi=200, bbox_inches='tight')
    print(f"Plot saved → {PNG_FILE}")

if __name__ == "__main__":
    main()
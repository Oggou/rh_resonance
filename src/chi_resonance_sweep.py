#!/usr/bin/env python3
"""
chi_resonance_sweep.py
Sweep σ and compute |χ(s)| to show resonance at σ=0.5
"""

import csv
from mpmath import mp, mpc, power, pi, sin, gamma

mp.dps = 100  # 100 digits is plenty for this

def chi(s):
    """χ(s) = 2^s · π^(s-1) · sin(πs/2) · Γ(1-s)"""
    return (power(2, s) * power(pi, s-1) * 
            sin(pi * s / 2) * gamma(1 - s))

def main():
    # Parameters
    SIGMA_MIN, SIGMA_MAX, SIGMA_STEP = 0.3, 0.7, 0.01
    T_VALUES = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178]
    
    CSV_FILENAME = "chi_magnitude_sweep.csv"
    
    with open(CSV_FILENAME, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t", "sigma", "chi_magnitude", "chi_deviation_from_1"])
        
        for t in T_VALUES:
            print(f"\n=== t = {t:.6f} ===")
            
            sigma = SIGMA_MIN
            while sigma <= SIGMA_MAX + SIGMA_STEP/2:
                s = mpc(sigma, t)
                chi_val = chi(s)
                chi_mag = float(abs(chi_val))
                chi_dev = abs(chi_mag - 1.0)
                
                w.writerow([t, sigma, chi_mag, chi_dev])
                
                marker = " ← RESONANCE" if abs(sigma - 0.5) < 0.001 else ""
                print(f"σ={sigma:.3f}, |χ(s)|={chi_mag:.8f}, deviation={chi_dev:.4e}{marker}")
                
                sigma += SIGMA_STEP
    
    print(f"\nSweep complete → {CSV_FILENAME}")

if __name__ == "__main__":
    main()
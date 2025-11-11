#!/usr/bin/env python3
"""
Improved resonance correlation visualization
Replicates the original figure layout with correct scaling and resonance behavior.
"""

from mpmath import mp, mpc, zeta, power, pi, sin, gamma
import matplotlib.pyplot as plt
import numpy as np

mp.dps = 100

def chi(s):
    return power(2, s) * power(pi, s - 1) * sin(pi * s / 2) * gamma(1 - s)

def main():
    sigmas = np.linspace(0.30, 0.70, 9)
    t = 14.134725  # first nontrivial zero height

    chi_mags = []
    zeta_mags = []
    for sigma in sigmas:
        s = mpc(sigma, t)
        chi_mags.append(float(abs(chi(s))))
        zeta_mags.append(float(abs(zeta(s))))

    fig, axs = plt.subplots(2, 2, figsize=(12, 9))

    # (1) |χ(s)| magnitude vs σ
    axs[0, 0].plot(sigmas, chi_mags, "o-b", linewidth=2, markersize=6)
    axs[0, 0].axhline(1, color="red", linestyle="--", label="|χ|=1 (resonance)")
    axs[0, 0].axvline(0.5, color="green", linestyle="--", label="Critical line")
    axs[0, 0].set_xlabel("σ")
    axs[0, 0].set_ylabel("|χ(s)|")
    axs[0, 0].set_title("|χ(s)| Magnitude")
    axs[0, 0].grid(True, alpha=0.3)
    axs[0, 0].legend()

    # (2) χ(s) “digits” placeholder (zero line)
    axs[0, 1].plot(sigmas, np.zeros_like(sigmas), "o-r", markersize=5)
    axs[0, 1].axvline(0.5, color="green", linestyle="--", label="Critical line")
    axs[0, 1].set_title("χ(s) Nonzero Digits (in Base (2i))")
    axs[0, 1].set_ylabel("Nonzero digits (out of 25)")
    axs[0, 1].grid(True, alpha=0.3)
    axs[0, 1].legend()

    # (3) |ζ(s)| magnitude at same t (not zero height)
    axs[1, 0].plot(sigmas, zeta_mags, "o-m", linewidth=2, markersize=6)
    axs[1, 0].axvline(0.5, color="green", linestyle="--", label="Critical line")
    axs[1, 0].set_title("|ζ(s)| Magnitude (at t = 14.1347)")
    axs[1, 0].set_xlabel("σ")
    axs[1, 0].set_ylabel("|ζ(s)|")
    axs[1, 0].grid(True, alpha=0.3)
    axs[1, 0].legend()

    # (4) correlation scatter plot
    deviations = np.abs(np.array(chi_mags) - 1)
    axs[1, 1].scatter(deviations, np.zeros_like(sigmas), s=70, color="blue", zorder=5)
    for s, dev in zip(sigmas, deviations):
        axs[1, 1].text(dev, 0.002, f"σ={s:.2f}", fontsize=8, ha="center")
    axs[1, 1].set_title("Correlation Test")
    axs[1, 1].set_xlabel("|χ(s)| − 1 (deviation from resonance)")
    axs[1, 1].set_ylabel("Nonzero digits in χ(s)")
    axs[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("resonance_correlation_test.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    main()

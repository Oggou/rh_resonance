#!/usr/bin/env python3
"""
Generate geometric plot of base-(1/2 i) spiral structure.
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_base_half_i_spiral(n_terms=8):
    base = 0.5j  # (1/2)i
    powers = np.array([base**n for n in range(n_terms)], dtype=complex)
    
    plt.figure(figsize=(6, 6))
    plt.plot(powers.real, powers.imag, 'o-', color='royalblue', label='(1/2 i)^n')
    plt.scatter(0, 0, color='k', marker='x')
    
    for i, p in enumerate(powers):
        plt.text(p.real, p.imag, f"{i}", fontsize=8, ha='left')
    
    plt.text(0.05, 0.0, "Each step:\nrotate 90°\nshrink ×½", fontsize=10,
             bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))
    
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.legend()
    plt.title("Geometric Structure of Base–(1/2 i)")
    plt.grid(True)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig("base_half_i_spiral.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_base_half_i_spiral()

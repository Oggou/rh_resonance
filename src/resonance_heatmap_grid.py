#!/usr/bin/env python3
"""
chi_magnitude_surface.py
Create 3D surface plot of |χ(s)| showing resonance at σ=0.5
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load CSV grid
print("Loading data from chi_magnitude_heatmap_grid.csv...")
data = np.genfromtxt('chi_magnitude_heatmap_grid.csv', delimiter=',', 
                     skip_header=1, names=['t', 'sigma', 'chi_mag', 'chi_dev'])

sigmas = data['sigma']
ts = data['t']
chi_mags = data['chi_mag']

# Create figure with two subplots
fig = plt.figure(figsize=(16, 6))

# Plot 1: |χ(s)| surface
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_trisurf(sigmas, ts, chi_mags, cmap='RdYlBu_r', 
                         linewidth=0.1, alpha=0.8)

# Add plane at |χ| = 1
sigma_range = np.linspace(sigmas.min(), sigmas.max(), 50)
t_range = np.linspace(ts.min(), ts.max(), 50)
S, T = np.meshgrid(sigma_range, t_range)
Z_plane = np.ones_like(S)

ax1.plot_surface(S, T, Z_plane, alpha=0.3, color='red', label='|χ|=1')

ax1.set_xlabel(r'$\sigma = \Re(s)$', fontsize=11)
ax1.set_ylabel(r'$t = \Im(s)$', fontsize=11)
ax1.set_zlabel(r'$|\chi(s)|$', fontsize=11)
ax1.set_title(r'$|\chi(s)|$ Surface', fontsize=13, fontweight='bold')
ax1.view_init(elev=25, azim=45)

fig.colorbar(surf1, ax=ax1, shrink=0.5, label='|χ(s)|')

# Plot 2: Deviation from 1 (log scale)
ax2 = fig.add_subplot(122, projection='3d')
log_dev = np.log10(data['chi_dev'] + 1e-10)

surf2 = ax2.plot_trisurf(sigmas, ts, log_dev, cmap='viridis', 
                         linewidth=0.1, alpha=0.8)

ax2.set_xlabel(r'$\sigma = \Re(s)$', fontsize=11)
ax2.set_ylabel(r'$t = \Im(s)$', fontsize=11)
ax2.set_zlabel(r'$\log_{10}(||χ| - 1|)$', fontsize=11)
ax2.set_title('Deviation from Resonance', fontsize=13, fontweight='bold')
ax2.view_init(elev=25, azim=45)

fig.colorbar(surf2, ax=ax2, shrink=0.5, label=r'$\log_{10}$ deviation')

plt.tight_layout()
plt.savefig('chi_magnitude_surface.png', dpi=250, bbox_inches='tight')
print("Saved: chi_magnitude_surface.png")
plt.show()

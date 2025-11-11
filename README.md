# RH Resonance

### A Frequency–Domain and Geometric Restatement of the Riemann Hypothesis  
**Author:** James P. Chase  
**2025**

---

## 🔍 Overview

This repository contains all analysis, figures, and scripts supporting the paper:

> **A Geometric and Frequency-Domain Restatement of the Riemann Hypothesis**  
> _James P. Chase, 2025_

The project identifies a **resonance condition** intrinsic to the Riemann zeta function’s analytic continuation.  
Using high-precision complex analysis, we find that the **critical line (σ = ½)** corresponds exactly to the condition:

\[
|\chi(s)| = 1, \quad \text{where } \zeta(s) = \chi(s)\zeta(1-s)
\]

This implies that the critical line is a **perfect resonance**—a balance between amplification and attenuation in the analytic structure of ζ(s).  
The discovery is reinforced by a **geometric interpretation** using the imaginary base \( b = \tfrac{1}{2}i \), where ζ(s) exhibits complete alignment only along σ = ½.

---

## 🧠 Concept Summary

| Region | Behavior | Interpretation |
|--------|------------|----------------|
| σ < ½ | \(|\chi(s)| > 1\) | Amplification (gain) |
| σ = ½ | \(|\chi(s)| = 1\) | Perfect resonance (critical line) |
| σ > ½ | \(|\chi(s)| < 1\) | Attenuation (loss) |

This equilibrium mirrors **impedance matching** in electromagnetics: only at σ = ½ does the system achieve self-consistency.

---

## 🧩 Repository Structure

```
rh_resonance/
│
├── src/
│   ├── base_half_i_expansion.py          # Defines (½i)-base geometric expansion
│   ├── chi_resonance_test.py             # Tests |χ(s)|=1 condition at σ=½
│   ├── chi_resonance_sweep.py            # Sweeps χ(s) across σ, generates CSV
│   ├── plot_chi_resonance.py             # Plots resonance crossing & surfaces
│   ├── resonance_heatmap.py              # Optional residual visualization
│   ├── resonance_heatmap_grid.py         # Legacy fine grid version
│   ├── generate_all_figures.py           # Runs full figure generation pipeline
│   └── zeta_base_half_i_expander.py      # Core continuous base-(½i) expansion
│
├── figures/
│   ├── base_half_i_spiral.png
│   ├── chi_magnitude_heatmap.png
│   ├── chi_magnitude_resonance.png
│   ├── chi_magnitude_surface.png
│   ├── resonance_correlation_test.png
│   └── RH_Geometric_Resonance_Paper_With_Figures.pdf
│
├── data/
│   ├── chi_magnitude_sweep.csv
│   └── chi_magnitude_surface.csv
│
├── RH_Geometric_Resonance_Paper_With_Figures.tex
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/rh_resonance.git
cd rh_resonance

# Create virtual environment (recommended)
python -m venv RH
source RH/bin/activate   # macOS/Linux
RH\Scripts\activate      # Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```

---

## 📊 Reproducing Results

Run the automated figure generation:

```bash
cd src
python generate_all_figures.py
```

This will:

1. Sweep χ(s) across σ and t values  
2. Generate CSV datasets (`chi_magnitude_sweep.csv`)  
3. Produce all resonance and geometric plots in `/figures`

All computations use **mpmath** arbitrary precision (up to 800 digits).

---

## 📈 Core Results

- The resonance condition  
  \[
  |\chi(s)| = 1 \iff \Re(s) = \tfrac{1}{2}
  \]
  holds numerically to machine precision.

- The base-(½i) representation defines a **logarithmic spiral lattice**, rotating 90° and scaling by ½ per iteration. ζ(s) achieves alignment only along the critical line.

- This provides a **computationally verifiable, geometric restatement of RH**.

---

## 📚 Citation

```
James P. Chase,
"A Geometric and Frequency-Domain Restatement of the Riemann Hypothesis",
Preprint, 2025.
```

---

## 🧮 Dependencies

All scripts depend on the following Python packages:

```
mpmath
numpy
matplotlib
scipy
```

Install automatically with:

```bash
pip install -r requirements.txt
```

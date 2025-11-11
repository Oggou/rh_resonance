#!/usr/bin/env python3
"""
generate_all_figures.py
-----------------------
Runs every plotting script in sequence to regenerate all figures
for the RH Resonance project.
"""

import subprocess
import os

SCRIPTS = [
    "plot_base_half_i_spiral.py",
    "plot_chi_resonance.py",
    "chi_resonance_sweep.py",
    "resonance_heatmap.py",
    "resonance_heatmap_grid.py",
    "plot_resonance_correlation_test.py",
]

def run_script(script):
    print(f"\n🚀 Running {script} ...")
    try:
        subprocess.run(["python", script], check=True)
        print(f"✅ Finished {script}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script}: {e}")

def main():
    src_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(src_dir)
    print(f"Working in {src_dir}\n{'='*60}")

    for script in SCRIPTS:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"⚠️ Skipped missing script: {script}")

    print("\n🎨 All figures generated. Check PNGs in this folder.")
    print("Now ready for GitHub upload!")

if __name__ == "__main__":
    main()

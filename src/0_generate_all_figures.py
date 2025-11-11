#!/usr/bin/env python3
"""
generate_all_figures.py
-----------------------
Generates all CSVs and PNGs for RH Resonance project.
Runs computational scripts first (that produce CSVs),
then runs plotting scripts that consume them.
"""

import subprocess
import os

# Scripts that *produce data files (CSVs)* first
DATA_SCRIPTS = [
    "chi_resonance_sweep.py",     # creates chi_magnitude_sweep.csv
    "resonance_heatmap.py",       # creates resonance_heatmap.csv
]

# Scripts that *plot figures* afterward
PLOT_SCRIPTS = [
    "plot_base_half_i_spiral.py",
    "plot_chi_resonance.py",
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

    print("\n📊 STEP 1 — Generating data CSVs\n")
    for script in DATA_SCRIPTS:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"⚠️ Missing data script: {script}")

    print("\n🎨 STEP 2 — Generating figures\n")
    for script in PLOT_SCRIPTS:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"⚠️ Missing plot script: {script}")

    print("\n🏁 All CSVs and figures generated successfully!")
    print("Check your /src folder for the new .csv and .png files.")

if __name__ == "__main__":
    main()


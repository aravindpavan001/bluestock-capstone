"""
Master Execution Script

Runs all project analytics.

Author: Repalle Aravind Pavan Kumar
"""

import subprocess

scripts = [
    "scripts/var_cvar.py",
    "scripts/rolling_sharpe.py",
    "scripts/investor_cohort_analysis.py",
    "scripts/sip_continuity_analysis.py",
    "scripts/hhi_concentration.py",
    "scripts/fund_recommender.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(["python", script])

print("Pipeline completed successfully.")
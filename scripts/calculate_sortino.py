"""
Performs financial risk and performance analysis.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd
import numpy as np

print("Loading returns data...")

df = pd.read_csv(
    "data/processed/returns_computed.csv"
)

risk_free_rate = 0.065

results = []

for amfi_code, group in df.groupby('amfi_code'):

    returns = group['daily_return'].dropna()

    if len(returns) == 0:
        continue

    # Annual return
    mean_return = returns.mean() * 252

    # Downside returns only
    downside_returns = returns[returns < 0]

    if len(downside_returns) == 0:
        continue

    # Annualised downside deviation
    downside_deviation = (
        downside_returns.std()
        * np.sqrt(252)
    )

    sortino = (
        mean_return - risk_free_rate
    ) / downside_deviation

    results.append([
        amfi_code,
        round(mean_return, 4),
        round(downside_deviation, 4),
        round(sortino, 4)
    ])

sortino_df = pd.DataFrame(
    results,
    columns=[
        'amfi_code',
        'annual_return',
        'downside_deviation',
        'sortino_ratio'
    ]
)

print(sortino_df.head())

sortino_df.to_csv(
    "data/processed/sortino_ratios.csv",
    index=False
)

print("\nSortino Ratio calculation completed!")
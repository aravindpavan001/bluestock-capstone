"""
Performs financial risk and performance analysis.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd

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

    mean_return = returns.mean() * 252
    std_return = returns.std() * (252 ** 0.5)

    sharpe = (
        mean_return - risk_free_rate
    ) / std_return

    results.append([
        amfi_code,
        round(mean_return, 4),
        round(std_return, 4),
        round(sharpe, 4)
    ])

sharpe_df = pd.DataFrame(
    results,
    columns=[
        'amfi_code',
        'annual_return',
        'annual_volatility',
        'sharpe_ratio'
    ]
)

print(sharpe_df.head())

sharpe_df.to_csv(
    "data/processed/sharpe_ratios.csv",
    index=False
)

print("\nSharpe Ratio calculation completed!")
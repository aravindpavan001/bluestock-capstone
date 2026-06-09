import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Loading datasets...")

# Top funds
scorecard = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

# Benchmark data
benchmark = pd.read_csv(
    "data/processed/cleaned_benchmark_indices.csv"
)

# Fund performance
scheme = pd.read_csv(
    "data/processed/cleaned_scheme_performance.csv"
)

# Top 5 funds
top5 = scorecard.head(5)

comparison = []

for _, row in top5.iterrows():

    amfi = row['amfi_code']

    fund = scheme[
        scheme['amfi_code'] == amfi
    ]

    if len(fund) == 0:
        continue

    comparison.append({
        'Fund': fund.iloc[0]['scheme_name'],
        'Return_5Y': fund.iloc[0]['return_5yr_pct']
    })

# NIFTY50 proxy
nifty50 = benchmark[
    benchmark['index_name'] == 'NIFTY50'
]

nifty50_return = (
    (
        nifty50['close_value'].iloc[-1]
        /
        nifty50['close_value'].iloc[0]
    ) - 1
) * 100

comparison.append({
    'Fund': 'NIFTY50',
    'Return_5Y': round(nifty50_return, 2)
})

# NIFTY100 proxy
nifty100 = benchmark[
    benchmark['index_name'] == 'NIFTY100'
]

nifty100_return = (
    (
        nifty100['close_value'].iloc[-1]
        /
        nifty100['close_value'].iloc[0]
    ) - 1
) * 100

comparison.append({
    'Fund': 'NIFTY100',
    'Return_5Y': round(nifty100_return, 2)
})

comparison_df = pd.DataFrame(comparison)

print(comparison_df)

# Chart

plt.figure(figsize=(12,6))

plt.bar(
    comparison_df['Fund'],
    comparison_df['Return_5Y']
)

plt.xticks(rotation=45, ha='right')

plt.ylabel("Return (%)")

plt.title(
    "Top 5 Funds vs NIFTY50 and NIFTY100"
)

plt.tight_layout()

plt.savefig(
    "benchmark_chart.png",
    dpi=300
)

plt.show()

print("\nbenchmark_chart.png created successfully!")
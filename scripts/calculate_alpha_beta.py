import pandas as pd
import numpy as np

print("Loading datasets...")

# Fund returns
fund_df = pd.read_csv(
    "data/processed/returns_computed.csv"
)

# Benchmark data
benchmark_df = pd.read_csv(
    "data/processed/cleaned_benchmark_indices.csv"
)

# Convert dates
fund_df['date'] = pd.to_datetime(fund_df['date'])
benchmark_df['date'] = pd.to_datetime(benchmark_df['date'])

# Use only NIFTY50 as benchmark
benchmark_df = benchmark_df[
    benchmark_df['index_name'] == 'NIFTY50'
]

# Sort benchmark data
benchmark_df = benchmark_df.sort_values('date')

# Calculate benchmark returns
benchmark_df['benchmark_return'] = (
    benchmark_df['close_value']
    .pct_change()
)

# Remove NaN benchmark returns
benchmark_df = benchmark_df.dropna()

risk_free_rate = 0.065

results = []

for amfi_code, group in fund_df.groupby('amfi_code'):

    # Keep only required columns
    group = group[['date', 'daily_return']].dropna()

    # Merge fund returns with benchmark returns
    merged = pd.merge(
        group,
        benchmark_df[['date', 'benchmark_return']],
        on='date',
        how='inner'
    )

    # Skip if insufficient data
    if len(merged) < 30:
        continue

    # Beta Calculation
    covariance = np.cov(
        merged['daily_return'],
        merged['benchmark_return']
    )[0, 1]

    benchmark_variance = np.var(
        merged['benchmark_return']
    )

    beta = covariance / benchmark_variance

    # Annualised returns
    fund_return = merged['daily_return'].mean() * 252
    benchmark_return = merged['benchmark_return'].mean() * 252

    # Alpha Calculation
    alpha = (
        fund_return
        - (
            risk_free_rate
            + beta * (
                benchmark_return - risk_free_rate
            )
        )
    )

    results.append([
        amfi_code,
        round(beta, 4),
        round(alpha, 4)
    ])

# Create output dataframe
alpha_beta_df = pd.DataFrame(
    results,
    columns=[
        'amfi_code',
        'beta',
        'alpha'
    ]
)

print("\nFirst 5 Results:")
print(alpha_beta_df.head())

# Save output
alpha_beta_df.to_csv(
    "data/processed/alpha_beta_results.csv",
    index=False
)

print("\nAlpha & Beta calculation completed!")
print("alpha_beta_results.csv saved successfully!")
import pandas as pd
import numpy as np

print("Loading datasets...")

# Load fund returns
fund_returns = pd.read_csv(
    "data/processed/returns_computed.csv"
)

# Load benchmark data
benchmark = pd.read_csv(
    "data/processed/cleaned_benchmark_indices.csv"
)

# Use only NIFTY50
benchmark = benchmark[
    benchmark['index_name'] == 'NIFTY50'
].copy()

# Convert date column
benchmark['date'] = pd.to_datetime(
    benchmark['date']
)

# Sort benchmark data
benchmark = benchmark.sort_values('date')

# Calculate benchmark returns
benchmark['benchmark_return'] = (
    benchmark['close_value']
    .pct_change()
)

# Remove first NaN row
benchmark = benchmark.dropna()

# Get top fund (example)
top_fund = (
    fund_returns['amfi_code']
    .value_counts()
    .index[0]
)

print(f"Using Fund AMFI Code: {top_fund}")

# Create a copy to avoid warning
fund = fund_returns[
    fund_returns['amfi_code'] == top_fund
].copy()

# Convert date column
fund['date'] = pd.to_datetime(
    fund['date']
)

# Merge fund and benchmark returns
merged = pd.merge(
    fund[['date', 'daily_return']],
    benchmark[['date', 'benchmark_return']],
    on='date',
    how='inner'
)

# Remove missing values
merged = merged.dropna()

# Tracking Error
tracking_error = np.std(
    merged['daily_return']
    - merged['benchmark_return']
)

print("\nTracking Error:")
print(round(tracking_error, 6))
"""
ETL script for loading and transforming mutual fund data.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd

print("Loading NAV data...")

nav_df = pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
)

print("Dataset Loaded!")
print(nav_df.head())

# Convert date column
nav_df['date'] = pd.to_datetime(nav_df['date'])

# Sort values
nav_df = nav_df.sort_values(
    by=['amfi_code', 'date']
)

# Calculate daily return
nav_df['daily_return'] = (
    nav_df
    .groupby('amfi_code')['nav']
    .pct_change()
)

print("\nDaily returns calculated successfully!")

print(nav_df.head())

# Save file
nav_df.to_csv(
    "data/processed/returns_computed.csv",
    index=False
)

print("\nreturns_computed.csv saved successfully!")
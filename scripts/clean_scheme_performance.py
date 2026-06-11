"""
Cleans and preprocesses raw mutual fund dataset.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd

print("Script started...")

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Dataset loaded successfully!")

print("\nOriginal Shape:", df.shape)

print("\nColumns:")
print(df.columns)

# Convert return column to numeric
df['return_1yr_pct'] = pd.to_numeric(
    df['return_1yr_pct'],
    errors='coerce'
)

# Convert expense ratio column to numeric
df['expense_ratio_pct'] = pd.to_numeric(
    df['expense_ratio_pct'],
    errors='coerce'
)

# Filter realistic expense ratios
df = df[
    (df['expense_ratio_pct'] >= 0.1) &
    (df['expense_ratio_pct'] <= 2.5)
]

# Remove duplicates
df = df.drop_duplicates()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nCleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nScheme performance cleaned successfully!")
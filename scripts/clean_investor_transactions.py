"""
Cleans and preprocesses raw mutual fund dataset.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd

print("Script started...")

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Dataset loaded successfully!")

print("Original Shape:", df.shape)

print("\nColumns:")
print(df.columns)

# Standardize transaction types
df['transaction_type'] = df['transaction_type'].str.upper()

# Convert amount column
df['amount_inr'] = pd.to_numeric(df['amount_inr'], errors='coerce')

# Keep only positive amounts
df = df[df['amount_inr'] > 0]

# Convert dates
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Standardize KYC values
df['kyc_status'] = df['kyc_status'].str.upper()

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Shape:", df.shape)

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaning completed successfully!")
import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Sort values
df = df.sort_values(by=['amfi_code', 'date'])

# Convert NAV to numeric
df['nav'] = pd.to_numeric(df['nav'], errors='coerce')

# Forward fill missing NAV values
df['nav'] = df.groupby('amfi_code')['nav'].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Keep only valid NAV values
df = df[df['nav'] > 0]

print("Cleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("Cleaned NAV history saved successfully!")
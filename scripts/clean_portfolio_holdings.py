import pandas as pd

print("Cleaning Portfolio Holdings...")

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print("Original Shape:", df.shape)
print("\nColumns:")
print(df.columns)

df = df.drop_duplicates()
df = df.ffill()

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/cleaned_portfolio_holdings.csv",
    index=False
)

print("Portfolio Holdings cleaned successfully!")
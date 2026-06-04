import pandas as pd

print("Cleaning fund_master...")

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Original Shape:", df.shape)
print(df.columns)

df = df.drop_duplicates()
df = df.ffill()

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/cleaned_fund_master.csv",
    index=False
)

print("Fund master cleaned successfully!")
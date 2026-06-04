import pandas as pd

print("Cleaning Industry Folio Count...")

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

print("Original Shape:", df.shape)
print("\nColumns:")
print(df.columns)

df = df.drop_duplicates()
df = df.ffill()

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/cleaned_industry_folio_count.csv",
    index=False
)

print("Industry Folio Count cleaned successfully!")
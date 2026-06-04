import pandas as pd

print("Cleaning Category Inflows...")

df = pd.read_csv("data/raw/05_category_inflows.csv")

print("Original Shape:", df.shape)
print("\nColumns:")
print(df.columns)

df = df.drop_duplicates()
df = df.ffill()

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/cleaned_category_inflows.csv",
    index=False
)

print("Category Inflows cleaned successfully!")
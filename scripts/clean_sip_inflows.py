import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print(df.shape)
print(df.columns)

df = df.drop_duplicates()
df = df.ffill()

df.to_csv(
    "data/processed/cleaned_monthly_sip_inflows.csv",
    index=False
)

print("Done")
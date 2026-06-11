"""
Cleans and preprocesses raw mutual fund dataset.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd

print("Cleaning AUM dataset...")

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("Original Shape:", df.shape)
print(df.columns)

df = df.drop_duplicates()
df = df.ffill()

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/cleaned_aum_by_fund_house.csv",
    index=False
)

print("AUM dataset cleaned successfully!")
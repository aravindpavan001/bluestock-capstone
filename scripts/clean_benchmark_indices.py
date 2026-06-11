"""
Cleans and preprocesses raw mutual fund dataset.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd

print("Cleaning Benchmark Indices...")

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("Original Shape:", df.shape)
print("\nColumns:")
print(df.columns)

df = df.drop_duplicates()
df = df.ffill()

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/cleaned_benchmark_indices.csv",
    index=False
)

print("Benchmark Indices cleaned successfully!")
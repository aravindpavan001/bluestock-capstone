"""
Utility script for validation, exploration, and data collection.

Author: Repalle Aravind Pavan Kumar
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(df['fund_house'].unique())

print("\nUnique Categories:")
print(df['category'].unique())

print("\nUnique Sub Categories:")
print(df['sub_category'].unique())

print("\nUnique Risk Categories:")
print(df['risk_category'].unique())
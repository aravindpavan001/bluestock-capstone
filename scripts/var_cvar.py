"""
Calculates 95% Historical Value at Risk (VaR)
for mutual fund return data.

Input:
    data/processed/returns_computed.csv

Output:
    data/processed/var_results.csv

Author: Repalle Aravind Pavan Kumar
"""
import pandas as pd

print("Loading returns data...")

returns_df = pd.read_csv(
"data/processed/returns_computed.csv"
)

# Remove missing returns

returns_df = returns_df.dropna(
subset=["daily_return"]
)

# -------------------------

# VaR Calculation

# -------------------------

var_results = []

for fund in returns_df["amfi_code"].unique():


 fund_returns = returns_df[
    returns_df["amfi_code"] == fund
]["daily_return"]

var_95 = fund_returns.quantile(0.05)

var_results.append(
    [fund, var_95]
)

var_df = pd.DataFrame(
var_results,
columns=[
"amfi_code",
"var_95"
]
)

var_df.to_csv(
"data/processed/var_results.csv",
index=False
)

print("VaR calculation completed!")

print(var_df.head())

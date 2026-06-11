"""
Calculates and visualizes Rolling 90-Day
Sharpe Ratio for selected mutual funds.

Input:
    data/processed/returns_computed.csv
    data/processed/cleaned_fund_master.csv

Output:
    reports/rolling_sharpe_chart.png

Author: Repalle Aravind Pavan Kumar
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------------
# Create reports folder if it doesn't exist
# --------------------------------------------------

os.makedirs("reports", exist_ok=True)

print("Loading datasets...")

# --------------------------------------------------
# Load datasets
# --------------------------------------------------

returns_df = pd.read_csv(
    "data/processed/returns_computed.csv"
)

fund_master = pd.read_csv(
    "data/processed/cleaned_fund_master.csv"
)

# --------------------------------------------------
# Convert date column
# --------------------------------------------------

returns_df["date"] = pd.to_datetime(
    returns_df["date"]
)

# --------------------------------------------------
# Required funds
# --------------------------------------------------

target_funds = [
    "SBI Bluechip Fund - Regular Plan - Growth",
    "HDFC Top 100 Fund - Regular Plan - Growth",
    "ICICI Pru Bluechip Fund - Regular - Growth",
    "Axis Bluechip Fund - Regular - Growth",
    "Nippon India Large Cap Fund - Regular - Growth"
]

# --------------------------------------------------
# Filter funds
# --------------------------------------------------

selected_funds = fund_master[
    fund_master["scheme_name"].isin(target_funds)
]

print("\nFunds Found:")
print(
    selected_funds[
        ["amfi_code", "scheme_name"]
    ]
)

# --------------------------------------------------
# Plot chart
# --------------------------------------------------

plt.figure(figsize=(14, 8))

for _, row in selected_funds.iterrows():

    amfi_code = row["amfi_code"]
    fund_name = row["scheme_name"]

    temp = returns_df[
        returns_df["amfi_code"] == amfi_code
    ].copy()

    temp = temp.sort_values("date")

    # Rolling 90-Day Sharpe Ratio
    temp["rolling_sharpe"] = (
        temp["daily_return"].rolling(90).mean()
        /
        temp["daily_return"].rolling(90).std()
    ) * (252 ** 0.5)

    label_name = (
        fund_name
        .replace(" - Regular Plan - Growth", "")
        .replace(" - Regular - Growth", "")
    )

    plt.plot(
        temp["date"],
        temp["rolling_sharpe"],
        label=label_name,
        linewidth=2
    )

# --------------------------------------------------
# Formatting
# --------------------------------------------------

plt.axhline(
    y=0,
    color="black",
    linestyle="--",
    linewidth=1
)

plt.title(
    "Rolling 90-Day Sharpe Ratio Comparison (2022-2026)",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel(
    "Date",
    fontsize=12
)

plt.ylabel(
    "Sharpe Ratio",
    fontsize=12
)

plt.legend()

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

# --------------------------------------------------
# Save chart
# --------------------------------------------------

plt.savefig(
    "reports/rolling_sharpe_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nTask 3 Completed!")
print("rolling_sharpe_chart.png saved successfully!")
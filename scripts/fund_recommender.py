import pandas as pd
import os

# ----------------------------------------
# Create reports folder
# ----------------------------------------

os.makedirs("reports", exist_ok=True)

print("Loading datasets...")

# ----------------------------------------
# Load datasets
# ----------------------------------------

fund_master = pd.read_csv(
    "data/processed/cleaned_fund_master.csv"
)

sharpe_df = pd.read_csv(
    "data/processed/sharpe_ratios.csv"
)

# ----------------------------------------
# Merge datasets
# ----------------------------------------

funds = fund_master.merge(
    sharpe_df,
    on="amfi_code",
    how="inner"
)

print("\nDatasets merged successfully!")
print(f"Total Funds: {len(funds)}")

# ----------------------------------------
# User Input
# ----------------------------------------

risk = input(
    "\nEnter Risk Profile (Low / Moderate / High): "
).strip().lower()

# ----------------------------------------
# LOW RISK
# Lowest Volatility
# ----------------------------------------

if risk == "low":

    recommendations = funds.sort_values(
        by="annual_volatility",
        ascending=True
    ).head(3)

# ----------------------------------------
# MODERATE RISK
# Medium Volatility
# ----------------------------------------

elif risk == "moderate":

    funds_sorted = funds.sort_values(
        by="annual_volatility",
        ascending=True
    )

    middle = len(funds_sorted) // 2

    recommendations = funds_sorted.iloc[
        middle-1:middle+2
    ]

# ----------------------------------------
# HIGH RISK
# Highest Sharpe Ratio
# ----------------------------------------

elif risk == "high":

    recommendations = funds.sort_values(
        by="sharpe_ratio",
        ascending=False
    ).head(3)

# ----------------------------------------
# Invalid Input
# ----------------------------------------

else:

    print(
        "\nInvalid Risk Profile!"
    )

    exit()

# ----------------------------------------
# Display Results
# ----------------------------------------

print("\nTop 3 Recommended Funds:\n")

print(
    recommendations[
        [
            "scheme_name",
            "annual_return",
            "annual_volatility",
            "sharpe_ratio"
        ]
    ]
)

# ----------------------------------------
# Save Report
# ----------------------------------------

recommendations.to_csv(
    "reports/fund_recommendations.csv",
    index=False
)

print("\nTask 6 Completed!")
print(
    "fund_recommendations.csv saved successfully!"
)
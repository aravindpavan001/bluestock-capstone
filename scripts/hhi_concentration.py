import pandas as pd
import os

# --------------------------------------------------
# Create reports folder
# --------------------------------------------------

os.makedirs("reports", exist_ok=True)

print("Loading portfolio holdings data...")

# --------------------------------------------------
# Load portfolio holdings
# --------------------------------------------------

portfolio_df = pd.read_csv(
    "data/processed/cleaned_portfolio_holdings.csv"
)

print("Dataset Loaded!")
print(portfolio_df.head())

# --------------------------------------------------
# Check columns
# --------------------------------------------------

print("\nColumns:")
print(portfolio_df.columns)

# --------------------------------------------------
# Calculate HHI
# --------------------------------------------------

results = []

for fund in portfolio_df["amfi_code"].unique():

    temp = portfolio_df[
        portfolio_df["amfi_code"] == fund
    ].copy()

    # Convert percentage weight to decimal
    temp["weight_decimal"] = (
        temp["weight_pct"] / 100
    )

    # HHI = Sum(weight²)
    hhi = (
        temp["weight_decimal"] ** 2
    ).sum()

    results.append([
        fund,
        round(hhi, 4)
    ])

# --------------------------------------------------
# Create Results DataFrame
# --------------------------------------------------

hhi_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "hhi_index"
    ]
)

# --------------------------------------------------
# Diversification Label
# --------------------------------------------------

def classify_hhi(hhi):

    if hhi < 0.15:
        return "Highly Diversified"

    elif hhi < 0.25:
        return "Moderately Diversified"

    else:
        return "Highly Concentrated"

hhi_df["portfolio_type"] = (
    hhi_df["hhi_index"]
    .apply(classify_hhi)
)

# --------------------------------------------------
# Display Results
# --------------------------------------------------

print("\nFirst 10 Results:")
print(hhi_df.head(10))

# --------------------------------------------------
# Save Results
# --------------------------------------------------

hhi_df.to_csv(
    "reports/hhi_concentration_report.csv",
    index=False
)

print("\nTask 7 Completed!")
print(
    "hhi_concentration_report.csv saved successfully!"
)
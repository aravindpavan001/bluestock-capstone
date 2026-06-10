import pandas as pd
import os

# --------------------------------------------------
# Create reports folder if it doesn't exist
# --------------------------------------------------

os.makedirs("reports", exist_ok=True)

print("Loading datasets...")

# --------------------------------------------------
# Load investor transactions
# --------------------------------------------------

transactions = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

fund_master = pd.read_csv(
    "data/processed/cleaned_fund_master.csv"
)

# --------------------------------------------------
# Convert date column
# --------------------------------------------------

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# --------------------------------------------------
# First Investment Year (Cohort)
# --------------------------------------------------

first_investment = (
    transactions
    .groupby("investor_id")["transaction_date"]
    .min()
    .reset_index()
)

first_investment["first_year"] = (
    first_investment["transaction_date"]
    .dt.year
)

# --------------------------------------------------
# Merge cohort back
# --------------------------------------------------

transactions = transactions.merge(
    first_investment[
        ["investor_id", "first_year"]
    ],
    on="investor_id",
    how="left"
)

# --------------------------------------------------
# Favorite Fund
# --------------------------------------------------

favorite_fund = (
    transactions
    .groupby(
        ["first_year", "amfi_code"]
    )
    .size()
    .reset_index(name="transaction_count")
)

favorite_fund = favorite_fund.loc[
    favorite_fund.groupby("first_year")
    ["transaction_count"]
    .idxmax()
]

favorite_fund = favorite_fund.merge(
    fund_master[
        ["amfi_code", "scheme_name"]
    ],
    on="amfi_code",
    how="left"
)

# --------------------------------------------------
# Cohort Summary
# --------------------------------------------------

cohort_summary = (
    transactions
    .groupby("first_year")
    .agg(
        investors=("investor_id", "nunique"),
        average_sip=("amount_inr", "mean"),
        total_invested=("amount_inr", "sum")
    )
    .reset_index()
)

# --------------------------------------------------
# Add Favorite Fund
# --------------------------------------------------

cohort_summary = cohort_summary.merge(
    favorite_fund[
        ["first_year", "scheme_name"]
    ],
    on="first_year",
    how="left"
)

cohort_summary.rename(
    columns={
        "scheme_name": "favorite_fund"
    },
    inplace=True
)

# --------------------------------------------------
# Round values
# --------------------------------------------------

cohort_summary["average_sip"] = (
    cohort_summary["average_sip"]
    .round(2)
)

cohort_summary["total_invested"] = (
    cohort_summary["total_invested"]
    .round(2)
)

# --------------------------------------------------
# Display results
# --------------------------------------------------

print("\nInvestor Cohort Analysis:")
print(cohort_summary)

# --------------------------------------------------
# Save results
# --------------------------------------------------

cohort_summary.to_csv(
    "reports/investor_cohort_analysis.csv",
    index=False
)

print(
    "\nTask 4 Completed!"
)

print(
    "investor_cohort_analysis.csv saved successfully!"
)
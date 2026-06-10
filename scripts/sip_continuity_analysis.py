import pandas as pd
import os

# --------------------------------------------------
# Create reports folder
# --------------------------------------------------

os.makedirs("reports", exist_ok=True)

print("Loading datasets...")

# --------------------------------------------------
# Load transactions
# --------------------------------------------------

transactions = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

# --------------------------------------------------
# Convert date column
# --------------------------------------------------

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# --------------------------------------------------
# Keep only SIP transactions
# --------------------------------------------------

sip_df = transactions[
    transactions["transaction_type"] == "SIP"
].copy()

print(f"Total SIP Transactions: {len(sip_df)}")

# --------------------------------------------------
# Sort by investor and date
# --------------------------------------------------

sip_df = sip_df.sort_values(
    ["investor_id", "transaction_date"]
)

# --------------------------------------------------
# Calculate gap between SIPs
# --------------------------------------------------

sip_df["previous_date"] = sip_df.groupby(
    "investor_id"
)["transaction_date"].shift(1)

sip_df["gap_days"] = (
    sip_df["transaction_date"]
    - sip_df["previous_date"]
).dt.days

# --------------------------------------------------
# Count SIP transactions per investor
# --------------------------------------------------

sip_counts = (
    sip_df.groupby("investor_id")
    .size()
    .reset_index(name="sip_count")
)

# Keep investors with 6+ SIPs
eligible_investors = sip_counts[
    sip_counts["sip_count"] >= 6
]["investor_id"]

sip_df = sip_df[
    sip_df["investor_id"].isin(
        eligible_investors
    )
]

# --------------------------------------------------
# Flag risky investors
# --------------------------------------------------

sip_df["status"] = sip_df["gap_days"].apply(
    lambda x: "AT_RISK"
    if pd.notnull(x) and x > 35
    else "ACTIVE"
)

# --------------------------------------------------
# Investor Summary
# --------------------------------------------------

risk_summary = (
    sip_df.groupby("investor_id")
    .agg(
        sip_count=("investor_id", "count"),
        max_gap_days=("gap_days", "max")
    )
    .reset_index()
)

risk_summary["status"] = risk_summary[
    "max_gap_days"
].apply(
    lambda x: "AT_RISK"
    if pd.notnull(x) and x > 35
    else "ACTIVE"
)

# --------------------------------------------------
# Results
# --------------------------------------------------

print("\nFirst 10 Investors:")
print(risk_summary.head(10))

# --------------------------------------------------
# Save report
# --------------------------------------------------

risk_summary.to_csv(
    "reports/sip_continuity_analysis.csv",
    index=False
)

print("\nTask 5 Completed!")
print(
    "sip_continuity_analysis.csv saved successfully!"
)
print("\nSummary:")

print(
    risk_summary["status"]
    .value_counts()
)
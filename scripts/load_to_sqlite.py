from sqlalchemy import create_engine
import pandas as pd

print("Starting SQLite load process...")

# Create SQLite connection
engine = create_engine('sqlite:///bluestock_mf.db')

# Load cleaned NAV history
nav_df = pd.read_csv(
  'data/processed/nav_history_cleaned.csv')

nav_df.to_sql(
    'fact_nav_history',
    engine,
    if_exists='replace',
    index=False
)

print("NAV history loaded successfully!")

# Load investor transactions
txn_df = pd.read_csv(
    'data/processed/investor_transactions_cleaned.csv'
)

txn_df.to_sql(
    'fact_investor_transactions',
    engine,
    if_exists='replace',
    index=False
)

print("Investor transactions loaded successfully!")

# Load scheme performance
perf_df = pd.read_csv(
    'data/processed/scheme_performance_cleaned.csv'
)

perf_df.to_sql(
    'fact_scheme_performance',
    engine,
    if_exists='replace',
    index=False
)

print("Scheme performance loaded successfully!")

print("\nAll datasets loaded into SQLite database!")
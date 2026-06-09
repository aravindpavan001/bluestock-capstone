import pandas as pd

print("Loading NAV data...")

df = pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
)

df['date'] = pd.to_datetime(df['date'])

results = []

for amfi_code, group in df.groupby('amfi_code'):

    group = group.sort_values('date')

    # Running maximum NAV
    running_max = group['nav'].cummax()

    # Drawdown
    drawdown = (
        group['nav'] / running_max
    ) - 1

    # Worst drawdown
    max_drawdown = drawdown.min()

    results.append([
        amfi_code,
        round(max_drawdown * 100, 2)
    ])

mdd_df = pd.DataFrame(
    results,
    columns=[
        'amfi_code',
        'max_drawdown_pct'
    ]
)

print("\nFirst 5 Results:")
print(mdd_df.head())

mdd_df.to_csv(
    "data/processed/max_drawdown_results.csv",
    index=False
)

print("\nMaximum Drawdown calculation completed!")
print("max_drawdown_results.csv saved successfully!")
import pandas as pd

print("Loading NAV data...")

df = pd.read_csv("data/processed/cleaned_nav_history.csv")

df['date'] = pd.to_datetime(df['date'])

results = []

for amfi_code, group in df.groupby('amfi_code'):

    group = group.sort_values('date')

    start_nav = group['nav'].iloc[0]
    end_nav = group['nav'].iloc[-1]

    years = (
        (group['date'].iloc[-1] - group['date'].iloc[0]).days
        / 365.25
    )

    cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

    results.append([
        amfi_code,
        round(start_nav, 2),
        round(end_nav, 2),
        round(years, 2),
        round(cagr, 2)
    ])

cagr_df = pd.DataFrame(
    results,
    columns=[
        'amfi_code',
        'start_nav',
        'end_nav',
        'years',
        'cagr_pct'
    ]
)

print(cagr_df.head())

cagr_df.to_csv(
    "data/processed/cagr_results.csv",
    index=False
)

print("\nCAGR calculation completed!")
print("cagr_results.csv saved successfully!")
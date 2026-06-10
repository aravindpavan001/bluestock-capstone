import pandas as pd
import matplotlib.pyplot as plt

print("Loading datasets...")

returns_df = pd.read_csv(
    "data/processed/returns_computed.csv"
)

fund_master = pd.read_csv(
    "data/processed/cleaned_fund_master.csv"
)

returns_df['date'] = pd.to_datetime(
    returns_df['date']
)

target_funds = [
    "SBI Bluechip Fund - Regular Plan - Growth",
    "HDFC Top 100 Fund - Regular Plan - Growth",
    "ICICI Pru Bluechip Fund - Direct - Growth",
    "Axis Bluechip Fund - Regular Plan - Growth",
    "Nippon India Large Cap Fund - Growth Plan"
]

selected = fund_master[
    fund_master['scheme_name'].isin(target_funds)
]

plt.figure(figsize=(12,6))

for _, row in selected.iterrows():

    amfi = row['amfi_code']
    name = row['scheme_name']

    temp = returns_df[
        returns_df['amfi_code'] == amfi
    ].copy()

    temp = temp.sort_values('date')

    temp['rolling_sharpe'] = (
        temp['daily_return']
        .rolling(90)
        .mean()
        /
        temp['daily_return']
        .rolling(90)
        .std()
    ) * (252 ** 0.5)

    plt.plot(
        temp['date'],
        temp['rolling_sharpe'],
        label=name[:20]
    )

plt.title(
    "Rolling 90-Day Sharpe Ratio"
)

plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")

plt.legend()

plt.grid(True)

plt.savefig(
    "reports/charts/rolling_sharpe_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(
    "rolling_sharpe_chart.png saved successfully!"
)
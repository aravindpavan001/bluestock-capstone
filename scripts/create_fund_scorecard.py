import pandas as pd

print("Loading datasets...")

# Load files
cagr = pd.read_csv(
    "data/processed/cagr_results.csv"
)

sharpe = pd.read_csv(
    "data/processed/sharpe_ratios.csv"
)

alpha_beta = pd.read_csv(
    "data/processed/alpha_beta_results.csv"
)

drawdown = pd.read_csv(
    "data/processed/max_drawdown_results.csv"
)

scheme = pd.read_csv(
    "data/processed/cleaned_scheme_performance.csv"
)

# Merge all datasets
scorecard = (
    cagr
    .merge(sharpe[['amfi_code', 'sharpe_ratio']], on='amfi_code')
    .merge(alpha_beta[['amfi_code', 'alpha']], on='amfi_code')
    .merge(drawdown[['amfi_code', 'max_drawdown_pct']], on='amfi_code')
    .merge(
        scheme[
            ['amfi_code',
             'scheme_name',
             'expense_ratio_pct']
        ],
        on='amfi_code'
    )
)

# Ranking

scorecard['return_rank'] = (
    scorecard['cagr_pct']
    .rank(ascending=False)
)

scorecard['sharpe_rank'] = (
    scorecard['sharpe_ratio']
    .rank(ascending=False)
)

scorecard['alpha_rank'] = (
    scorecard['alpha']
    .rank(ascending=False)
)

scorecard['expense_rank'] = (
    scorecard['expense_ratio_pct']
    .rank(ascending=True)
)

scorecard['drawdown_rank'] = (
    scorecard['max_drawdown_pct']
    .rank(ascending=False)
)

# Final weighted score

scorecard['score'] = (
      scorecard['return_rank'] * 0.30
    + scorecard['sharpe_rank'] * 0.25
    + scorecard['alpha_rank'] * 0.20
    + scorecard['expense_rank'] * 0.15
    + scorecard['drawdown_rank'] * 0.10
)

# Convert to 100-point style

scorecard['final_score'] = (
    100
    - (
        scorecard['score']
        / scorecard['score'].max()
        * 100
      )
)

scorecard = scorecard.sort_values(
    'final_score',
    ascending=False
)

print("\nTop 10 Funds:")
print(
    scorecard[
        ['scheme_name',
         'final_score']
    ].head(10)
)

scorecard.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print("\nFund scorecard created successfully!")
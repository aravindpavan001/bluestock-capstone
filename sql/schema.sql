CREATE TABLE dim_fund (
fund_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
fund_name TEXT,
category TEXT
);

CREATE TABLE fact_nav_history (
nav_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
date DATE,
nav REAL
);

CREATE TABLE fact_investor_transactions (
transaction_id INTEGER PRIMARY KEY,
investor_id INTEGER,
amfi_code INTEGER,
transaction_date DATE,
transaction_type TEXT,
amount_inr REAL,
city TEXT,
state TEXT,
kyc_status TEXT
);

CREATE TABLE fact_scheme_performance (
performance_id INTEGER PRIMARY KEY,
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
expense_ratio_pct REAL,
sharpe_ratio REAL,
risk_grade TEXT
);

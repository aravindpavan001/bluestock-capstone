-- View NAV history sample
SELECT *
FROM fact_nav_history
LIMIT 5;

-- View investor transactions sample
SELECT *
FROM fact_investor_transactions
LIMIT 5;

-- View scheme performance sample
SELECT *
FROM fact_scheme_performance
LIMIT 5;

-- Count NAV records
SELECT COUNT(*) AS total_nav_records
FROM fact_nav_history;

-- Count transaction records
SELECT COUNT(*) AS total_transactions
FROM fact_investor_transactions;

-- Average NAV per month
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav_history
GROUP BY month
ORDER BY month;

-- Total investment amount by transaction type
SELECT
transaction_type,
SUM(amount_inr) AS total_amount
FROM fact_investor_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;

-- Average 1-year return by risk grade
SELECT
risk_grade,
AVG(return_1yr_pct) AS avg_return
FROM fact_scheme_performance
GROUP BY risk_grade
ORDER BY avg_return DESC;

-- Top schemes by 1-year return
SELECT
scheme_name,
return_1yr_pct
FROM fact_scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Average expense ratio by category
SELECT
category,
AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_scheme_performance
GROUP BY category
ORDER BY avg_expense_ratio DESC;

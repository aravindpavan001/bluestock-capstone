-- 1. Top 5 funds by AUM
SELECT
scheme_name,
aum_crore
FROM fact_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav_history
GROUP BY month
ORDER BY month;

-- 3. Transaction count by state
SELECT
state,
COUNT(*) AS transaction_count
FROM fact_investor_transactions
GROUP BY state
ORDER BY transaction_count DESC;

-- 4. Total investment amount by transaction type
SELECT
transaction_type,
SUM(amount_inr) AS total_amount
FROM fact_investor_transactions
GROUP BY transaction_type;

-- 5. Funds with expense ratio below 1%
SELECT
scheme_name,
expense_ratio_pct
FROM fact_scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Average return by risk grade
SELECT
risk_grade,
AVG(return_1yr_pct) AS avg_return
FROM fact_scheme_performance
GROUP BY risk_grade;

-- 7. Top 5 schemes by 1-year return
SELECT
scheme_name,
return_1yr_pct
FROM fact_scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 8. Average investment amount by city tier
SELECT
city_tier,
AVG(amount_inr) AS avg_amount
FROM fact_investor_transactions
GROUP BY city_tier;

-- 9. Count of investors by gender
SELECT
gender,
COUNT(*) AS investor_count
FROM fact_investor_transactions
GROUP BY gender;

-- 10. Average expense ratio by category
SELECT
category,
AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_scheme_performance
GROUP BY category;

 Bluestock Mutual Fund Capstone

  Project Overview

This project analyses Indian Mutual Fund data using Python, SQL, and Power BI.

The objective is to perform data cleaning, risk analysis, investor behaviour analysis, portfolio analytics, and dashboard reporting to generate actionable insights for investors and fund managers.

---

  Project Structure

bluestock_capstone/

├── data/

│ ├── raw/

│ └── processed/

├── scripts/

├── notebooks/

├── sql/

├── dashboard/

├── reports/

├── README.md

└── requirements.txt

---

  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- Power BI
- Git
- GitHub

---

 Datasets Used

The project uses multiple mutual fund datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

 ETL Process

 Data Ingestion

Raw CSV files are loaded from:

data/raw/

   Data Cleaning

Cleaning scripts standardise:

- Missing values
- Data types
- Duplicate records
- Column naming conventions

Cleaned datasets are stored in:

data/processed/

    Database Loading

Processed datasets are loaded into SQLite for structured analysis.

---

   Analytics Performed

    Risk Analytics

- CAGR
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Tracking Error
- Value at Risk (VaR)
- Rolling Sharpe Ratio

    Investor Analytics

- Investor Cohort Analysis
- SIP Continuity Analysis

    Portfolio Analytics

- HHI Concentration Analysis
- Fund Recommendation Engine
- Fund Scorecard Generation

---

   Setup Instructions

    Clone Repository

```bash
git clone https://github.com/aravindpavan001/bluestock-capstone.git
cd bluestock-capstone
```

    Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

    Install Dependencies

```bash
pip install -r requirements.txt
```

---

   How to Run the ETL

Run the data ingestion process:

```bash
python scripts/data_ingestion.py
```

Run data cleaning scripts:

```bash
python scripts/data_cleaning.py
```

Run the complete analytics pipeline:

```bash
python scripts/run_pipeline.py
```

Processed datasets will be generated inside:

```text
data/processed/
```

---

   How to Open the Dashboard

Open the Power BI dashboard file:

```text
dashboard/bluestock_mf_dashboard.pbix
```

Requirements:

- Microsoft Power BI Desktop installed
- All processed datasets available in data/processed/

Steps:

1. Open Power BI Desktop.
2. Open the .pbix file from the dashboard folder.
3. Refresh data if required.
4. Explore the report pages and interactive visuals.


   Running the Pipeline

Execute:

python scripts/run_pipeline.py

This automatically runs:-
- VaR Analysis
- Rolling Sharpe Analysis
- Investor Cohort Analysis
- SIP Continuity Analysis
- HHI Concentration Analysis
= Fund Recommendation Engine

---

   Dashboard

The Power BI dashboard contains:

   Industry Overview

- Total AUM
- SIP Trends
- Category Analysis

   Fund Performance

- CAGR Analysis
- Risk Metrics
- Fund Comparison

    Investor Analytics

- Cohort Analysis
- SIP Continuity

    SIP & Market Trends

- SIP Inflows vs NIFTY50
- Category Heatmap
- Top Categories by Inflows

   Fund NAV Detail

  Drill-through NAV Analysis

---

   Outputs Generated

The project generates:

- Cleaned datasets
- Risk analytics reports
- Portfolio concentration reports
- Investor behaviour reports
- Recommendation outputs
- Dashboard visualisations

---

   Author

Repalle Aravind Pavan Kumar

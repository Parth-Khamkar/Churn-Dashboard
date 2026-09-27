# Customer Churn Analytics Dashboard

An end-to-end churn analysis project built on the IBM Telco Customer Churn dataset (7,043 customers), using Python for cleaning and exploration, SQL for segment analysis, and Tableau for an interactive dashboard.


## 📊 Overview

This dashboard identifies which customer segments are most likely to churn and quantifies the revenue at risk, so a retention team could prioritize where to act first.

**Key findings from this dashboard:**
- **Overall churn rate: 26.54%**
- **Monthly revenue at risk: $139,131**
- Month-to-month contract customers churn at **42.71%**, compared to just **11.27%** for one-year contracts and **2.83%** for two-year contracts — a ~15x difference between the highest and lowest risk contract types
- Churn is heavily concentrated in new customers: the **0–12 month** tenure group churns at **47.68%**, dropping steadily to just **6.61%** for customers with 60+ months of tenure

## 🖼️ Dashboard Preview

![Churn Dashboard](./Screenshot/churn-dashboard-overview.png)

*(Rename your screenshot in the `Screenshots` folder to match the filename above, or edit this path to match your actual filename.)*

## 🛠️ Tech Stack

- **Python (Pandas)** — data cleaning, exploratory analysis, and chart generation
- **SQL (SQLite)** — segment-level aggregation queries (churn rate by contract, revenue at risk by service type)
- **Tableau Public** — interactive dashboard with KPI tiles, bar charts, and a distribution histogram

## 📁 Project Workflow

1. **Data Cleaning (Python)** — fixed the `TotalCharges` column (blank strings → numeric), created a binary `ChurnFlag`, and bucketed customers into `TenureGroup` ranges
2. **Exploratory Analysis (Python)** — generated initial churn-rate breakdowns by contract type and tenure to identify key drivers
3. **Load to SQL (`load_sql.py`)** — loaded the cleaned dataset into a SQLite database (`churn.db`)
4. **SQL Analysis** — wrote queries to quantify churn rate and revenue at risk by segment (contract type, payment method, internet service)
5. **Tableau Dashboard Build** — created two calculated fields (`Churn Rate`, `Revenue at Risk`), built two KPI tiles, two bar charts, and a monthly-charges distribution histogram, then assembled them into one filterable dashboard

## 📈 Dashboard Components

| Visual | What it shows |
|---|---|
| **Overall KPI – Churn Rate** | Single-number tile: 26.54% of customers have churned |
| **Monthly Revenue at Risk** | Single-number tile: $139,131 in monthly revenue tied to churned customers |
| **Churn by Contract** | Bar chart comparing churn rate across Month-to-month, One year, and Two year contracts |
| **Churn Rate by Tenure Group** | Bar chart showing churn rate declining as customer tenure increases |
| **Monthly Charges Distribution** | Histogram comparing spending patterns of churned vs. retained customers |

## 📂 Files in This Repo

| File | Description |
|---|---|
| `telco_churn.csv` | Raw source dataset |
| `telco_churn_clean.csv` | Cleaned dataset with ChurnFlag and TenureGroup columns |
| `clean.py` | Python script for data cleaning |
| `analyze.py` | Python script for exploratory analysis and charts |
| `load_sql.py` | Python script to load cleaned data into SQLite |
| `churn.db` | SQLite database used for SQL analysis |
| `churn-dashboard.twbx` | Full interactive Tableau workbook |
| `Screenshots/` | PNG screenshots of the dashboard |

## ▶️ How to Use

- **View instantly:** [open the live dashboard on Tableau Public](#) *(replace with your published link)*
- **Explore interactively:** download `churn-dashboard.twbx` and open it in [Tableau Public](https://public.tableau.com/) (free) or Tableau Desktop
- **Check the SQL logic:** open `churn.db` in [DB Browser for SQLite](https://sqlitebrowser.org/) (free) to run the segment queries yourself

## 👤 Author

**Parth Dadasaheb Khamkar**
[LinkedIn](https://linkedin.com/in/parth-khamkar-704144241) · parth.d.khamkar2970@gmail.com

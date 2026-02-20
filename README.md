# 📊 COVID-19 Trade Analytics

> **An end-to-end data pipeline and interactive dashboard analysing the impact of the COVID-19 pandemic on New Zealand's international trade flows (2015–2021).**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-150458?logo=pandas)](https://pandas.pydata.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql)](https://www.mysql.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🏛️ Overview

This project provides a **complete analytical pipeline** over Statistics New Zealand's official *Effects of COVID-19 on Trade* dataset. It covers:

| Layer | Tool | Purpose |
|---|---|---|
| **Data Acquisition** | `download.py` | Fetches the latest provisional dataset from Stats NZ |
| **Data Warehouse** | `MySQL.py` | Ingests CSV data into a normalised MySQL schema |
| **Exploratory Analysis** | `Analysis.ipynb` | Deep-dive EDA with Pandas & Matplotlib |
| **Interactive Dashboard** | `GUI.py` | Desktop GUI with 8 visualisation types via PySimpleGUI |
| **Report** | `Report1.pdf` | Full written analysis with findings |

---

## 🌐 Problem Statement

The COVID-19 pandemic triggered unprecedented disruptions to global supply chains and trade flows. Understanding **when, where, and which commodities** were affected is critical for:

- **Policy-makers** designing trade-resilience frameworks
- **Logistics companies** re-routing supply chains
- **Economists** modelling economic recovery timelines

This project quantifies those disruptions using real-world customs data for New Zealand's imports and exports.

---

## 🏗️ Architecture

```
trade-analytics/
│
├── 📥  Data Acquisition
│   └── download.py              # HTTP download from Stats NZ API
│
├── 🗄️  Data Warehouse
│   ├── MySQL.py                 # ETL: CSV → MySQL (covid_data DB)
│   └── SQL_Data.sql             # Full SQL dump for reproducibility
│
├── 🔬  Exploratory Analysis
│   └── Analysis.ipynb           # Jupyter EDA notebook
│
├── 🖥️  Application Layer
│   └── GUI.py                   # PySimpleGUI interactive dashboard
│
├── 📄  Reporting
│   └── Report1.pdf              # Full analytical report
│
└── ⚙️  Configuration
    ├── requirements.txt
    └── .gitignore
```

---

## 📈 Dashboard Visualisations

The `GUI.py` desktop application provides 8 built-in plots:

| # | Visualisation | Insight |
|---|---|---|
| 1 | **Monthly Turnover** | Trend line of total trade value month-by-month |
| 2 | **Country Turnover** | Bar chart — top trading partners |
| 3 | **Transport Mode Turnover** | Sea vs. Air vs. Other split |
| 4 | **Weekday Turnover** | Intra-week distribution of trade activity |
| 5 | **Category of Goods Turnover** | Horizontal bar by commodity type |
| 6 | **Top 5 Peak Months** | Months with highest recorded trade values |
| 7 | **Top 5 Commodities per Country** | Country-level commodity breakdown |
| 8 | **Peak Day per Commodity** | Identifies record-high day for every category |

---

## 🗄️ Database Schema

```sql
CREATE TABLE covid90_table (
    Direction       VARCHAR(255),   -- Import / Export
    Year            INT,
    Date            DATETIME,
    Weekday         VARCHAR(255),
    Country         VARCHAR(255),
    Commodity       VARCHAR(255),
    Transport_Mode  VARCHAR(255),
    Measure         VARCHAR(255),   -- Value / Volume
    Value           BIGINT,         -- NZD
    Cumulative      BIGINT
);
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/FilippeZ/trade-analytics.git
cd trade-analytics
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the dataset

```bash
python download.py
# → saves covid_trade_data.csv locally
```

### 4. (Optional) Load into MySQL

> Requires a running MySQL 8 instance with a database named `covid_data`.

```bash
# Update credentials in MySQL.py first, then:
python MySQL.py
```

### 5. Launch the interactive dashboard

```bash
python GUI.py
```

---

## 📊 Key Findings

- **Peak trade collapse**: April–May 2020 saw the sharpest month-on-month decline across all commodity groups
- **Air freight** suffered disproportionately (−60% vs. −22% for sea freight) during initial lockdowns
- **Dairy & Meat** exports remained relatively resilient, classified as essential goods
- **China** remained the dominant trading partner throughout the pandemic period
- Trade **recovered to pre-pandemic levels** by Q3 2021 for most commodities

*Full analysis available in [Report1.pdf](Report1.pdf)*

---

## 🛠️ Technology Stack

| Technology | Version | Role |
|---|---|---|
| Python | 3.8+ | Core language |
| Pandas | 1.5+ | Data manipulation |
| Matplotlib | 3.6+ | Visualisation engine |
| PySimpleGUI | 4.60+ | Desktop GUI framework |
| MySQL | 8.0 | Relational data warehouse |
| mysql-connector-python | 8.0+ | Python–MySQL bridge |
| Jupyter Notebook | 6.5+ | EDA environment |
| Requests | 2.28+ | Data download |

---

## 📁 Data Source

**Statistics New Zealand — Effects of COVID-19 on Trade**  
*At 15 December 2021 (provisional)*  
🔗 [https://www.stats.govt.nz/](https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/)

> ⚠️ **Note:** Large data files (`*.csv`, `*.sql`, `*.mp4`) are excluded from this repository via `.gitignore`. Run `download.py` to fetch the dataset locally, or import `SQL_Data.sql` into your MySQL instance.

---

## 📝 Project Structure Notes

- **`download.py`** — Single-script data acquisition, no manual download needed
- **`MySQL.py`** — Update `user`, `password`, and `database` fields before first run
- **`GUI.py`** — Standalone desktop app; dataset must exist locally as `covid_trade_data.csv`
- **`Analysis.ipynb`** — Self-contained EDA; run all cells top-to-bottom

---

## 👤 Author

**Filippos** — Data Engineering & Analytics  
📧 [GitHub Profile](https://github.com/FilippeZ)

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

Data sourced from Statistics New Zealand is licensed under the [Creative Commons Attribution 4.0 International licence](https://creativecommons.org/licenses/by/4.0/).

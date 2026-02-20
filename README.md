# 🌍 Trade Analytics — Global Supply Chain & COVID-19 Impact

> **An end-to-end data engineering pipeline analyzing the unprecedented impact of COVID-19 on New Zealand's international trade flows (2015–2021).**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-150458?logo=pandas)](https://pandas.pydata.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql)](https://www.mysql.com/)

---

## 📋 Overview
**Trade Analytics** is a comprehensive analytical framework designed to quantify supply chain disruptions during crisis events. Built using **Statistics New Zealand's** official *Effects of COVID-19 on Trade* dataset, this ecosystem features automated data ingestion, relational warehousing in MySQL, deep-dive exploratory data analysis (EDA), and a responsive desktop application for interactive decision-making.

## 🎯 The Problem
The COVID-19 pandemic caused severe bottlenecks in global logistics, leading to:
* **Critical Supply Shortages:** Unpredictable availability of essential commodities like food and medical supplies.
* **Logistical Paralysis:** Disproportionate collapse of air freight routes compared to maritime shipping.
* **Economic Uncertainty:** Without clear visualization of macro-trends, policymakers and business leaders lack the insight needed for robust recovery planning.

## ✅ The Solution
This platform transforms millions of raw customs records into actionable business intelligence using a structured data pipeline:

| Feature | Technology | Business Value |
| :--- | :--- | :--- |
| **Data Automation** | `requests` API | Hands-free data acquisition of the latest provisional records |
| **Data Warehousing** | MySQL | Robust, query-optimized storage of massive temporal datasets |
| **Interactive BI** | PySimpleGUI | 8 dynamic dashboards for instant stakeholder insights |

---

## 🏗️ Architecture & Workflow
The system follows a classic Extract, Transform, Load (ETL) and Reporting architecture:

1. **Extraction Layer:** Automated retrieval of remote CSV troves (`download.py`).
2. **Persistence Layer:** Schema definition and bulk insertion into a relational database (`MySQL.py`).
3. **Exploration Layer:** In-depth statistical analysis and trend identification (`Analysis.ipynb`).
4. **Presentation Layer:** End-user graphical interface for exploring turnover by country, mode, and commodity (`GUI.py`).

## 📂 Project Structure
```text
trade-analytics/
├── GUI.py                # 🖥️ Main Interactive Dashboard
├── MySQL.py              # 🗄️ ETL pipeline to MySQL Data Warehouse
├── download.py           # 📥 Automated Data Acquisition
├── Analysis.ipynb        # 🔬 Exploratory Data Analysis
├── requirements.txt      # ⚙️ Python dependencies
├── Report1.pdf           # 📄 Comprehensive Analytical Report
└── .gitignore            # 🚫 Excludes large data artifacts
```

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/FilippeZ/trade-analytics.git
cd trade-analytics
pip install -r requirements.txt
```

### 2. Data Acquisition
```bash
python download.py
```

### 3. Launching the Interface
```bash
python GUI.py
```

*(Optional) To populate the MySQL warehouse, ensure a local MySQL instance is running with a `covid_data` schema, update credentials in `MySQL.py`, and run it.*

---

## 📊 Business Intelligence Insights

By analyzing 2015-2021 data, our models revealed several non-intuitive market behaviors:

### 📈 Resilience and Explosive Rebound
Despite initial lockdowns, global trade demonstrated a remarkable "V-shaped" recovery. The top five months for absolute turnover across the entire decade all occurred during the pandemic's later stages in **2021** (November, July, October, June, and May). 

### 🚢 The Dominance of Sea Freight
While passenger aviation collapsed, cargo logistics rapidly pivoted. **Sea transport** proved highly resilient, absorbing the shock and moving an overwhelmingly larger share of trade volume compared to air transport, ensuring supply chain continuity.

### 🏭 Commodity Winners
Not all sectors suffered equally. Essential and primary industrial categories, specifically **"Non-food manufactured goods"** and **"Milk powder, butter, and cheese"**, emerged as the highest-performing segments, shielding the export economy from broader macro-economic shocks.

### ⏱️ Temporal Trade Rhythms
The data proves logistics is highly bound to standard behavioral weeks: trade activity peaks sharply on **Mondays** as backlogs from the weekend are cleared, followed by a severe drop-off on Saturdays and Sundays.

---

## 🛠️ Tech Stack
* **Language:** Python 3.8+
* **Data Engineering:** Pandas, MySQL Connector
* **Data Visualization:** Matplotlib
* **User Interface:** PySimpleGUI
* **Database:** MySQL 8.0

## 📄 License
Licensed under the MIT License — see `LICENSE` for details. Data sourced from Statistics New Zealand (CC BY 4.0).

## 👤 Author
**Filippos-Paraskevas Zygouris**  
[GitHub](https://github.com/FilippeZ)

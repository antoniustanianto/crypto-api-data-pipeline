# Crypto API Data Pipeline

A simple **Data Engineering project** that builds an automated ETL pipeline to collect cryptocurrency price data from the CoinGecko API and store it in a DuckDB database for analysis.

The pipeline demonstrates core data engineering concepts such as **API ingestion, data transformation, database loading, and scheduled data collection**.

---

# Project Overview

This project simulates a real-world **data ingestion pipeline** where data is collected from an external API, processed, and stored for analytics.

Each time the pipeline runs, it fetches the latest cryptocurrency prices and appends them to the database, creating a **historical dataset for time-series analysis**.

---

# Pipeline Architecture

```
CoinGecko API
      │
      ▼
Extract (Python - requests)
      │
      ▼
Transform (Pandas)
      │
      ▼
Load (DuckDB)
      │
      ▼
Historical Price Storage
      │
      ▼
SQL Analytics
```

---

# Tech Stack

**Languages & Tools**

- Python
- Pandas
- DuckDB
- SQL

**Data Source**

- CoinGecko Public API

---

# Project Structure

```
crypto-api-data-pipeline
│
├── extract.py        # Extract data from API
├── transform.py      # Transform JSON to structured dataframe
├── load.py           # Load data into DuckDB
├── pipeline.py       # Orchestrates the ETL pipeline
├── scheduler.py      # Runs pipeline automatically on a schedule
│
├── query_data.py     # Example script to query database
├── analysis.sql      # SQL analysis queries
│
├── requirements.txt
└── README.md
```

---

# ETL Pipeline Steps

### 1️⃣ Extract

The pipeline retrieves cryptocurrency prices from the **CoinGecko API**.

Example API response:

```
{
  "bitcoin": {"usd": 71215},
  "ethereum": {"usd": 2088},
  "solana": {"usd": 89}
}
```

---

### 2️⃣ Transform

The raw JSON response is transformed into a structured dataframe.

Schema:

| column | description |
|------|-------------|
| timestamp | time of data ingestion |
| coin | cryptocurrency name |
| price_usd | price in USD |

---

### 3️⃣ Load

The processed data is stored in a **DuckDB database**.

Table name:

```
crypto_prices
```

Schema:

```
timestamp TIMESTAMP
coin TEXT
price_usd DOUBLE
```

Each pipeline execution **appends new records**, creating a historical dataset.

---

# Running the Pipeline

Run the ETL pipeline manually:

```
python pipeline.py
```

This will:

1. Fetch latest cryptocurrency prices
2. Transform the data
3. Store it in DuckDB

---

# Automated Pipeline Scheduling

The project also includes a scheduler to automatically run the pipeline.

Run:

```
python scheduler.py
```

This simulates a **scheduled data pipeline** similar to workflows managed by tools like **Apache Airflow or Prefect**.

---

# Example SQL Analysis

### View latest data

```sql
SELECT *
FROM crypto_prices
ORDER BY timestamp DESC;
```

### Average price per cryptocurrency

```sql
SELECT
    coin,
    AVG(price_usd) AS avg_price
FROM crypto_prices
GROUP BY coin;
```

### Price statistics

```sql
SELECT
    coin,
    MIN(price_usd) AS min_price,
    MAX(price_usd) AS max_price,
    AVG(price_usd) AS avg_price
FROM crypto_prices
GROUP BY coin;
```

---

# Key Data Engineering Concepts Demonstrated

- API data ingestion
- ETL pipeline design
- modular Python pipeline architecture
- automated data pipelines
- time-series data storage
- SQL-based analysis

---

# Future Improvements

Potential improvements for this project:

- pipeline orchestration with **Apache Airflow**
- logging and monitoring
- data warehouse modeling (star schema)
- dashboard visualization
- containerization with Docker

---

# Author

Antonius Oktavian Tanianto  
Aspiring Data Engineer

# Crypto API Data Pipeline

This project demonstrates a simple **Data Engineering pipeline** that extracts cryptocurrency price data from the CoinGecko API, transforms the data using Python, and loads it into a DuckDB database for analysis.

The pipeline stores **historical cryptocurrency prices**, enabling time-series analysis and price trend exploration.

---

## Pipeline Architecture

CoinGecko API  
↓  
Extract (Python - requests)  
↓  
Transform (Pandas)  
↓  
Load (DuckDB)  
↓  
Historical Data Storage  
↓  
SQL Analysis  

---

## Tech Stack

- Python
- Pandas
- DuckDB
- SQL
- CoinGecko API

---

## Project Structure

```
crypto-api-data-pipeline
│
├── extract.py
├── transform.py
├── load.py
├── pipeline.py
├── scheduler.py
│
├── query_data.py
├── analysis.sql
│
├── requirements.txt
└── README.md
```

---

## Data Pipeline Steps

### 1. Extract

The pipeline retrieves cryptocurrency prices from the **CoinGecko API** using Python.

Example API response:

```
{
  "bitcoin": {"usd": 71215},
  "ethereum": {"usd": 2088},
  "solana": {"usd": 89}
}
```

---

### 2. Transform

The JSON response is transformed into a structured dataframe.

Schema:

| column | description |
|------|-------------|
| timestamp | time of data ingestion |
| coin | cryptocurrency name |
| price_usd | price in USD |

This step converts the raw API response into an analytics-friendly dataset.

---

### 3. Load

The transformed data is stored in a **DuckDB database**.

Table:

```
crypto_prices
```

Schema:

```
timestamp TIMESTAMP
coin TEXT
price_usd DOUBLE
```

Each pipeline execution **appends new rows**, creating a historical dataset.

---

## Example SQL Analysis

### View latest price data

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

## Running the Pipeline

Run the ETL pipeline:

```
python pipeline.py
```

Each execution fetches new cryptocurrency prices and stores them in the database.

---

## Automated Pipeline Scheduling

The pipeline can be scheduled to run periodically using the scheduler script.

Run:

```
python scheduler.py
```

This will execute the pipeline automatically at defined intervals.

---

## Key Learning Outcomes

This project demonstrates several core **Data Engineering concepts**:

- API data ingestion
- ETL pipeline design
- modular Python pipeline architecture
- database loading
- time-series data storage
- SQL-based analytics

---

## Possible Improvements

Future improvements could include:

- pipeline orchestration using Airflow or Prefect
- data warehouse modeling
- monitoring and logging
- visualization dashboard

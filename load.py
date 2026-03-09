import duckdb

def load_data(df):

    con = duckdb.connect("crypto.db")

    con.execute("""
    CREATE TABLE IF NOT EXISTS crypto_prices (
        timestamp TIMESTAMP,
        coin TEXT,
        price_usd DOUBLE
    )
    """)

    con.register("df", df)

    con.execute("""
    INSERT INTO crypto_prices
    SELECT * FROM df
    """)

    print("Data successfully loaded into DuckDB")


if __name__ == "__main__":

    import pandas as pd
    from datetime import datetime

    data = {
        "timestamp": [datetime.now(), datetime.now()],
        "coin": ["bitcoin", "ethereum"],
        "price_usd": [70000, 2000]
    }

    df = pd.DataFrame(data)

    load_data(df)
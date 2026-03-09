import duckdb

con = duckdb.connect("crypto.db")

df = con.execute("""
SELECT *
FROM crypto_prices
ORDER BY timestamp DESC
""").fetchdf()

print(df)
-- View all data
SELECT *
FROM crypto_prices
ORDER BY timestamp DESC;


-- Average price per coin
SELECT
    coin,
    AVG(price_usd) AS avg_price
FROM crypto_prices
GROUP BY coin;


-- Latest price
SELECT
    coin,
    price_usd,
    timestamp
FROM crypto_prices
ORDER BY timestamp DESC;


-- Price histoty
SELECT
    timestamp,
    coin,
    price_usd
FROM crypto_prices
ORDER BY timestamp DESC;


-- Price trend per coin
SELECT
    coin,
    MIN(price_usd) AS min_price,
    MAX(price_usd) AS max_price,
    AVG(price_usd) AS avg_price
FROM crypto_prices
GROUP BY coin;
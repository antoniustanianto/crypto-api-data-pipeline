import pandas as pd
from datetime import datetime

def transform_data(data):

    rows = []

    for coin, value in data.items():
        rows.append({
            "timestamp": datetime.now(),
            "coin": coin,
            "price_usd": value["usd"]
        })

    df = pd.DataFrame(rows)

    return df


if __name__ == "__main__":

    sample_data = {
        'bitcoin': {'usd': 71215},
        'ethereum': {'usd': 2088.12},
        'solana': {'usd': 89.09}
    }

    df = transform_data(sample_data)

    print(df)
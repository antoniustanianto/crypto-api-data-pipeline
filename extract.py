import requests

def extract_data():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data


if __name__ == "__main__":
    print(extract_data())
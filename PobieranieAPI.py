import csv
import requests
from datetime import datetime, timezone

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
ACTUAL_PRICES_FILE = "Wyniki1.csv"

def get_historical_prices():
    """ Pobiera historyczne kursy Bitcoina z API CoinGecko i zapisuje je do pliku Wyniki1.csv. """
    params = {"vs_currency": "usd", "days": "30"}
    response = requests.get(COINGECKO_API_URL, params=params)





    if response.status_code != 200:
        print(f"Błąd pobierania danych: {response.status_code}")
        return []

    data = response.json()


    if "prices" not in data or not data["prices"]:
        print("Błąd: Brak danych w API!")
        return []

    historical_prices = [
        [datetime.fromtimestamp(entry[0] / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S"), entry[1]]
        for entry in data["prices"]
    ]

    save_to_csv(historical_prices, ACTUAL_PRICES_FILE)
    print(f"Zapisano {len(historical_prices)} rekordów do {ACTUAL_PRICES_FILE}")
    return historical_prices

def save_to_csv(data, filename):
    """ Zapisuje dane do pliku CSV. """
    if not data:
        print(f"Brak danych do zapisania w {filename}!")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Data i czas", "Cena (USD)"])
        writer.writerows(data)

    print(f"Plik {filename} został utworzony.")
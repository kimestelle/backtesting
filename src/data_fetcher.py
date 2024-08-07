from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockTradesRequest
from datetime import datetime
import pandas as pd
import os

def fetch_tick_data():
    API_KEY = 'AKBHN1RFMO9ZKRFRMYT8'
    API_SECRET = 'RpUXF6k3Zf0R6byzhHA7Scx0FRknvMMfh5D891X3'

    client = StockHistoricalDataClient(API_KEY, API_SECRET)

    request_params = StockTradesRequest(
        symbol_or_symbols="FUN",
        start=datetime(2024, 1, 30, 14, 30),
        end=datetime(2024, 1, 30, 14, 45)
    )
    print('Fetching trades...')
    trades = client.get_stock_trades(request_params).df
    print('Fetched trades:')
    print(trades.head())
    return trades

def save_data(data, filename):
    print("Saving data...")
    if not data.empty:
        print("Data is not empty. Saving...")
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        data.to_csv(filename, index=True)
        print(f"Data saved to {filename}")
    else:
        print("No data to save")

if __name__ == "__main__":
    print("Starting script...")
    data = fetch_tick_data()
    save_data(data, 'data/tick_data.csv')
    print("Script finished.")

from binance.client import Client
import os

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET")
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_order(self, **kwargs):
        return self.client.futures_create_order(**kwargs)

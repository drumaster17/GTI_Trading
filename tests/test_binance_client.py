# test_binance_client.py
import unittest
from exchanges.binance_client import BinanceClient

class TestBinanceClient(unittest.TestCase):
    def test_initialization(self):
        client = BinanceClient()
        self.assertIsNotNone(client.spot_client)
        self.assertIsNotNone(client.futures_client)

if __name__ == "__main__":
    unittest.main()
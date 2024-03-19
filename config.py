from dotenv import load_dotenv
import os

load_dotenv()

EXCHANGES = {
    "binance": {
        "api_key": os.getenv("BINANCE_API_KEY"),
        "secret": os.getenv("BINANCE_SECRET"),
        "use_testnet": os.getenv("BINANCE_USE_TESTNET", "False") == "True",
        "testnet": {
            "api_key": os.getenv("BINANCE_TESTNET_API_KEY"),
            "secret": os.getenv("BINANCE_TESTNET_SECRET"),
        },
    },
    "binance_futures": {
        "api_key": os.getenv("BINANCE_FUTURES_API_KEY"),
        "secret": os.getenv("BINANCE_FUTURES_SECRET"),
        "use_testnet": os.getenv("BINANCE_FUTURES_USE_TESTNET", "False") == "True",
        "testnet": {
            "api_key": os.getenv("BINANCE_FUTURES_TESTNET_API_KEY"),
            "secret": os.getenv("BINANCE_FUTURES_TESTNET_SECRET"),
        },
    },
    "kucoin": {
        "api_key": os.getenv("KUCOIN_API_KEY"),
        "secret": os.getenv("KUCOIN_SECRET"),
        "password": os.getenv("KUCOIN_PASSWORD"),
        "use_testnet": os.getenv("KUCOIN_USE_TESTNET", "False") == "True",
        # Voeg testnet configuratie voor KuCoin hier toe indien beschikbaar
    },
    "coinbase": {
        "api_key": os.getenv("COINBASE_API_KEY"),
        "secret": os.getenv("COINBASE_SECRET"),
        "use_testnet": os.getenv("COINBASE_USE_TESTNET", "False") == "True",
        # Voeg testnet configuratie voor Coinbase hier toe indien beschikbaar
    },
}
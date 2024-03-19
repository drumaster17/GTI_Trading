from ccxt import binance as binance_client
import os

class BinanceClient:
    def __init__(self):
        # Bepaal of de bot op de testnet of live moet draaien
        self.use_testnet = os.getenv("BINANCE_USE_TESTNET", "False") == "True"

        # Configureer de Spot en Futures clients
        self.spot_client = self._initialize_client(is_futures=False)
        self.futures_client = self._initialize_client(is_futures=True)

    def _initialize_client(self, is_futures):
        # API-sleutels ophalen uit omgevingsvariabelen
        if is_futures:
            api_key = os.getenv("BINANCE_FUTURES_API_KEY", "")
            api_secret = os.getenv("BINANCE_FUTURES_SECRET", "")
            if self.use_testnet:
                api_key = os.getenv("BINANCE_FUTURES_TESTNET_API_KEY", "")
                api_secret = os.getenv("BINANCE_FUTURES_TESTNET_SECRET", "")
        else:
            api_key = os.getenv("BINANCE_API_KEY", "")
            api_secret = os.getenv("BINANCE_SECRET", "")
            if self.use_testnet:
                api_key = os.getenv("BINANCE_TESTNET_API_KEY", "")
                api_secret = os.getenv("BINANCE_TESTNET_SECRET", "")
        
        client = binance_client({
            'apiKey': api_key,
            'secret': api_secret,
            'enableRateLimit': True,
        })

        # Configureer de client voor testnet of live
        if self.use_testnet:
            client.set_sandbox_mode(True)
        
        if is_futures:
            client.options['defaultType'] = 'future'
        
        # Controleer of de client correct is geconfigureerd
        try:
            client.load_markets()
        except Exception as e:
            print(f"Failed to initialize client: {e}")
            return None

        return client

if __name__ == "__main__":
    client = BinanceClient()
    print("Spot client:", client.spot_client)
    print("Futures client:", client.futures_client)
    print("Balance:", client.spot_client.fetch_balance())
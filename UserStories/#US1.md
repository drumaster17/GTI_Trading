### US01: API-connectiviteit (Gedetailleerd)

**Samenvatting:** Als gebruiker wil ik dat mijn bot kan verbinden met KuCoin, Binance, en Coinbase via hun API's, zodat ik automatisch transacties kan uitvoeren en mijn portfolio kan beheren.

#### Gedetailleerde Uitwerking en Programmeringsgids

**1. Configuratie Bestand voor API Keys:**
Voordat we beginnen met programmeren, hebben we een veilige plek nodig om onze API keys te bewaren. Dit voorkomt dat gevoelige gegevens hard-coded in de code staan en per ongeluk gedeeld worden.

- **Bestand:** `config.py`
- **Doel:** Slaat API keys en andere configuratiegegevens op.

```python
# config.py
EXCHANGES = {
    "binance": {
        "api_key": "jouw_binance_api_key",
        "secret": "jouw_binance_secret",
    },
    "kucoin": {
        "api_key": "jouw_kucoin_api_key",
        "secret": "jouw_kucoin_secret",
        "password": "jouw_kucoin_password", # Sommige exchanges vereisen extra informatie zoals een password.
    },
    "coinbase": {
        "api_key": "jouw_coinbase_api_key",
        "secret": "jouw_coinbase_secret",
    }
}
```

**2. Installatie en Configuratie van CCXT:**
CCXT is een cryptocurrency trading library die ons in staat stelt om gemakkelijk met veel verschillende exchanges te verbinden.

- Zorg ervoor dat je CCXT hebt geïnstalleerd (`pip install ccxt`).

**3. Opzetten van de Exchange Clients:**
We zullen een module opzetten om verbinding te maken met de exchanges. Dit houdt de code georganiseerd en maakt het gemakkelijk om extra exchanges toe te voegen in de toekomst.

- **Bestand:** `exchange_client.py`

```python
# exchange_client.py
import ccxt
from config import EXCHANGES

class ExchangeClient:
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.exchange = self._init_exchange()

    def _init_exchange(self):
        exchange_class = getattr(ccxt, self.exchange_name)
        exchange = exchange_class({
            'apiKey': EXCHANGES[self.exchange_name]['api_key'],
            'secret': EXCHANGES[self.exchange_name]['secret'],
            'password': EXCHANGES[self.exchange_name].get('password', None), # Niet alle exchanges vereisen een password.
        })
        return exchange

    def get_balance(self):
        return self.exchange.fetch_balance()

# Voorbeeldgebruik:
if __name__ == "__main__":
    binance_client = ExchangeClient("binance")
    print(binance_client.get_balance())

    kucoin_client = ExchangeClient("kucoin")
    print(kucoin_client.get_balance())
```

Dit script toont hoe je een `ExchangeClient` klasse kunt opzetten die verbinding maakt met een exchange. Het haalt ook de balans op als een voorbeeld van hoe je informatie van de exchange kunt ophalen.

**Belangrijk:** Zorg ervoor dat je je echte API keys niet deelt of upload naar openbare repositories. Overweeg om gebruik te maken van environment variabelen of gecodeerde opslagmethodes voor extra beveiliging.
### US02: Portfolio Overzicht (Gedetailleerd)

**Samenvatting:** Als gebruiker wil ik een overzicht kunnen zien van mijn portfolio over alle geïntegreerde exchanges heen, zodat ik inzicht heb in mijn totale holdings en de waarde daarvan in zowel USD als EUR.

#### Gedetailleerde Uitwerking en Programmeringsgids

**1. Opzetten van een PortfolioManager Klasse:**
We hebben een centrale klasse nodig die verantwoordelijk is voor het beheren en ophalen van portfolio-informatie van verschillende exchanges. Deze klasse zal de `ExchangeClient` gebruiken om gegevens van elke exchange op te halen.

- **Bestand:** `portfolio_manager.py`

**2. Structuur van de PortfolioManager Klasse:**

```python
# portfolio_manager.py
from exchange_client import ExchangeClient

class PortfolioManager:
    def __init__(self, exchange_names):
        self.clients = {name: ExchangeClient(name) for name in exchange_names}

    def get_aggregated_portfolio(self):
        # Aggregeer portfolio-informatie van alle exchanges
        portfolio = {}
        for name, client in self.clients.items():
            balance = client.get_balance()
            for currency, amount in balance['total'].items():
                if currency not in portfolio:
                    portfolio[currency] = 0
                portfolio[currency] += amount
        return portfolio

    def get_portfolio_value_in_usd(self):
        # Implementatie hangt af van de beschikbaarheid van prijsinformatie
        # Dit kan een uitdagende taak zijn, aangezien het omzetten van alle
        # currencies naar USD real-time prijsinformatie vereist.
        pass

# Voorbeeldgebruik:
if __name__ == "__main__":
    exchange_names = ["binance", "kucoin", "coinbase"]
    manager = PortfolioManager(exchange_names)
    print(manager.get_aggregated_portfolio())
```

**3. Uitdagingen en Overwegingen:**
- Het omzetten van balances naar USD (of een andere fiat valuta) vereist toegang tot actuele wisselkoersen. CCXT biedt methoden om prijsinformatie op te halen, maar de implementatie hiervan kan variëren afhankelijk van de specifieke behoeften en de beschikbaarheid van pairings op elke exchange.
- Het bijhouden van de totale waarde van je portfolio in fiat valuta vereist regelmatige updates van de wisselkoersen en mogelijk een manier om deze informatie efficiënt op te slaan en te verwerken.

**4. Aanbevelingen:**
- Begin met het implementeren van de basisfunctionaliteit om de totale balances van alle ondersteunde currencies te aggregeren.
- Onderzoek hoe je met de CCXT library real-time prijsinformatie kunt ophalen en gebruik dit om een methode te implementeren die de waarde van elke currency omzet naar USD.
- Overweeg het gebruik van een database of een datastructuur in het geheugen om prijsinformatie en wisselkoersen tijdelijk op te slaan, zodat je niet voortdurend verzoeken hoeft te sturen naar de exchanges voor prijsupdates.

Door de `PortfolioManager` klasse op deze manier te structureren, creëer je een flexibel systeem dat het mogelijk maakt om informatie over je portfolio te aggregeren en weer te geven, en biedt het een fundament om verder uit te breiden met meer geavanceerde features, zoals waardeberekening in fiat valuta's.
# GTI_Trading

## Overzicht
GTI_Trading is een geautomatiseerde cryptocurrency trading bot die gebruikmaakt van de CCXT library om te handelen op meerdere exchanges, waaronder KuCoin, Binance, en Coinbase. Het doel van GTI_Trading is om een flexibele en uitbreidbare bot te ontwikkelen die gebruikers in staat stelt hun crypto-portfolio te beheren, automatisch te handelen op basis van vooraf gedefinieerde strategieën, en snel te reageren op marktveranderingen door middel van een paniekverkoopfunctie.

## Belangrijkste Kenmerken
- Ondersteuning voor meerdere exchanges (KuCoin, Binance, Coinbase).
- Real-time portfolio tracking over alle geïntegreerde exchanges.
- Paniekverkoopfunctie om alle posities snel om te zetten naar USDT.
- Mogelijkheid om uniforme limietorders over meerdere exchanges te plaatsen.
- Beveiligde opslag van API-keys.
- Notificaties via Telegram en e-mail.

## Technologieën
- **Taal:** Python 3.8+
- **Belangrijkste Libraries:** CCXT, Requests, Python-telegram-bot, Pandas

## Setup en Installatie

Voordat je de bot kunt gebruiken, moet je ervoor zorgen dat je Python 3.8 of hoger hebt geïnstalleerd op je systeem en dat je over de juiste toegang beschikt tot de API's van de ondersteunde exchanges.

### Vereisten

- Python 3.8+
- Pip (Python Package Installer)

### Installatie-instructies

1. Kloon het GTI_Trading repository naar je lokale machine met:
git clone https://github.com/yourusername/GTI_Trading.git

2. Navigeer naar de GTI_Trading projectmap:
    cd GTI_Trading

3. Maak een virtuele omgeving aan (optioneel, maar aanbevolen):
    python -m venv venv


Activeer de virtuele omgeving:

- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

4. Installeer de benodigde libraries met pip:
    pip install -r requirements.txt

Dit installeert alle benodigde dependencies zoals vermeld in het `requirements.txt` bestand van het project.





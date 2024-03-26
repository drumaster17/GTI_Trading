import ccxt
from dotenv import load_dotenv
import os
import pandas as pd
import pandas_ta as ta
import time

# Load variables from the .env file
load_dotenv()

# Exchange setup
kucoin = ccxt.kucoin({
    'apiKey': os.getenv("K_apiKey", ""),
    'secret': os.getenv("K_secret", ""),
    'password': os.getenv("K_password", "")
})

def fetch_ohlcv(symbol, timeframe='15m'):
    # Fetch historical data
    ohlcv = kucoin.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime
    df.set_index('timestamp', inplace=True)
    return df

def get_macd_rsi(symbol, timeframe='15m'):
    # Fetch historical data
    df = fetch_ohlcv(symbol, timeframe)
    
    # Calculate MACD
    df.ta.macd(append=True)
    
    # Calculate RSI
    df.ta.rsi(append=True)
    
    # Get the last MACD and RSI values
    macd = df['MACD_12_26_9'].iloc[-1]
    signal = df['MACDs_12_26_9'].iloc[-1]
    rsi = df['RSI_14'].iloc[-1]

    return macd, signal, rsi

def buy_bnb_if_conditions_met():
    symbol = 'BNB/USDT'
    macd_15m, signal_15m, rsi_15m = get_macd_rsi(symbol, timeframe='15m')
    macd_1h, signal_1h, _ = get_macd_rsi(symbol, timeframe='1h')

    # Check combined conditions for both timeframes
    if macd_15m is not None and macd_15m < 0 and macd_15m > signal_15m and rsi_15m > 50 \
       and macd_1h is not None and macd_1h < 0:
        try:
            # Place market buy order for BNB with 5 USDT
            order = kucoin.create_market_buy_order(symbol, cost=5)
            print(f"Bought BNB with 5 USDT at market price.")
        except ccxt.BaseError as e:
            print(f"Error occurred while buying BNB: {e}")

while True:
    buy_bnb_if_conditions_met()
    time.sleep(900)  # Check every 15 minutes

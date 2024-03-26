# top 3 

import datetime
import ccxt
from dotenv import load_dotenv
import os
import time
import pandas as pd
import mplfinance as mpf


# # Laad variabelen uit het .env-bestand
load_dotenv()


# Exchange setup
kucoin = ccxt.kucoin({
    'apiKey': os.getenv("K_apiKey", ""),
    'secret': os.getenv("K_secret", ""),
    'password': os.getenv("K_password", "")
})

def fetch_balances():
    try:
        # Fetch balances
        balances = kucoin.fetch_balance()

        # Filter out currencies with balance greater than zero
        non_zero_balances = {currency: balance for currency, balance in balances['total'].items() if balance > 0}

        return non_zero_balances

    except ccxt.BaseError as e:
        print(f"Error occurred: {e}")
def sell_non_usdt_balances():
    non_usdt_balances = fetch_balances()
    for currency, balance in non_usdt_balances.items():
        try:
            # Create a sell market order for the currency
            order = kucoin.create_market_sell_order(currency + '/USDT', balance)
            print(f"Sold {balance} {currency} at market price.")
        except ccxt.BaseError as e:
            print(f"Error occurred while selling {currency}: {e}")

# Sell non-USDT balances
# sell_non_usdt_balances()

# Fetch and print non-zero balances
non_zero_balances = fetch_balances()
print("Non-zero balances:")
for currency, balance in non_zero_balances.items():
    print(f"{currency}: {balance}")


# # #Exchange setup
# def fetch_balances():
#     kucoin = ccxt.kucoin({
#     'apiKey' : os.getenv("K_apiKey", ""),
#     'secret' : os.getenv("K_secret", ""),
#     'password' : os.getenv("K_password", "")
# })

# try:
#         # Load account info and fetch balances
#         kucoin.load_markets()
#         balances = kucoin.fetch_balance()

#         # Filter out currencies with balance greater than zero
#         non_zero_balances = {currency: balance for currency, balance in balances['total'].items() if balance > 0}

#         return non_zero_balances

#     except ccxt.BaseError as e:
#         print(f"Error occurred: {e}")

# # Fetch and print non-zero balances
# non_zero_balances = fetch_balances()
# print("Non-zero balances:")
# for currency, balance in non_zero_balances.items():
#     print(f"{currency}: {balance}")

# exchange = ccxt.kucoin()
# exchange.load_markets()
# balances = kucoin.fetch_balance()
# # print(exchange.symbols) # to get all the coin pairs in the exchange
# non_zero_balances = {currency: balance for currency, balance in balances['total'].items() if balance > 0}
# # Coin Specs
# coin_name = "BNB/USDT"
# # resolution = "1d"
# # starting_date = "01 January 2024"

# # Check Balance

# print(kucoin.fetch_balance())
# # print("BNB", kucoin.fetch_balance()["BNB"])
# # print("BNB3L", kucoin.fetch_balance()["BNB3L"])
# # print("USDT", kucoin.fetch_balance()["USDT"])
# # print("KCS", kucoin.fetch_balance()["KCS"])

# # Check Prices
# print(kucoin.fetch_ticker(coin_name))

# # Buy Order
# order_type = "market"
# side = "buy"

# current_price = (kucoin.fetch_ticker(coin_name)["ask"] + kucoin.fetch_ticker(coin_name)["bid"]) / 2
# amount = 5 / current_price
# # amount = 5.0
# # kucoin.create_order(
# #     coin_name,
# #     order_type,
# #     side,
# #     amount,
# # )

# # print(kucoin.create_order(coin_name, order_type, side, amount))

# # kucoin.create_market_buy_order(coin_name,

# # Sell Order
# # order_type = "market"
# # side = "sell"
# # amount

# # starting_date = time.strptime(starting_date, "%d %B %Y") # convert to time.struct_time
# # starting_date = time.mktime(starting_date) # convert to seconds
# # starting_date = starting_date * 1000 # convert to milliseconds for kucoin

# # data = exchange.fetch_ohlcv(coin_name, timeframe=resolution, since=starting_date)


# # storing it into a pandas dataframe
# # data = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# # formatting the index

# # data.set_index(data['timestamp'], inplace=True)
# # data.index = pd.to_datetime(data.index, unit='ms')
# # del data['timestamp']

# # formatting the numbers
# # data["close"] = pd.to_numeric(data["close"])
# # data["high"] = pd.to_numeric(data["high"])
# # data["low"] = pd.to_numeric(data["low"])
# # data["open"] = pd.to_numeric(data["open"])
# # data["volume"] = pd.to_numeric(data["volume"])
# # print(data)

# # chart

# # mpf.plot(data,
# #          type = 'candle',
# #          style = "binance",
# #          title = f"{coin_name}",
# #          ylabel = 'Price',
# #          volume = True,
# #          ylabel_lower = 'Volume',
# #          mav = (5,10),
# # savefig='plot.png',





                             



# # #
# # # kucoin = ccxt.kucoin({
# # #     'apiKey' : os.getenv("K_apiKey", ""),
# # #     'secret' : os.getenv("K_secret", ""),
# # #     'password' : os.getenv("K_password", "")

# # # check connection
# # print("BNB", kucoin.fetch_balance()["BNB"])
# # print("USDT", kucoin.fetch_balance()["USDT"])
# # print("KCS", kucoin.fetch_balance()["KCS"])



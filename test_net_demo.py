# Let's try this out

# API Key: sxV243LlOdPF8hzKGfiZWjnN4PZAfwkQRpNDnYlqHYHmWh8HGqRQlMCxzLjYMxb7

# Secret Key: B9duqs0DkZE2wQqohygM7IxHleZsgZ3ov7o6ObmWMZz8me8FBFfHg7Ys4Sdagnvs

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.enums import *
from time import sleep
import json



api_key = 'sxV243LlOdPF8hzKGfiZWjnN4PZAfwkQRpNDnYlqHYHmWh8HGqRQlMCxzLjYMxb7'
api_private = 'B9duqs0DkZE2wQqohygM7IxHleZsgZ3ov7o6ObmWMZz8me8FBFfHg7Ys4Sdagnvs'

client = Client(api_key, api_private, testnet=True, tld='us')

btc_balance = client.get_asset_balance(asset='BTC')

print(btc_balance)

btc_price = client.get_symbol_ticker(symbol='BTCUSDT')
print(btc_price["price"])



















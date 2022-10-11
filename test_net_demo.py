from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.enums import *
from time import sleep
import json

api_key = 'sxV243LlOdPF8hzKGfiZWjnN4PZAfwkQRpNDnYlqHYHmWh8HGqRQlMCxzLjYMxb7'
api_secret = 'B9duqs0DkZE2wQqohygM7IxHleZsgZ3ov7o6ObmWMZz8me8FBFfHg7Ys4Sdagnvs'
client = Client(api_key, api_secret, testnet=True, tld='us')


class TradeBot:
    """Trading Bot Class"""

    def __init__(self, bot_name):
        # Probably don't need a name but oh well
        self.name = bot_name
        self._btc_balance = None
        self._last_btc_price = None


from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.enums import *
from time import sleep
import json

api_public = 'sxV243LlOdPF8hzKGfiZWjnN4PZAfwkQRpNDnYlqHYHmWh8HGqRQlMCxzLjYMxb7'
api_secret = 'B9duqs0DkZE2wQqohygM7IxHleZsgZ3ov7o6ObmWMZz8me8FBFfHg7Ys4Sdagnvs'

# client = Client(api_key, api_secret, testnet=True, tld='us')

class TradeBot:
    """Trading Bot Class"""

    def __init__(self):
        self._btc_balance = None
        self._last_btc_price = None
        self._api_key = None
        self._api_secret = None
        self._client = None

    def set_keys(self, public_key, secret_key):
        """Sets the keys for the account linked to the bot"""
        self._api_key = public_key
        self._api_secret = secret_key

    def create_client(self):
        """Create a client to be used with the bot, returns the client object"""
        self._client = Client(self._api_key, self._api_secret, testnet=True, tld='us')

    def get_client(self):
        """Returns the Client object"""
        return self._client

    def update_btc_balance(self):
        """Updates the value in the BTC balance"""
        self._btc_balance = self._client.get_asset_balance(asset='BTC')['free']

    def get_btc_balance(self):
        """Updates the balance and returns the free BTC balance"""
        self.update_btc_balance()
        return self._btc_balance

    def get_current_btc_price(self):
        """Updates the latest btc price and prints it out"""
        self._last_btc_price = self._client.get_symbol_ticker(symbol='BTCUSDT')['price']
        print(self._last_btc_price)

    def get_balance_of(self, asset_name):
        """Returns the balance of the specified asset"""
        asset = asset_name + "USDT"
        return self._client.get_asset_balance(asset=asset_name)['free']

    def get_price_of(self, asset_name):
        """Returns the latest price of the requested asset"""
        asset = asset_name + "USDT"
        return self._client.get_symbol_ticker(symbol=asset)['price']


bot_1 = TradeBot()
bot_1.set_keys(api_public, api_secret)
bot_1.create_client()
bot_1.update_btc_balance()
bot_1.get_current_btc_price()

balance = bot_1.get_btc_balance()
print("Bot_1's current BTC Balance is", balance, '\n')
print('Bot_1s balance of ETH is ', bot_1.get_balance_of('ETH'), '\n')
print('The current price of ETH is ', bot_1.get_price_of('ETH'), '\n')

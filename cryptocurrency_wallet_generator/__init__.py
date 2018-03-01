from .currencies.bitcoin import Bitcoin
from .currencies.bitcoincash import BitcoinCash
from .currencies.dash import Dash
from .currencies.ethereum import Ethereum
from .currencies.litecoin import Litecoin
from .currencies.garlicoin import Garlicoin


currencies = {
    "Bitcoin": Bitcoin,
    "Bitcoin Cash": BitcoinCash,
    "Dash": Dash,
    "Ethereum": Ethereum,
    "Litecoin": Litecoin,
    "Garlicoin": Garlicoin,
}


def generate_wallet(currency_name):
    currency = currencies[currency_name]()
    return currency.generate_wallet()

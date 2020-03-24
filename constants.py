# build & docker version - to be automated
VERSION = "v1.4.10"

# last prices from the previous run - to be automated
INITIAL_PRICES = {'eth_usd': 124.28, 'btc_usd': 5907.35, 'ln_btc': 0.001081, 'ln_usd': 6.39,
                  'timestamp_utc': 1584894426.848551, 'datetime_utc': '2020-03-23T01:27:06.848551'}

# bitfront response keys
KEY_RESPONSE_DATA = 'responseData'
KEY_LAST = 'last'

# response keys
ETH_USD = 'eth_usd'
BTC_USD = 'btc_usd'
LN_BTC = 'ln_btc'
LN_USD = 'ln_usd'
TIMESTAMP_UTC = 'timestamp_utc'
DATETIME_UTC = 'datetime_utc'

# registered coin pairs
PAIRS = {
    'LN': LN_USD,
    'BTC': BTC_USD,
    'ETH': ETH_USD
}

# time
ONE_MIN_IN_SEC = 60

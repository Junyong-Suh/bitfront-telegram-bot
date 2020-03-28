# build & docker version - to be automated
VERSION = "v1.5.0"

# symbols and currencies
BTC = 'BTC'
ETH = 'ETH'
LN = 'LN'
KRW = 'KRW'
USD = 'USD'

# exchanges
EXCHANGE_NAME = 'exchange_name'
BITFRONT = 'bitfront'
COINBASE = 'coinbase'
GOPAX = 'gopax'
UPBIT = 'upbit'

# response keys
BTC_USD = 'btc_usd'
BTC_KRW = 'btc_krw'
ETH_USD = 'eth_usd'
ETH_KRW = 'eth_krw'
LN_BTC = 'ln_btc'
LN_USD = 'ln_usd'
TIMESTAMP_UTC = 'timestamp_utc'
DATETIME_UTC = 'datetime_utc'

# registered coin pairs in exchanges
# coinbase supports both KRW and USD but USD only for now
EXCHANGE_PAIRS = {
    BITFRONT: {
        LN: LN_USD,
        BTC: BTC_USD,
        ETH: ETH_USD
    },
    COINBASE: {
        BTC: BTC_USD,
        ETH: ETH_USD
    },
    GOPAX: {
        BTC: BTC_KRW,
        ETH: ETH_KRW
    },
    UPBIT: {
        BTC: BTC_KRW,
        ETH: ETH_KRW
    }
}

UPPER_BOUND = 'upper'
LOWER_BOUND = 'lower'
USD_KRW_EXCHANGE_RATE = 1200
THRESHOLDS = {
    UPPER_BOUND: {
        BTC_USD: 7000,
        ETH_USD: 150,
        LN_USD: 7.5,
        BTC_KRW: 7000 * USD_KRW_EXCHANGE_RATE,
        ETH_KRW: 150 * USD_KRW_EXCHANGE_RATE
    },
    LOWER_BOUND: {
        BTC_USD: 5500,
        ETH_USD: 120,
        LN_USD: 6.5,
        BTC_KRW: 5500 * USD_KRW_EXCHANGE_RATE,
        ETH_KRW: 120 * USD_KRW_EXCHANGE_RATE
    }
}

# last prices from the previous run - to be automated
INITIAL_PRICES = {'bitfront': {'eth_usd': 128.78, 'btc_usd': 6244.92, 'ln_btc': 0.00113, 'ln_usd': 7.06, 'timestamp_utc': 1585377367.153477, 'datetime_utc': '2020-03-28T15:36:07.153477', 'exchange_name': 'bitfront'}, 'coinbase': {'btc_usd': 6245.005, 'btc_krw': 7573567.3637, 'eth_usd': 128.715, 'eth_krw': 156097.8291, 'timestamp_utc': 1585377367.559408, 'datetime_utc': '2020-03-28T15:36:07.559408', 'exchange_name': 'coinbase'}, 'gopax': {'btc_krw': 7645000, 'eth_krw': 157600, 'timestamp_utc': 1585377367.746028, 'datetime_utc': '2020-03-28T15:36:07.746028', 'exchange_name': 'gopax'}, 'upbit': {'btc_krw': 7636000.0, 'eth_krw': 157350.0, 'timestamp_utc': 1585377367.894074, 'datetime_utc': '2020-03-28T15:36:07.894074', 'exchange_name': 'upbit'}}

# bitfront response keys
KEY_RESPONSE_DATA = 'responseData'
KEY_LAST = 'last'

# gopax response keys
KEY_PRICE = 'price'

# coinbase response keys
KEY_DATA = 'data'
KEY_RATES = 'rates'

# upbit response keys
KEY_TRADE_PRICE = 'trade_price'

# time
ONE_MIN_IN_SEC = 60

# notification footer types
EVENT = "EVENT"
HOURLY = "HOURLY"

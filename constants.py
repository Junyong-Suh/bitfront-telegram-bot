# build & docker version - to be automated
VERSION = "v1.5.0"

# last prices from the previous run - to be automated
INITIAL_PRICES = {'bitfront': {'eth_usd': 131.73, 'btc_usd': 6435, 'ln_btc': 0.00122999, 'ln_usd': 7.91, 'timestamp_utc': 1585600164.559508, 'datetime_utc': '2020-03-31T05:29:24.559508', 'exchange_name': 'bitfront'}, 'coinbase': {'btc_usd': 6413.365, 'btc_krw': 7820874.149725, 'eth_usd': 131.52, 'eth_krw': 160384.0368, 'timestamp_utc': 1585600164.760461, 'datetime_utc': '2020-03-31T05:29:24.760461', 'exchange_name': 'coinbase'}, 'gopax': {'btc_krw': 7815000, 'eth_krw': 160000, 'timestamp_utc': 1585600164.98631, 'datetime_utc': '2020-03-31T05:29:24.986310', 'exchange_name': 'gopax'}, 'upbit': {'btc_krw': 7823000.0, 'eth_krw': 160150.0, 'timestamp_utc': 1585600165.154777, 'datetime_utc': '2020-03-31T05:29:25.154777', 'exchange_name': 'upbit'}}

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

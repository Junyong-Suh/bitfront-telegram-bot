# build & docker version - to be automated
VERSION = "v1.5.8"

# last prices from the previous run - to be automated
INITIAL_PRICES = {'bitfront': {'eth_usd': 144.15, 'btc_usd': 6880.39, 'ln_btc': 0.00140998, 'ln_usd': 9.7, 'timestamp_utc': 1585889855.381443, 'datetime_utc': '2020-04-03T13:57:35.381443', 'exchange_name': 'bitfront'}, 'coinbase': {'btc_usd': 6890.055, 'btc_krw': 8524720.54875, 'eth_usd': 144.025, 'eth_krw': 178194.93125, 'timestamp_utc': 1585889855.998378, 'datetime_utc': '2020-04-03T13:57:35.998378', 'exchange_name': 'coinbase'}, 'gopax': {'btc_krw': 8272000, 'eth_krw': 173000, 'timestamp_utc': 1585889856.225254, 'datetime_utc': '2020-04-03T13:57:36.225254', 'exchange_name': 'gopax'}, 'upbit': {'btc_krw': 8273000.0, 'eth_krw': 172700.0, 'timestamp_utc': 1585889856.400983, 'datetime_utc': '2020-04-03T13:57:36.400983', 'exchange_name': 'upbit'}}

# symbols and currencies
BTC = "BTC"
ETH = "ETH"
LN = "LN"
KRW = "KRW"
USD = "USD"

# exchanges
EXCHANGE_NAME = "exchange_name"
BITFRONT = "bitfront"
COINBASE = "coinbase"
GOPAX = "gopax"
UPBIT = "upbit"

# response keys
BTC_USD = "btc_usd"
BTC_KRW = "btc_krw"
ETH_USD = "eth_usd"
ETH_KRW = "eth_krw"
LN_BTC = "ln_btc"
LN_USD = "ln_usd"
TIMESTAMP_UTC = "timestamp_utc"
DATETIME_UTC = "datetime_utc"

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

UPPER_BOUND = "upper"
LOWER_BOUND = "lower"
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
KEY_RESPONSE_DATA = "responseData"
KEY_LAST = "last"

# gopax response keys
KEY_PRICE = "price"

# coinbase response keys
KEY_DATA = "data"
KEY_RATES = "rates"

# upbit response keys
KEY_TRADE_PRICE = "trade_price"

# time
ONE_MIN_IN_SEC = 60

# notification footer types
EVENT = "EVENT"
HOURLY = "HOURLY"

# error responses
ERROR_RESPONSE = {
    BITFRONT: {KEY_RESPONSE_DATA: {KEY_LAST: 0}},
    COINBASE: {KEY_DATA: {KEY_RATES: {USD: 0, KRW: 0}}},
    GOPAX: {KEY_PRICE: 0},
    UPBIT: [{KEY_TRADE_PRICE: 0}]
}

# log level
LOG_DEBUG = "debug"
LOG_INFO = "info"
LOG_WARNING = "warning"
LOG_ERROR = "error"

# ElasticSearch
ES_INDEX_LOGS = "logs"
ES_LOG_LEVEL = "level"
ES_MSG = "msg"

# The domain with https:// and trailing slash. For example, https://my-test-domain.us-east-1.es.amazonaws.com/
ES_HOST = "https://search-bitfront-telegram-bot-bm2tdula3ijlvjsxgfafe7ab5a.us-west-1.es.amazonaws.com/"

# build & docker version - to be automated
VERSION = "v1.6.6"
KEY_VERSION = "version"

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
ES_LOG = "log"

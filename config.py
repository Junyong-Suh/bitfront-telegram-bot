import constants as c

USD_KRW_EXCHANGE_RATE = 1100
THRESHOLDS = {
    c.UPPER_BOUND: {
        c.BTC_USD: 40000,
        c.ETH_USD: 1300,
        c.LN_USD: 15,
        c.BTC_KRW: 40000 * USD_KRW_EXCHANGE_RATE,
        c.ETH_KRW: 1300 * USD_KRW_EXCHANGE_RATE
    },
    c.LOWER_BOUND: {
        c.BTC_USD: 30000,
        c.ETH_USD: 800,
        c.LN_USD: 10,
        c.BTC_KRW: 30000 * USD_KRW_EXCHANGE_RATE,
        c.ETH_KRW: 800 * USD_KRW_EXCHANGE_RATE
    }
}

TELEGRAM_IDS_SUBSCRIBER = ["1045847434", "692300937"]  # JY (KR) JH
# TELEGRAM_IDS_SUBSCRIBER = ["1045847434"]  # JY (KR)
TELEGRAM_IDS_PREMIUM = ["1045847434"]  # JY

# The domain with https:// and trailing slash. For example, https://my-test-domain.us-east-1.es.amazonaws.com/
ES_HOST = "https://search-bitfront-telegram-bot-bm2tdula3ijlvjsxgfafe7ab5a.us-west-1.es.amazonaws.com/"

import constants as c

USD_KRW_EXCHANGE_RATE = 1215
THRESHOLDS = {
    c.UPPER_BOUND: {
        c.BTC_USD: 8500,
        c.ETH_USD: 220,
        c.LN_USD: 12,
        c.BTC_KRW: 8500 * USD_KRW_EXCHANGE_RATE,
        c.ETH_KRW: 220 * USD_KRW_EXCHANGE_RATE
    },
    c.LOWER_BOUND: {
        c.BTC_USD: 5500,
        c.ETH_USD: 130,
        c.LN_USD: 6,
        c.BTC_KRW: 5500 * USD_KRW_EXCHANGE_RATE,
        c.ETH_KRW: 130 * USD_KRW_EXCHANGE_RATE
    }
}

TELEGRAM_IDS_SUBSCRIBER = ["1045847434", "692300937"]  # JY (KR) JH
# TELEGRAM_IDS_SUBSCRIBER = ["1045847434"]  # JY (KR)
TELEGRAM_IDS_PREMIUM = ["1045847434"]  # JY

# The domain with https:// and trailing slash. For example, https://my-test-domain.us-east-1.es.amazonaws.com/
ES_HOST = "https://search-bitfront-telegram-bot-bm2tdula3ijlvjsxgfafe7ab5a.us-west-1.es.amazonaws.com/"
from datetime import datetime
import constants as c
from lib import remote


# get coin pair from GOPAX
def get_coin_pair(ticker1, ticker2, timeout=3):
    quote_url = "https://api.gopax.co.kr/trading-pairs/" + ticker1 + "-" + ticker2 + "/ticker"
    fallback_response = c.ERROR_RESPONSE[c.GOPAX]
    return remote.get_quote(quote_url, fallback_response, timeout)


# Get last prices of KRW-BTC, KRW-ETH from GOPAX
def get_last_prices():
    r = get_coin_pair(c.BTC, c.KRW)
    btc_krw = r[c.KEY_PRICE]
    r = get_coin_pair(c.ETH, c.KRW)
    eth_krw = r[c.KEY_PRICE]
    utc_now = datetime.utcnow()
    return {
        c.BTC_KRW: btc_krw,
        c.ETH_KRW: eth_krw,
        c.TIMESTAMP_UTC: datetime.timestamp(utc_now),
        c.DATETIME_UTC: utc_now.isoformat(),
        c.EXCHANGE_NAME: c.GOPAX
    }

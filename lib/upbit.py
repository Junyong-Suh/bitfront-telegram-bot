from datetime import datetime
import constants as c
from lib import remote


# get coin pair from UPBIT
def get_coin_pair(ticker1, ticker2, timeout=3):
    quote_url = "https://api.upbit.com/v1/trades/ticks?market=" + ticker1 + "-" + ticker2 + "&count=1"
    fallback_response = c.ERROR_RESPONSE[c.UPBIT]
    return remote.get_quote(quote_url, fallback_response, timeout)


# Get last prices of KRW-BTC, KRW-ETH from UPBIT
def get_last_prices():
    r = get_coin_pair(c.KRW, c.BTC)
    btc_krw = r[0][c.KEY_TRADE_PRICE]
    r = get_coin_pair(c.KRW, c.ETH)
    eth_krw = r[0][c.KEY_TRADE_PRICE]
    utc_now = datetime.utcnow()
    return {
        c.BTC_KRW: btc_krw,
        c.ETH_KRW: eth_krw,
        c.TIMESTAMP_UTC: datetime.timestamp(utc_now),
        c.DATETIME_UTC: utc_now.isoformat(),
        c.EXCHANGE_NAME: c.UPBIT
    }

from datetime import datetime
import requests
import constants as c
import logging


# get coin pair from upbit
# timeout -> infinite retry
def get_coin_pair(ticker1, ticker2, timeout=3):
    try:
        r = requests.get(
            "https://api.upbit.com/v1/trades/ticks?market=" + ticker1 + "-" + ticker2 + "&count=1",
            timeout=timeout
        )
    except requests.exceptions.ReadTimeout as rtErr:
        logging.error("ReadTimeout: " + str(rtErr))
        return get_coin_pair(ticker1, ticker2, timeout+1)

    return r.json()


# Get last prices of KRW-BTC, KRW-ETH from upbit
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

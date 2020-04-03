from datetime import datetime
import requests
import constants as c
import logging


# get coin pair from upbit
def get_coin_pair(ticker1, ticker2, timeout=3):
    try:
        r = requests.get(
            "https://api.upbit.com/v1/trades/ticks?market=" + ticker1 + "-" + ticker2 + "&count=1",
            timeout=timeout
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e:
        logging.error(e)
    except requests.exceptions.ConnectionError as e:
        logging.error(e)
    except requests.exceptions.Timeout as e:
        logging.error(e)
    except requests.exceptions.RequestException as e:
        logging.error(e)
    return c.ERROR_RESPONSE[c.UPBIT]


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

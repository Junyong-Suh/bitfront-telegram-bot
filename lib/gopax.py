from datetime import datetime
import requests
import constants as c
from lib import logger


# get coin pair from gopax
def get_coin_pair(ticker1, ticker2, timeout=3):
    try:
        r = requests.get(
            "https://api.gopax.co.kr/trading-pairs/" + ticker1 + "-" + ticker2 + "/ticker",
            timeout=timeout
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e:
        logger.error(str(e))
    except requests.exceptions.ConnectionError as e:
        logger.error(str(e))
    except requests.exceptions.Timeout as e:
        logger.error(str(e))
    except requests.exceptions.RequestException as e:
        logger.error(str(e))
    return c.ERROR_RESPONSE[c.GOPAX]


# Get last prices of KRW-BTC, KRW-ETH from gopax
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

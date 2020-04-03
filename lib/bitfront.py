from datetime import datetime
import requests
import constants as c
from lib import logger


# get coin pair from bitfront
def get_coin_pair(ticker1, ticker2, timeout=3):
    try:
        r = requests.get(
            "https://openapi.bitfront.me/v1/market/public/currentTickValue?coinPair=" + ticker1 + "." + ticker2 + "",
            timeout=timeout
        )
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e:
        logger.error(e)
    except requests.exceptions.ConnectionError as e:
        logger.error(e)
    except requests.exceptions.Timeout as e:
        logger.error(e)
    except requests.exceptions.RequestException as e:
        logger.error(e)
    return c.ERROR_RESPONSE[c.BITFRONT]


# Get last prices of ETH-USD, BTC-USD, LN-BTC from bitfront
# calculate LN-USD from BTC-USD and LN-BTC
def get_last_prices():
    r = get_coin_pair(c.ETH, c.USD)
    eth_usd = r[c.KEY_RESPONSE_DATA][c.KEY_LAST]
    r = get_coin_pair(c.BTC, c.USD)
    btc_usd = r[c.KEY_RESPONSE_DATA][c.KEY_LAST]
    r = get_coin_pair(c.LN, c.BTC)
    ln_btc = r[c.KEY_RESPONSE_DATA][c.KEY_LAST]
    ln_usd = round(btc_usd * ln_btc, 2)
    utc_now = datetime.utcnow()
    return {
        c.ETH_USD: eth_usd,
        c.BTC_USD: btc_usd,
        c.LN_BTC: ln_btc,
        c.LN_USD: ln_usd,
        c.TIMESTAMP_UTC: datetime.timestamp(utc_now),
        c.DATETIME_UTC: utc_now.isoformat(),
        c.EXCHANGE_NAME: c.BITFRONT
    }

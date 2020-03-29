from datetime import datetime
import requests
import constants as c
import logging


# get coin pair from coinbase
# timeout -> infinite retry
def get_coin_pair(ticker, timeout=3):
    try:
        r = requests.get(
            "https://api.coinbase.com/v2/exchange-rates?currency=" + ticker,
            timeout=timeout
        )
    except requests.exceptions.ReadTimeout as rtErr:
        logging.error("ReadTimeout: " + str(rtErr))
        return get_coin_pair(ticker, timeout+1)

    return r.json()


# Get last rates of BTC and ETH from coinbase
def get_last_prices():
    r = get_coin_pair(c.BTC)
    btc_rates = r[c.KEY_DATA][c.KEY_RATES]
    r = get_coin_pair(c.ETH)
    eth_rates = r[c.KEY_DATA][c.KEY_RATES]
    utc_now = datetime.utcnow()
    # coinbase rates are returned in string so covert to float
    return {
        c.BTC_USD: float(btc_rates[c.USD]),
        c.BTC_KRW: float(btc_rates[c.KRW]),
        c.ETH_USD: float(eth_rates[c.USD]),
        c.ETH_KRW: float(eth_rates[c.KRW]),
        c.TIMESTAMP_UTC: datetime.timestamp(utc_now),
        c.DATETIME_UTC: utc_now.isoformat(),
        c.EXCHANGE_NAME: c.COINBASE
    }

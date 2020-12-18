from datetime import datetime
import constants as c
from lib import logger, remote


# get coin pair from CoinBase
def get_coin_pair(ticker, timeout=5):
    quote_url = "https://api.coinbase.com/v2/exchange-rates?currency=" + ticker
    fallback_response = c.ERROR_RESPONSE[c.COINBASE]
    return remote.get_quote(quote_url, fallback_response, timeout)


# Get last rates of BTC and ETH from CoinBase
def get_last_prices():
    r_btc = get_coin_pair(c.BTC)
    btc_rates = r_btc[c.KEY_DATA][c.KEY_RATES]
    r_eth = get_coin_pair(c.ETH)
    eth_rates = r_eth[c.KEY_DATA][c.KEY_RATES]
    utc_now = datetime.utcnow()

    # if either request is failed, mark both as failed to skip Coinbase
    # Coinbase API fails too often + retry fails too
    if btc_rates[c.USD] == 0 or eth_rates[c.USD] == 0:
        btc_rates = eth_rates = {c.USD: 0, c.KRW: 0}
        logger.error({c.ES_LOG: "Either or both call to Coinbase failed"})

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

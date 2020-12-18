from datetime import datetime
import constants as c
from lib import remote


# get coin pair from BitFront
def get_coin_pair(ticker1, ticker2, timeout=3):
    quote_url = "https://openapi.bitfront.me/v1/market/public/currentTickValue?coinPair=" + ticker1 + "." + ticker2 + ""
    fallback_response = c.ERROR_RESPONSE[c.BITFRONT]
    return remote.get_quote(quote_url, fallback_response, timeout)


# Get last prices of ETH-USD, BTC-USD, LN-BTC from BitFront
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

import requests

# get coin pair from bitfront
def getCoinPair(ticker1, ticker2):
    r = requests.get("https://openapi.bitfront.me/v1/market/public/currentTickValue?coinPair="+ ticker1 +"."+ ticker2 +"")
    return r.json()

# grab ETH-USD, BTC-USD, LN-BTC from bitfront
# calculate LN-USD from BTC-USD and LN-BTC
def grabPrices():
    r = getCoinPair("ETH", "USD")
    eth_usd = r['responseData']['last']
    r = getCoinPair("BTC", "USD")
    btc_usd = r['responseData']['last']
    r = getCoinPair("LN", "BTC")
    ln_btc = r['responseData']['last']
    ln_usd = round(btc_usd * ln_btc, 2)
    return {
        "eth_usd": eth_usd,
        "btc_usd": btc_usd,
        "ln_btc": ln_btc,
        "ln_usd": ln_usd
    }

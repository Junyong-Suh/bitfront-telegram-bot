import bitfront
import confidentials
import telegram
import time
import requests

# As a input to time.sleep() in sec
class PRICE_CHECK_INTERVAL():
    def ONE_MIN():
        return 60   # every min
    def TEN_MIN():
        return 600  # every 10 min
    def ONE_HOUR():
        return 3600 # every hour

def composeResult(current_prices):
    eth_usd = current_prices['eth_usd']
    btc_usd = current_prices['btc_usd']
    ln_btc = current_prices['ln_btc']
    ln_usd = round(btc_usd * ln_btc, 2)
    return "1LN = ${0} ({1} BTC)\n1BTC = ${2}\n1ETH = ${3}".format(
        str(ln_usd), str(ln_btc), str(btc_usd), str(eth_usd)
    )

def worth_notify(current_prices):
    # BTC Price Min and Max
    worth_btc = current_prices['btc_usd'] < 5000 or 5500 < current_prices['btc_usd']
    # ETH Price Min and Max
    worth_eth = current_prices['eth_usd'] < 100 or 120 < current_prices['eth_usd']
    # LN Price Min and Max
    worth_ln = current_prices['ln_usd'] < 4.5 # or 6 < current_prices['ln_usd']
    return worth_btc or worth_eth or worth_ln

def has_been_an_hour(current_prices, last_run_prices):
    return PRICE_CHECK_INTERVAL.ONE_HOUR() < current_prices['timestamp_utc'] - last_run_prices['timestamp_utc']

# ToDos
# 1. History and Statistics :: % change from the last notification
# 2. Dynamic register and deregister of telegram ids (from the bot)
# 3. Add unit tests
# 4. Add integration tests

def main():
    # exit if no receiver
    if not confidentials.TELEGRAM_IDS_SUBSCRIBER:
        print("No Telegram IDs to send the message - Add your Telegram IDs to ./confidentials.py (Please read README.md)")
        return

    # initialize
    last_run_prices = bitfront.getLastPrices() # will be replaced by a class
    time.sleep(3)

    # get the last prices and notify
    while True:
        current_prices = bitfront.getLastPrices()
        print(current_prices) # log to STDOUT

        if worth_notify(current_prices):
            # event notification
            msg = "WORK HARD MAKE MONEY\n" + composeResult(current_prices)
            telegram.notifyAllOnTelegram(msg, True) # to premium users only
            time.sleep(PRICE_CHECK_INTERVAL.ONE_MIN())
        elif has_been_an_hour(current_prices, last_run_prices):
            # hourly notification
            msg = "[Hourly Notification]\n" + composeResult(current_prices)
            telegram.notifyAllOnTelegram(msg, False) # to subscribers
            time.sleep(PRICE_CHECK_INTERVAL.TEN_MIN())
        else:
            # no notification
            time.sleep(PRICE_CHECK_INTERVAL.TEN_MIN())

        last_run_prices  = current_prices  # update the status

# main
main()

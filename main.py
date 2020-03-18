import requests
import confidentials
import telegram
import bitfront
import time

# As a input to time.sleep() in sec
class PRICE_CHECK_INTERVAL():
    def Often():
        return 60   # every min
    def Casual():
        return 600  # every 10 min
    def Slow():
        return 3600 # every hour

def composeResult(last_prices):
    eth_usd = last_prices['eth_usd']
    btc_usd = last_prices['btc_usd']
    ln_btc = last_prices['ln_btc']
    ln_usd = round(btc_usd * ln_btc, 2)
    return "1LN = $"+ str(ln_usd) +" ("+ str(ln_btc) + " BTC)" + "\n1BTC = $"+ str(btc_usd) + "\n1ETH = $"+ str(eth_usd)

def worth_notify(last_prices):
    # BTC Price Min and Max
    worth_btc = last_prices['btc_usd'] < 5000 or 5500 < last_prices['btc_usd']
    # ETH Price Min and Max
    worth_eth = last_prices['eth_usd'] < 100 or 120 < last_prices['eth_usd']
    # LN Price Min and Max
    worth_ln = last_prices['ln_usd'] < 4.5 # or 6 < last_prices['ln_usd']
    return worth_btc or worth_eth or worth_ln

# ToDos
# 1. History and Statistics :: % change from the last notification
# 2. Dynamic register and deregister of telegram ids (from the bot)

def main():
    # exit if no receiver
    if not confidentials.TELEGRAM_IDS:
        print("No Telegram IDs to send the message - Add your Telegram IDs to ./confidentials.py (Please read README.md)")
        return

    # grab the prices and notify
    while True:
        last_prices = bitfront.grabPrices()
        if worth_notify(last_prices):
            msg = "WORK HARD MAKE MONEY\n" + composeResult(last_prices)
            telegram.notifyAllOnTelegram(msg)
            time.sleep(PRICE_CHECK_INTERVAL.Often())
        else:
            print(last_prices)
            time.sleep(PRICE_CHECK_INTERVAL.Casual())

# main
main()

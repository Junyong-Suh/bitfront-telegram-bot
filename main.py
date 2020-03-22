import bitfront
import confidentials
import notification as notify
import time
import logging
import constants as c

# logging option
logging.basicConfig(level=logging.INFO)


# event thresholds for the premium users - i.e., myself :)
def worth_notify(current_prices):
    # return worth_downwards(current_prices)
    # return worth_upwards(current_prices)
    return worth_downwards(current_prices) or worth_upwards(current_prices)


# BTC, ETH, LN lower bound
def worth_downwards(current_prices):
    btc_by_price = current_prices[c.BTC_USD] < 5200
    eth_by_price = current_prices[c.ETH_USD] < 125
    ln_by_price = current_prices[c.LN_USD] < 4.5
    return btc_by_price or eth_by_price or ln_by_price


# BTC, ETH, LN upper bound
def worth_upwards(current_prices):
    btc_by_price = 6000 < current_prices[c.BTC_USD]
    eth_by_price = 200 < current_prices[c.ETH_USD]
    ln_by_price = 6 < current_prices[c.LN_USD]
    return btc_by_price or eth_by_price or ln_by_price


# current_prices[c.DATETIME_UTC] == datetime.utcnow().isoformat()
# ex. '2020-03-22T04:15:48.832863'
def is_o_clock(current_prices):
    return current_prices[c.DATETIME_UTC][14:16] == '00'


# ToDos
# 1. History and Statistics :: % change from the last notification
# 2. Dynamic register and deregister of telegram ids (from the bot)
# 3. Add unit tests
# 4. Add integration tests


def main():
    # exit if no receiver
    if not confidentials.TELEGRAM_IDS_SUBSCRIBER:
        logging.error('No Telegram IDs to notify - Set your confidentials.py (Read README.md)')
        return

    # initialize
    last_event_prices = last_hourly_prices = {}

    # get the last prices and notify
    while True:
        current_prices = bitfront.get_last_prices()
        logging.info(current_prices)  # log to STDOUT

        if is_o_clock(current_prices):
            # hourly notification
            notify.to_subscribers(current_prices, last_hourly_prices)
            last_hourly_prices = current_prices

        if worth_notify(current_prices):
            # event notification
            notify.to_premiums(current_prices, last_event_prices)
            last_event_prices = current_prices

        # check every min
        time.sleep(c.ONE_MIN_IN_SEC)


# main
main()

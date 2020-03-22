import bitfront
import confidentials
import telegram
import time
import logging
import constants as c

VERSION = "v1.4.5"  # build & docker version - to be automated
logging.basicConfig(level=logging.INFO)


# notify to premium users (a.k.a. event based, i.e., myself lol)
def notify_to_premiums(current_prices, last_prices):
    result = compose_result(current_prices, last_prices)
    msg = "WORK HARD MAKE MONEY\n" + result + "\nBot " + VERSION
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_PREMIUM, msg)


# notify to all subscribers
def notify_to_subscribers(current_prices, last_prices):
    result = compose_result(current_prices, last_prices)
    msg = "[Hourly]\n" + result + "\nBot " + VERSION
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_SUBSCRIBER, msg)


# compose the actual msg to notify
def compose_result(current_prices, last_prices):
    return "1LN = ${0}\n1BTC = ${1}\n1ETH = ${2}".format(
        get_pair_result(current_prices, last_prices, c.LN_USD),
        get_pair_result(current_prices, last_prices, c.BTC_USD),
        get_pair_result(current_prices, last_prices, c.ETH_USD)
    )


# return the pair in format with the percent changes
def get_pair_result(current, last, key):
    percent_point_changed = 0
    if last and 0 < current[key]:
        percent_point_changed = (current[key] - last[key]) / current[key]
    return "{0} ({1:.2f}%)".format(current[key], percent_point_changed * 100)


# event thresholds for the premium users - i.e., myself :)
def worth_notify(current_prices):
    # BTC Price Min and Max
    worth_btc = current_prices[c.BTC_USD] < 5200  # or 5500 < current_prices[c.BTC_USD]
    # ETH Price Min and Max
    worth_eth = current_prices[c.ETH_USD] < 125  # or 120 < current_prices[c.ETH_USD]
    # LN Price Min and Max
    worth_ln = current_prices[c.LN_USD] < 4.5  # or 6 < current_prices[c.LN_USD]
    return worth_btc or worth_eth or worth_ln


# current_prices[c.DATETIME_UTC] == datetime.utcnow().isoformat()
# ex. '2020-03-22T04:15:48.832863'
def is_o_clock(current_prices):
    return current_prices[c.DATETIME_UTC] == '00'


# ToDos
# 1. History and Statistics :: % change from the last notification
# 2. Dynamic register and deregister of telegram ids (from the bot)
# 3. Add unit tests
# 4. Add integration tests


def main():
    # exit if no receiver
    if not confidentials.TELEGRAM_IDS_SUBSCRIBER:
        logging.error(
            'No Telegram IDs to send the message - Set your confidentials.py (Read README.md)'
        )
        return

    # initialize
    last_event_prices = last_hourly_prices = {}

    # get the last prices and notify
    while True:
        current_prices = bitfront.get_last_prices()
        logging.info(current_prices)  # log to STDOUT

        if is_o_clock(current_prices):
            # hourly notification
            notify_to_subscribers(current_prices, last_hourly_prices)
            last_hourly_prices = current_prices

        if worth_notify(current_prices):
            # event notification
            notify_to_premiums(current_prices, last_event_prices)
            last_event_prices = current_prices
            time.sleep(c.ONE_MIN_IN_SEC)
        else:
            # no notification
            time.sleep(c.TEN_MIN_IN_SEC)


# main
main()

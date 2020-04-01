import confidentials
import time
import logging
import constants as c
import sys
from lib import utils, threshold, notification as notify
from lib import bitfront, upbit, coinbase, gopax

# logging option
logging.basicConfig(level=logging.INFO)


# appending the footer instead of prepending the header
# as only top three lines are displayed on the preview
def get_footer(current, notification_type):
    exchange = current[c.EXCHANGE_NAME].upper()
    return "[" + notification_type.upper() + "] on " + exchange + "\nBot " + c.VERSION


# update if no error
def update_last_price(current, last, exchange):
    if current[exchange] is not c.ERROR_RESPONSE[exchange]:
        last[exchange] = current[exchange]


# ToDo: make the calls concurrent
def all_exchanges():
    return {
        "bitfront": bitfront.get_last_prices(),
        "coinbase": coinbase.get_last_prices(),
        "gopax": gopax.get_last_prices(),
        "upbit": upbit.get_last_prices()
    }

# 1. Make the all_exchanges() calls concurrent
# 2. Make initial values, thresholds, up/down settings as environmental variables


# the very main entry
def main(argv):
    # exit if no receiver
    if not confidentials.TELEGRAM_IDS_SUBSCRIBER:
        logging.error('No Telegram IDs to notify - Set your confidentials.py (Read README.md)')
        return

    # initialize
    last_event_prices = last_hourly_prices = c.INITIAL_PRICES

    # get the last prices and notify
    while True:
        current_prices = all_exchanges()
        logging.info(current_prices)

        # from Bitfront, Coinbase, GoPax and Upbit
        for _, exchange in enumerate(c.EXCHANGE_PAIRS.keys()):
            if utils.is_o_clock():
                # hourly notification
                footer = get_footer(current_prices[exchange], c.HOURLY)
                notify.to_subscribers(current_prices[exchange], last_hourly_prices[exchange], footer)
                update_last_price(current_prices, last_hourly_prices, exchange)

            # by prices and percent changes
            if threshold.worth_notify(current_prices[exchange], last_event_prices[exchange]):
                # event notification
                footer = get_footer(current_prices[exchange], c.EVENT)
                notify.to_premiums(current_prices[exchange], last_event_prices[exchange], footer)
                update_last_price(current_prices, last_event_prices, exchange)

        # check every min
        time.sleep(c.ONE_MIN_IN_SEC)


# main
if __name__ == "__main__":
    main(sys.argv[1:])


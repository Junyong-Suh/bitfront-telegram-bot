import confidentials
import time
import logging
import constants as c
from lib import utils, threshold, bitfront, notification as notify

# logging option
logging.basicConfig(level=logging.INFO)


# appending the footer instead of prepending the header
# as only top three lines are displayed on the preview
def get_footer(current, last):
    footer = "[⏰Hourly⏰]"
    if threshold.worth_by_ds(current, last):
        footer = "[🔥떡상🔥]"
    elif threshold.worth_by_dr(current, last):
        footer = "[⚠️떡락⚠️]"
    elif threshold.worth_notify(current, last):
        footer = "[‼️Event‼️]"
    return "\n" + footer + " Bot " + c.VERSION


# the very main entry
def main():
    # exit if no receiver
    if not confidentials.TELEGRAM_IDS_SUBSCRIBER:
        logging.error('No Telegram IDs to notify - Set your confidentials.py (Read README.md)')
        return

    # initialize
    last_event_prices = last_hourly_prices = {'eth_usd': 124.28, 'btc_usd': 5907.35, 'ln_btc': 0.001081, 'ln_usd': 6.39, 'timestamp_utc': 1584894426.848551, 'datetime_utc': '2020-03-23T01:27:06.848551'}

    # get the last prices and notify
    while True:
        current_prices = bitfront.get_last_prices()
        logging.info(current_prices)  # log to STDOUT

        if utils.is_o_clock(current_prices):
            # hourly notification
            footer = get_footer(current_prices, last_hourly_prices)
            notify.to_subscribers(current_prices, last_hourly_prices, footer)
            last_hourly_prices = current_prices

        # by prices and percent changes
        if threshold.worth_notify(current_prices, last_event_prices):
            # event notification
            footer = get_footer(current_prices, last_event_prices)
            notify.to_premiums(current_prices, last_event_prices, footer)
            last_event_prices = current_prices

        # check every min
        time.sleep(c.ONE_MIN_IN_SEC)


# main
main()

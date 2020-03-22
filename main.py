import bitfront
import confidentials
import notification as notify
import time
import logging
import constants as c
import threshold
import utils

# logging option
logging.basicConfig(level=logging.INFO)


# ToDos
# 1. History and Statistics
# 2. Add/remove Telegram IDs via the bot
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

        if utils.is_o_clock(current_prices):
            # hourly notification
            notify.to_subscribers(current_prices, last_hourly_prices)
            last_hourly_prices = current_prices

        # by prices and percent changes
        if threshold.worth_notify(current_prices, last_event_prices):
            # event notification
            notify.to_premiums(current_prices, last_event_prices)
            last_event_prices = current_prices

        # check every min
        time.sleep(c.ONE_MIN_IN_SEC)


# main
main()

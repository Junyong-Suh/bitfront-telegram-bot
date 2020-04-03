import confidentials
import time
import logging
import constants as c
import sys
from lib import utils, threshold
from lib import formatter as f, notification as notify
from lib import bitfront, upbit, coinbase, gopax

# logging option
logging.basicConfig(level=logging.INFO)


def voila(current_prices, last_prices, is_hourly):
    msg = ""
    has_events_to_notify = False

    # Bitfront, Coinbase, GoPax and Upbit
    for _, exchange in enumerate(c.EXCHANGE_PAIRS.keys()):
        # skip if the exchange response is error
        if current_prices[exchange] is c.ERROR_RESPONSE[exchange]:
            continue

        # compose the msg and update the last price
        if is_hourly:
            msg = msg + f.compose_msg(current_prices[exchange], last_prices[c.HOURLY][exchange])
            last_prices[c.HOURLY][exchange] = current_prices[exchange]
        else:
            # flag if any events
            if threshold.worth_notify(current_prices[exchange], last_prices[c.EVENT][exchange]):
                has_events_to_notify = True
                msg = msg + f.compose_msg(current_prices[exchange], last_prices[c.EVENT][exchange])
            last_prices[c.EVENT][exchange] = current_prices[exchange]

    msg = msg + "Bot " + c.VERSION  # prepend the bot version
    return msg, last_prices, has_events_to_notify


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
def main(argv, is_local=True):
    # exit if no receiver
    if not confidentials.TELEGRAM_IDS_SUBSCRIBER:
        logging.error('No Telegram IDs to notify - Set your confidentials.py (Read README.md)')
        return

    # initialize
    last_prices = {c.HOURLY: c.INITIAL_PRICES, c.EVENT: c.INITIAL_PRICES}

    # get the last prices and notify
    while True:
        is_hourly = utils.is_o_clock()
        current_prices = all_exchanges()
        logging.info(current_prices)

        msg, last_prices, has_events_to_notify = voila(current_prices, last_prices, is_hourly)
        if is_hourly:
            # hourly notification
            notify.to_subscribers(msg)
        elif has_events_to_notify:
            # by prices and percent changes
            notify.to_premiums(msg)
        elif is_local:
            # testing
            notify.to_premiums("[TEST]\n" + msg)

        # check every min
        time.sleep(c.ONE_MIN_IN_SEC)


# main
if __name__ == "__main__":
    if 1 < len(sys.argv) and sys.argv[1] == "production":
        main(sys.argv[2:], False)  # prod
    else:
        main(sys.argv[2:], True)   # local


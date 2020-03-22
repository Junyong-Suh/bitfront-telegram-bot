import bitfront
import confidentials
import telegram
import time
import logging

VERSION = "v1.4.5"  # build & docker version - to be automated
logging.basicConfig(level=logging.INFO)


# As a input to time.sleep() in sec
class PriceCheckInterval:
    @staticmethod
    def one_min():
        return 60  # every min

    @staticmethod
    def ten_min():
        return 600  # every 10 min

    @staticmethod
    def one_hour():
        return 3600  # every hour


def notify_to_premiums(current_prices, last_prices):
    result = compose_result(current_prices, last_prices)
    msg = "WORK HARD MAKE MONEY\n" + result + "\nBot " + VERSION
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_PREMIUM, msg)


def notify_to_subscribers(current_prices, last_prices):
    result = compose_result(current_prices, last_prices)
    msg = "[Hourly]\n" + result + "\nBot " + VERSION
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_SUBSCRIBER, msg)


def compose_result(current_prices, last_prices):
    return "1LN = ${0}\n1BTC = ${1}\n1ETH = ${2}".format(
        get_pair_result(current_prices, last_prices, 'ln_usd'),
        get_pair_result(current_prices, last_prices, 'btc_usd'),
        get_pair_result(current_prices, last_prices, 'eth_usd')
    )


def get_pair_result(current, last, key):
    percent_point_changed = 0
    if last and 0 < current[key]:
        percent_point_changed = (current[key] - last[key]) / current[key]
    return "{0} ({1:.2f}%)".format(current[key], percent_point_changed * 100)


def worth_notify(current_prices):
    # BTC Price Min and Max
    worth_btc = current_prices['btc_usd'] < 5200  # or 5500 < current_prices['btc_usd']
    # ETH Price Min and Max
    worth_eth = current_prices['eth_usd'] < 125  # or 120 < current_prices['eth_usd']
    # LN Price Min and Max
    worth_ln = current_prices['ln_usd'] < 4.5  # or 6 < current_prices['ln_usd']
    return worth_btc or worth_eth or worth_ln


def is_o_clock(current_prices):
    return current_prices['datetime_utc'] == '00'

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
            time.sleep(PriceCheckInterval.one_min())
        else:
            # no notification
            time.sleep(PriceCheckInterval.ten_min())


# main
main()

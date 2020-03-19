import bitfront
import confidentials
import telegram
import time


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


def compose_result(current_prices):
    eth_usd = current_prices['eth_usd']
    btc_usd = current_prices['btc_usd']
    ln_btc = current_prices['ln_btc']
    ln_usd = round(btc_usd * ln_btc, 2)
    return "1LN = ${0} ({1} BTC)\n1BTC = ${2}\n1ETH = ${3}".format(
        str(ln_usd), str(ln_btc), str(btc_usd), str(eth_usd)
    )


def worth_notify(current_prices):
    # BTC Price Min and Max
    worth_btc = current_prices['btc_usd'] < 5250 or 5500 < current_prices['btc_usd']
    # ETH Price Min and Max
    worth_eth = current_prices['eth_usd'] < 105 or 120 < current_prices['eth_usd']
    # LN Price Min and Max
    worth_ln = current_prices['ln_usd'] < 4.5  # or 6 < current_prices['ln_usd']
    return worth_btc or worth_eth or worth_ln


def has_been_an_hour(ts):
    return PriceCheckInterval.one_hour() < time.time() - ts

# ToDos
# 1. History and Statistics :: % change from the last notification
# 2. Dynamic register and deregister of telegram ids (from the bot)
# 3. Add unit tests
# 4. Add integration tests


def main():
    # exit if no receiver
    if not confidentials.TELEGRAM_IDS_SUBSCRIBER:
        print(
            'No Telegram IDs to send the message - Set your ./confidentials.py (Please read README.md)'
        )
        return

    # initialize
    last_hourly_notification_ts = time.time()

    # get the last prices and notify
    while True:
        current_prices = bitfront.get_last_prices()
        print(current_prices)  # log to STDOUT

        if worth_notify(current_prices):
            # event notification
            msg = "WORK HARD MAKE MONEY\n" + compose_result(current_prices)
            telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_PREMIUM, msg)
            time.sleep(PriceCheckInterval.one_min())
        elif has_been_an_hour(last_hourly_notification_ts):
            # hourly notification
            msg = "[Hourly Notification]\n" + compose_result(current_prices)
            telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_SUBSCRIBER, msg)
            last_hourly_notification_ts = time.time()
            time.sleep(PriceCheckInterval.ten_min())
        else:
            # no notification
            time.sleep(PriceCheckInterval.ten_min())


# main
main()

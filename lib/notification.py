import confidentials
import constants as c
from lib import utils, telegram


# notify to premium users (a.k.a. event based, i.e., myself lol)
def to_premiums(current_prices, last_prices):
    result = compose_result(current_prices, last_prices)
    msg = result + "\n[Event] Bot " + c.VERSION
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_PREMIUM, msg)


# notify to all subscribers
def to_subscribers(current_prices, last_prices):
    result = compose_result(current_prices, last_prices)
    msg = result + "\n[Hourly] Bot " + c.VERSION
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_SUBSCRIBER, msg)


def compose_result(current, last):
    result = ""
    for symbol, v in c.PAIRS.items():
        result = result + get_price_in_format(current, last, symbol, v) + "\n"
    return result


# 1LN = $5.25 (+0.14%)
# 1{0} = ${1} ({2:.2f}%)
def get_price_in_format(current, last, symbol, key):
    return "1 {0} = ${1} ({2:+.2f}%)".format(
        symbol,
        current[key],
        utils.percent_changed(current, last, key)
    )
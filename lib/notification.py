import confidentials
import constants as c
from lib import utils, telegram


# notify to premium users (a.k.a. event based, i.e., myself lol)
def to_premiums(current_prices, last_prices, footer=""):
    msg = compose_result(current_prices, last_prices) + footer
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_PREMIUM, msg)


# notify to all subscribers
def to_subscribers(current_prices, last_prices, footer=""):
    msg = compose_result(current_prices, last_prices) + footer
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_SUBSCRIBER, msg)


def compose_result(current, last):
    result = ""
    exchange = current[c.EXCHANGE_NAME]
    for symbol, v in c.EXCHANGE_PAIRS[exchange].items():
        result = result + get_price_in_format(current, last, symbol, v) + "\n"
    return result


# 1LN = $5.25 (+0.14%)
# 1{0} = ${1} ({2:.2f}%)
def get_price_in_format(current, last, coin_symbol, key):
    currency_symbol = '$'
    str_format = "1 {0} = {1}{2:,.2f} ({3:+.2f}%)"
    if "krw" in key:
        currency_symbol = '₩'
        str_format = "1 {0} = {1}{2:,.0f} ({3:+.2f}%)"

    return str_format.format(
        coin_symbol,
        currency_symbol,
        current[key],
        utils.percent_changed(current, last, key)
    )
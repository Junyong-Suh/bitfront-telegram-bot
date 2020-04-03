import constants as c
from lib import utils


# appending the footer instead of prepending the header
# as only top three lines are displayed on the preview
def get_footer(current):
    return "[" + current[c.EXCHANGE_NAME].upper() + "]\n"


def compose_msg(current, last):
    return get_result(current, last) + get_footer(current)


def get_result(current, last):
    result = ""
    exchange = current[c.EXCHANGE_NAME]
    for symbol, v in c.EXCHANGE_PAIRS[exchange].items():
        result = result + get_price_in_format(current, last, symbol, v) + "\n"
    return result


# 1LN = $5.25 (+0.14%)
# 1{0} = ${1} ({2:.2f}%)
def get_price_in_format(current, last, coin_symbol, key):
    currency_symbol = "$"
    str_format = "1 {0} = {1}{2:,.2f} ({3:+.2f}%)"
    if "krw" in key:
        currency_symbol = "₩"
        str_format = "1 {0} = {1}{2:,.0f} ({3:+.2f}%)"

    return str_format.format(
        coin_symbol,
        currency_symbol,
        current[key],
        utils.percent_changed(current, last, key)
    )
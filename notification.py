import telegram
import confidentials
import constants as c


# notify to premium users (a.k.a. event based, i.e., myself lol)
def to_premiums(current_prices, last_prices):
    result = compose_result(current_prices, last_prices)
    msg = "WORK HARD MAKE MONEY\n" + result + "\nBot " + c.VERSION
    telegram.notify_on_telegram(confidentials.TELEGRAM_IDS_PREMIUM, msg)


# notify to all subscribers
def to_subscribers(current_prices, last_prices):
    result = compose_result(current_prices, last_prices)
    msg = "[Hourly]\n" + result + "\nBot " + c.VERSION
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

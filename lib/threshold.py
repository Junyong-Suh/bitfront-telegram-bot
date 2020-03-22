import constants as c
from lib import utils

ABSOLUTE_PERCENT_CHANGE = 10


# event thresholds for the premium users - i.e., myself :)
def worth_notify(current, last):
    return worth_downwards(current) or worth_by_changes(current, last)
    # return worth_upwards(current) or worth_by_changes(current, last)
    # return worth_downwards(current) or worth_upwards(current) or worth_by_changes(current, last)


# BTC, ETH, LN lower bound
def worth_downwards(current):
    btc_by_price = current[c.BTC_USD] < 5200
    eth_by_price = current[c.ETH_USD] < 125
    ln_by_price = current[c.LN_USD] < 4.5
    return btc_by_price or eth_by_price or ln_by_price


# BTC, ETH, LN upper bound
def worth_upwards(current):
    btc_by_price = 6000 < current[c.BTC_USD]
    eth_by_price = 200 < current[c.ETH_USD]
    ln_by_price = 6 < current[c.LN_USD]
    return btc_by_price or eth_by_price or ln_by_price


# by absolute percent changes (either + or -)
def worth_by_changes(current, last):
    btc_by_change = ABSOLUTE_PERCENT_CHANGE < utils.percent_changed(current, last, c.BTC_USD)
    eth_by_change = ABSOLUTE_PERCENT_CHANGE < utils.percent_changed(current, last, c.ETH_USD)
    ln_by_change = ABSOLUTE_PERCENT_CHANGE < utils.percent_changed(current, last, c.LN_USD)
    return btc_by_change or eth_by_change or ln_by_change

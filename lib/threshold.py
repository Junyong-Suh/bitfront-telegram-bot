import constants as c
from lib import utils

ABSOLUTE_PERCENT_CHANGE = 10


# event thresholds for the premium users - i.e., myself :)
def worth_notify(current, last):
    worth = False
    exchange = current[c.EXCHANGE_NAME]
    for pair in c.EXCHANGE_PAIRS[exchange].values():
        # worth = worth or worth_downwards(current, pair) or worth_by_changes(current, last, pair)
        # worth = worth or worth_upwards(current, pair) or worth_by_changes(current, last, pair)
        worth = worth or worth_by_values(current, pair) or worth_by_changes(current, last, pair)
    return worth


# by either upper or lower bounds
def worth_by_values(current, pair):
    return worth_downwards(current, pair) or worth_upwards(current, pair)


# lower bounds
def worth_downwards(current, pair):
    lower_bound = c.THRESHOLDS[c.LOWER_BOUND][pair]
    return current[pair] < lower_bound


# upper bounds
def worth_upwards(current, pair):
    upper_bound = c.THRESHOLDS[c.UPPER_BOUND][pair]
    return upper_bound < current[pair]


# by absolute percent changes (either + or -)
def worth_by_changes(current, last, pair):
    return worth_by_ds(current, last, pair) or worth_by_dr(current, last, pair)


# ds stands for 떡상 (+)
def worth_by_ds(current, last, pair):
    changed = utils.percent_changed(current, last, pair)
    return ABSOLUTE_PERCENT_CHANGE < changed


# dr stands for 떡락 (-)
def worth_by_dr(current, last, pair):
    changed = utils.percent_changed(current, last, pair)
    return changed < -ABSOLUTE_PERCENT_CHANGE

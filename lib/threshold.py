import constants as c
import config
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


# lower bounds, but not zero (error or end of the world)
def worth_downwards(current, pair):
    lower_bound = config.THRESHOLDS[c.LOWER_BOUND][pair]
    return 0 < current[pair] < lower_bound


# upper bounds
def worth_upwards(current, pair):
    upper_bound = config.THRESHOLDS[c.UPPER_BOUND][pair]
    return upper_bound < current[pair]


# by absolute percent changes (either + or -)
def worth_by_changes(current, last, pair):
    return worth_by_ds(current, last, pair) or worth_by_dr(current, last, pair)


# ds stands for 떡상 (+), exact 100% change is considered an error (from zero values)
def worth_by_ds(current, last, pair):
    changed = utils.percent_changed(current, last, pair)
    return ABSOLUTE_PERCENT_CHANGE < changed != 100


# dr stands for 떡락 (-), exact -100% change is considered an error (from zero values)
def worth_by_dr(current, last, pair):
    changed = utils.percent_changed(current, last, pair)
    return -100 != changed < -ABSOLUTE_PERCENT_CHANGE

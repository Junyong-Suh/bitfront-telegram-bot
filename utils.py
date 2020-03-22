import constants as c


# current_prices[c.DATETIME_UTC] == datetime.utcnow().isoformat()
# ex. '2020-03-22T04:15:48.832863'
def is_o_clock(current_prices):
    return current_prices[c.DATETIME_UTC][14:16] == '00'


# end of the world if any price becomes zero
def percent_changed(current, last, key):
    changed = 0
    if last and 0 < current[key]:
        changed = (current[key] - last[key]) / current[key]
    return changed * 100

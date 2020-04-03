from datetime import datetime


# datetime.utcnow().isoformat() == "2020-03-22T04:15:48.832863"
def is_o_clock():
    return datetime.utcnow().isoformat()[14:16] == "00"


# end of the world if any price becomes zero
def percent_changed(current, last, pair):
    changed = 0
    if last and 0 < current[pair]:
        changed = (current[pair] - last[pair]) / current[pair]
    return changed * 100

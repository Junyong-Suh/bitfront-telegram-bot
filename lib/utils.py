from datetime import datetime


# datetime.utcnow().isoformat() == "2020-03-22T04:15:48.832863"
def true_every_3_hours():
    hour = datetime.utcnow().isoformat()[11:13]
    minute = datetime.utcnow().isoformat()[14:16]
    return minute == "00" and int(hour) % 3 == 0


# end of the world if any price becomes zero
def percent_changed(current, last, pair):
    changed = 0
    if last and 0 < current[pair]:
        changed = (current[pair] - last[pair]) / current[pair]
    return changed * 100

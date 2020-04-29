import config
from lib import telegram


# notify to premium users (a.k.a. event based, i.e., myself lol)
def to_premiums(msg):
    telegram.notify_on_telegram(config.TELEGRAM_IDS_PREMIUM, msg)


# notify to all subscribers
def to_subscribers(msg):
    telegram.notify_on_telegram(config.TELEGRAM_IDS_SUBSCRIBER, msg)

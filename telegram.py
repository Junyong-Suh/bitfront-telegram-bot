import requests
import confidentials
import logging


# the bot info
def get_me(bot_id):
    r = requests.get("https://api.telegram.org/bot" + bot_id + "/getMe")
    return r.json()


# notify to all receivers on Telegram
def notify_on_telegram(telegram_ids, msg):
    for tid in telegram_ids:
        notify_telegram(confidentials.FOREIGN_WORKER_BOT_ID, tid, msg)


# notify to Telegram chat
def notify_telegram(bot_id, chat_id, msg):
    r = requests.post(
        url="https://api.telegram.org/bot" + bot_id + "/sendMessage",
        json={"chat_id": chat_id, "text": msg}
    )
    logging.info(r.json())

import requests
import confidentials


# the bot info
def get_me(bot_id):
    r = requests.get("https://api.telegram.org/bot" + bot_id + "/getMe")
    return r.json()


# notify to all receivers on Telegram
def notify_all_on_telegram(msg, to_premium_users=False):
    if to_premium_users:
        for tid in confidentials.TELEGRAM_IDS_PREMIUM:
            notify_telegram(confidentials.FOREIGN_WORKER_BOT_ID, tid, msg)
    else:
        for tid in confidentials.TELEGRAM_IDS_SUBSCRIBER:
            notify_telegram(confidentials.FOREIGN_WORKER_BOT_ID, tid, msg)


# notify to Telegram chat
def notify_telegram(bot_id, chat_id, msg):
    r = requests.post(
        url="https://api.telegram.org/bot" + bot_id + "/sendMessage",
        json={"chat_id": chat_id, "text": msg}
    )
    print(r.json())

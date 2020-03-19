import requests
import confidentials

# the bot info
def getMe(bot_id):
    r = requests.get("https://api.telegram.org/bot"+ bot_id +"/getMe")
    return r.json()

# notify to all receivers on Telegram
def notifyAllOnTelegram(msg, toPremiumUsers=False):
    if toPremiumUsers:
        for id in confidentials.TELEGRAM_IDS_PREMIUM:
            notifyTelegram(confidentials.FOREIGN_WORKER_BOT_ID, id, msg)
    else:
        for id in confidentials.TELEGRAM_IDS_SUBSCRIBER:
            notifyTelegram(confidentials.FOREIGN_WORKER_BOT_ID, id, msg)

# notify to Telegram chat
def notifyTelegram(bot_id, chat_id, msg):
    r = requests.post(
        url="https://api.telegram.org/bot"+bot_id+"/sendMessage",
        json={"chat_id": chat_id, "text": msg}
    )
    print(r.json())

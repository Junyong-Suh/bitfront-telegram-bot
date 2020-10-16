import requests
import confidentials
import constants as c
from lib import logger


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
    try:
        r = requests.post(
            url="https://api.telegram.org/bot" + bot_id + "/sendMessage",
            json={"chat_id": chat_id, "text": msg}
        )
        logger.info(r.json())
    except requests.exceptions.HTTPError as e:
        logger.error({c.ES_LOG: str(e)})
    except requests.exceptions.ConnectionError as e:
        logger.error({c.ES_LOG: str(e)})
    except requests.exceptions.Timeout as e:
        logger.error({c.ES_LOG: str(e)})
    except requests.exceptions.RequestException as e:
        logger.error({c.ES_LOG: str(e)})

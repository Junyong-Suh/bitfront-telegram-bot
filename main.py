import requests
import confidentials

def getMe(bot_id):
    r = requests.get("https://api.telegram.org/bot"+ bot_id +"/getMe")
    return r.json()

def notifyTelegram(bot_id, chat_id, msg):
    r = requests.post(
        url="https://api.telegram.org/bot"+bot_id+"/sendMessage",
        json={"chat_id": chat_id, "text": msg}
    )
    # print(r.json())

def getCoinPair(ticker1, ticker2):
    r = requests.get("https://openapi.bitfront.me/v1/market/public/currentTickValue?coinPair="+ ticker1 +"."+ ticker2 +"")
    return r.json()

def composeResult():
    r = getCoinPair("ETH", "USD")
    eth_usd = r['responseData']['last']
    r = getCoinPair("BTC", "USD")
    btc_usd = r['responseData']['last']
    r = getCoinPair("LN", "BTC")
    ln_btc = r['responseData']['last']
    ln_usd = round(btc_usd * ln_btc, 2)
    return "1LN = $"+ str(ln_usd) +" ("+ str(ln_btc) + " BTC)" + "\n1BTC = $"+ str(btc_usd) + "\n1ETH = $"+ str(eth_usd)

# ToDos
# 1. History and Statistics :: % change from the last notification
# 2. Periodic Job (Lambda if no % change required)
# 3. Dynamic Lower and High Prices settings ($4 or less LN & $6 or higher LN)
# 4. Dynamic on and off

notifyTelegram(
    confidentials.FOREIGN_WORKER_BOT_ID,
    confidentials.FOREIGN_WORKER_TELEGRAM_ID,
    "WORK HARD MAKE MONEY\n" + composeResult()
)

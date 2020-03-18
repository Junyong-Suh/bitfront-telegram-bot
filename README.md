# bitfront-telegram-bot

A simple Python script to notify price alerts from [Bitfront](https://www.bitfront.me/) on Telegram by a [bot](https://t.me/bitfront_price_bot)

## Requirements

* Works on both Python 2.7.17+ and Python 3.6.9+
* The only dependency: [requests](https://requests.readthedocs.io/en/master/)

## Quick Start

### Install Python

```
brew install python3 # either python or python3
```

### Clone the Code

```
git clone git@github.com:Junyong-Suh/bitfront-telegram-bot.git
```

### Install Dependencies

```
cd bitfront-telegram-bot
pip3 install -r requirements.txt # either pip or pip3
```

### Get Your Credentials

Update your credentials to [`credentials.py`](https://github.com/Junyong-Suh/bitfront-telegram-bot/blob/master/confidentials.py)

* How to get your own Telegram Bot and the ID: [https://core.telegram.org/bots](https://core.telegram.org/bots)

* How to get your Telegram ID: [https://support.bigone.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-](https://support.bigone.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-)

### Run the Script

```
python3 main.py
```
You will get the message from the bot.

## References
* [https://core.telegram.org/bots/api#making-requests](https://core.telegram.org/bots/api#making-requests)
* [https://core.telegram.org/bots/api#message](https://core.telegram.org/bots/api#message)
* [https://github.com/bitfront-exchange/bitfront-api-docs](https://github.com/bitfront-exchange/bitfront-api-docs)
* [https://bitfront-exchange.github.io/bitfront-api-docs/#/api/market/v1-market-public-currentTickValue-get](https://bitfront-exchange.github.io/bitfront-api-docs/#/api/market/v1-market-public-currentTickValue-get)

## Contributions

Please make an issue and a PR :-)

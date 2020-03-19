# bitfront-telegram-bot

A simple Python script to notify price alerts from [Bitfront](https://www.bitfront.me/) on Telegram by a [bot](https://t.me/bitfront_price_bot)

## Requirements

* Requires Python 3.7.4+
* The only dependency: [requests](https://requests.readthedocs.io/en/master/)

## Quick Start

### Clone the Code

```
$ git clone git@github.com:Junyong-Suh/bitfront-telegram-bot.git
```

### Install Dependencies

```
$ python --version
Python 3.7.7
$ cd bitfront-telegram-bot
$ pip3 install -r requirements.txt
```

### Set Your Credentials

Rename `credentials_empty.py` to `credentials.py` and set your credentials

* How to get your own Telegram Bot and the ID: [https://core.telegram.org/bots](https://core.telegram.org/bots)

* How to get your Telegram ID: [https://support.bigone.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-](https://support.bigone.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-)

(Optional) Once you update your credentials, make Git not to track the file

```
# untrack
$ git update-index --assume-unchanged confidentials.py

# track again
# git update-index --no-assume-unchanged confidentials.py
```

### Subscribe to Your Bot

Turn on your Telegram App, find your bot and add.

### Run the Script

```
python main.py
```
You will get messages from the bot

## Docker

Assume that you set the credentials and subscribed to your bot. 

* Build the image

```
docker build -t bitfront-price-alert .
```

* Run 

```
docker run bitfront-price-alert:latest
```

## References
* [https://core.telegram.org/bots/api#making-requests](https://core.telegram.org/bots/api#making-requests)
* [https://core.telegram.org/bots/api#message](https://core.telegram.org/bots/api#message)
* [https://github.com/bitfront-exchange/bitfront-api-docs](https://github.com/bitfront-exchange/bitfront-api-docs)
* [https://bitfront-exchange.github.io/bitfront-api-docs/#/api/market/v1-market-public-currentTickValue-get](https://bitfront-exchange.github.io/bitfront-api-docs/#/api/market/v1-market-public-currentTickValue-get)

## Contributions

Please make an issue and a PR :-)

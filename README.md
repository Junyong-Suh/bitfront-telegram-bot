# bitfront-telegram-bot

A simple Python script to notify price alerts from [Bitfront](https://www.bitfront.me/) on Telegram by a [bot](https://t.me/bitfront_price_bot)

## Requirements

* Requires Python 3.8.2+
* Dependency: [requests](https://requests.readthedocs.io/en/master/)

## Quick Start

### Clone the Code

```
$ git clone git@github.com:Junyong-Suh/bitfront-telegram-bot.git
```

### Setup Virtual Environment

Install `pip` and `virtualenv`

```bash
// install pip
$ curl https://bootstrap.pypa.io/get-pip.py > getpip.py
$ sudo python getpip.py

// install virtualenv
$ sudo pip install virtualenv
```

### Install Dependencies

```bash
$ cd bitfront-telegram-bot
$ virtualenv -p python3.8.2 .venv
$ source .venv/bin/activate
$ python3 --version
Python 3.8.2
$ pip3 install -r requirements.txt
```

### Set Your Credentials

Rename `credentials_empty.py` to `credentials.py` and set your credentials

* How to get your own Telegram Bot and the ID: [https://core.telegram.org/bots](https://core.telegram.org/bots)

Add your Telegram ID(s) to `constants.py`

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
python3 main.py
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
or
```
docker run -d -e FOREIGN_WORKER_BOT_ID={NUMBER}:{KEY} bitfront-price-alert:latest
```

## References
* [https://core.telegram.org/bots/api#making-requests](https://core.telegram.org/bots/api#making-requests)
* [https://core.telegram.org/bots/api#message](https://core.telegram.org/bots/api#message)
* [https://github.com/bitfront-exchange/bitfront-api-docs](https://github.com/bitfront-exchange/bitfront-api-docs)
* [https://bitfront-exchange.github.io/bitfront-api-docs/#/api/market/v1-market-public-currentTickValue-get](https://bitfront-exchange.github.io/bitfront-api-docs/#/api/market/v1-market-public-currentTickValue-get)

## Contributions

Please make an issue and a PR :-)

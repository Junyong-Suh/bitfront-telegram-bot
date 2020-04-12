import requests
import constants as c
import logging


# ToDo: make the call fire and forget - not to block
def to_es(index, payload):
    try:
        r = requests.post(c.ES_HOST + index + "/_doc", json=payload)
        r.raise_for_status()
        logging.debug(r.text)
    except requests.exceptions.HTTPError as e:
        logging.debug(e)
    except requests.exceptions.ConnectionError as e:
        logging.debug(e)
    except requests.exceptions.Timeout as e:
        logging.debug(e)
    except requests.exceptions.RequestException as e:
        logging.debug(e)

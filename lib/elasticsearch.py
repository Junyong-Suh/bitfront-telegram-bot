import requests
import constants as c
import logging


def to_es(index, payload):
    r = requests.post(c.ES_HOST + index + "/_doc", json=payload)
    logging.debug(r.text)


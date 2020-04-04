import requests
import constants as c
import logging


# ToDo: make the call fire and forget - not to block
def to_es(index, payload):
    r = requests.post(c.ES_HOST + index + "/_doc", json=payload)
    logging.debug(r.text)


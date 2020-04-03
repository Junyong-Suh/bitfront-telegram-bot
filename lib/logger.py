import logging
from datetime import datetime
import constants as c
from lib import elasticsearch as es

# logging option
logging.basicConfig(level=logging.INFO)


# debug only goes to STDOUT
def debug(msg):
    logging.debug(msg)


def info(msg):
    logging.info(msg)
    to_es(msg, c.LOG_INFO)


def error(msg):
    logging.error(msg)
    to_es(msg, c.LOG_ERROR)


def warning(msg):
    logging.warning(msg)
    to_es(msg, c.LOG_WARNING)


def to_es(msg, level=c.LOG_INFO):
    utc_now = datetime.utcnow()
    datetime_utc = utc_now.isoformat()
    payload = {
        c.ES_LOG_LEVEL: level,
        c.ES_MSG: msg,
        c.TIMESTAMP_UTC: datetime.timestamp(utc_now),
        c.DATETIME_UTC: datetime_utc
    }
    es.to_es(c.ES_INDEX_LOGS, payload)

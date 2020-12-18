import requests
import constants as c
from lib import logger


# return the quote from given url
def get_quote(quote_url, fallback_response, timeout=3):
    try:
        r = requests.get(quote_url, timeout=timeout)
        r.raise_for_status()
        logger.info(f"r.status_code: {r.status_code}, r.json(): {r.json()}")
    except requests.exceptions.HTTPError as e:
        logger.error({c.ES_LOG: str(e)})
    except requests.exceptions.ConnectionError as e:
        logger.error({c.ES_LOG: str(e)})
    except requests.exceptions.Timeout as e:
        logger.error({c.ES_LOG: str(e)})
    except requests.exceptions.RequestException as e:
        logger.error({c.ES_LOG: str(e)})
    except requests.exceptions as e:
        logger.error({c.ES_LOG: str(e)})

    if r.status_code == 200:
        return r.json()
    else:
        return fallback_response

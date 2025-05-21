import logging
import requests
from langdetect import detect, LangDetectException
from logger import logger
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type



@retry(
    stop=stop_after_attempt(3), 
    wait=wait_exponential(multiplier=2, min=2, max=10), 
    retry=retry_if_exception_type(requests.RequestException),
    reraise=True 
)
def is_feed_accessible(url):
    try:
        response = requests.head(url, timeout=15, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException as e:
        logger.warning(f"Retrying access to feed {url} due to: {e}")
        raise  # Raise again so `tenacity` catches it

def detect_language(text):
    try:
        return detect(text)
    except LangDetectException:
        logger.exception(f"Failed to get langauge of the text: {text}")
        return "unknown"

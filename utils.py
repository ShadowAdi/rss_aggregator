import logging
import requests
from langdetect import detect, LangDetectException
from logger import logger


def is_feed_accessible(url):
    try:
        response = requests.head(url, timeout=15, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException as e:
        logger.exception(f"Failed to access feed {url}: {e}")
        return False


def detect_language(text):
    try:
        return detect(text)
    except LangDetectException:
        logger.exception(f"Failed to get langauge of the text: {text}")
        return "unknown"

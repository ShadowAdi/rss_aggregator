import json
import logging
from logger import logger


def Json_Saver(all_articles):
    try:
        with open("news.json", "w", encoding="utf-8") as f:
            json.dump(all_articles, f, ensure_ascii=False, indent=4)
        logger.info("Saved articles to news.json")
    except Exception as e:
        logger.exception(f"Error writing to JSON file: {e}")

import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("rss_logger")
logger.setLevel(logging.DEBUG)  # Capture everything

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

info_handler = logging.FileHandler("logs/info.log")
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

error_handler = logging.FileHandler("logs/error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(console_handler)

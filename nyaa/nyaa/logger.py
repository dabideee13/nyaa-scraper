import logging
import sys

# Log configurations
LOG_FORMAT = (
    "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s"
)
LOG_FORMATTER = logging.Formatter(
    LOG_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S"
)
LOG_FILE = "main.log"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(LOG_FORMATTER)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(LOG_FORMATTER)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

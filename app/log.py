import logging
import sys
import time

import coloredlogs

from app.config import BaseConfig

# this format allows clickable link to code source in PyCharm
_log_format = (
    "%(asctime)s - %(name)s - %(levelname)s - %(process)d - "
    '"%(pathname)s:%(lineno)d" - %(funcName)s() - %(message_id)s - %(message)s'
)
_log_formatter = logging.Formatter(_log_format)


def _get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(_log_formatter)
    console_handler.formatter.converter = time.gmtime()

    return console_handler


def _get_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(_get_console_handler())

    logger.propagate = False

    if BaseConfig.COLOR_LOG:
        coloredlogs.install(level="DEBUG", logger=logger, fmt=_log_format)

    return logger


print(">>> init logging <<<")

# Disable flask logs
log = logging.getLogger("werkzeug")
log.disabled = True

logging.Logger.d = logging.Logger.debug
logging.Logger.i = logging.Logger.info
logging.Logger.w = logging.Logger.warning
logging.Logger.e = logging.Logger.error
logging.Logger.c = logging.Logger.critical

LOG = _get_logger("SL")

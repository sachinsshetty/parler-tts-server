import logging
import logging.config
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logger = logging.getLogger("parler_tts_server")

# https://www.youtube.com/watch?v=9L77QExPmI0
# https://docs.python.org/3/library/logging.config.html
logging_config = {
    "version": 1,  # required
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "root": {
            "level": LOG_LEVEL,
            "handlers": ["stdout"],
        },
    },
}


logging.config.dictConfig(logging_config)
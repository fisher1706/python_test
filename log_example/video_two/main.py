from repository.db import get_data
from repository.file import load_config


import logging
import logging.handlers
import logging.config


def password_filter(log: logging.LogRecord) -> int:
    if "password" in str(log.msg):
        return 0
    else:
        return 1


# noinspection PyTypeChecker
def init_logger(name):
    logger = logging.getLogger(name)
    my_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(my_format))
    sh.setLevel(logging.DEBUG)
    sh.addFilter(password_filter)
    # fh = logging.FileHandler(filename="logs/test.log")
    fh = logging.handlers.RotatingFileHandler(filename="logs/test.log")
    fh.setFormatter(logging.Formatter(my_format))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug("logger was initialized")


def get_logging_git_config():
    return {
        'version': 1,
        'formatters': {
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "std": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "detailed",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "detailed",
                "filename": "logs/test.log",
            }
        },
        "loggers": {
            "app": {
                "handlers": ["std", "file"],
                "level": "DEBUG",
            }
        }
    }


init_logger("app") # config log from python code
# logging.config.dictConfig(get_logging_git_config()) # config log from dict
my_logger = logging.getLogger("app.main")


def make_work():
    conf = load_config()
    if conf:
        my_logger.debug(conf)
        try:
            db_data = get_data(conf)
            my_logger.debug(db_data)
        except ConnectionError as err:
            # my_logger.error(err)
            my_logger.exception(err)


if __name__ == "__main__":
    my_logger.info("Starting service ... ")
    make_work()
    my_logger.info("Stopping service ... ")

import logging
from pprint import pprint


class MyFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        print("my_filter")
        pprint(record.__dict__)
        return True


class InfoFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.levelno == 20:
            return True


class WarningFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.levelno == 30:
            return True


logger_conf = {
    "version": 1,
    "formatters": {
        "console_msg": {
            "format": "{levelname} - {message} - {filename} - {funcName} - {lineno}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "console_msg",
        },
        "file_info": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "console_msg",
            "filename": "my_info_log.log",
            "filters": ["info_filter"],
        },
        "file_warning": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "console_msg",
            "filename": "my_warning_log.log",
            "filters": ["warning_filter"],
        },
    },
    "filters": {
        "my_filter": {"()": MyFilter},
        "info_filter": {"()": InfoFilter},
        "warning_filter": {"()": WarningFilter},
    },
    "loggers": {
        "my_python_logger": {
            "level": "INFO",
            "handlers": ["console", "file_info", "file_warning"],
            "filters": ["my_filter"],
        }
    },
}

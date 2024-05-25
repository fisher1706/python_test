import logging.config
from my_config import logger_conf

logging.config.dictConfig(logger_conf)
logger = logging.getLogger("my_python_logger")


def main():
    logger.info("message info")
    logger.warning("message warning")
    status = 404
    logger.error("message error", extra={"status_code": status})

    try:
        print(10/0)
        logger.error("message error", extra={"status_code": status})
    except Exception as e:
        print(e)
        logger.exception(e)
    print("Hello world")


if __name__ == '__main__':
    print(f"logger: {logger}")
    print(f"handlers: {logger.handlers}")
    print("*" * 200)

    main()

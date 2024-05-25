import logging.config
from settings import logger_config


logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')

worlds = ['new house', 'apple', 'ice cream', 3]


def main():
    for item in worlds:
        try:
            print(item.split(' '))
        except Exception as e:
            # logger.debug(f'Exception here, item = {item}', exc_info=True)
            logger.exception(f'Exception here, item = {item}, exception = {e}')


if __name__ == '__main__':
    main()

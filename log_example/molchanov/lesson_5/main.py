import logging.config
from settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def new_function():
    name = 'oleg'
    logger.debug('Enter in to the new_function()', extra={'oleg_name': name})


def main():
    logger.debug('Enter in to the main()')


if __name__ == '__main__':
    main()
    new_function()

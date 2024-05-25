# https://www.youtube.com/watch?v=qqdgynJ5ATU

import logging
import requests

logging.basicConfig(level='DEBUG', filename='my_log.log')
logger = logging.getLogger()
# logger.setLevel('DEBUG') # loggin.DEBUF
logging.getLogger('urllib3').setLevel('CRITICAL')

for key in logging.Logger.manager.loggerDict:
    print(key)


print(dir(logger))
print(logger)
print(logger.level)
print(logger.handlers)


def main(name):
    logger.warning(f'Enter the main() function: name = {name}')
    logger.debug(f'Enter the main() function: name = {name}')

    r = requests.get('https://www.google.com')
    print(r)


if __name__ == '__main__':
    main('oleg')

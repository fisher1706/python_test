import logging

# logging.basicConfig()
# logger = logging.getLogger()
# print(logger)


app_logger = logging.getLogger("app_logger")

console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)

f = logging.Formatter(fmt="%(levelname)s - %(name)s - %(message)s")
console_handler.setFormatter(f)

# print(app_logger)
# print(app_logger.parent)
# print(app_logger.handlers)

# print('Root handlers', app_logger.parent.handlers)

utils_logger = logging.getLogger("app_logger.utils")
utils_logger.setLevel("DEBUG")
# utils_logger.propagate = False

# print(utils_logger)
# print(utils_logger.parent)
# print(utils_logger.handlers)


def main():
    utils_logger.debug("Hello world")


if __name__ == "__main__":
    main()

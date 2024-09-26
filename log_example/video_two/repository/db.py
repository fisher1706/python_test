import logging

logger = logging.getLogger("app.repository.db")


def create_connection(conf):
    print(f"conf: {conf}")
    logger.debug("Creating connection")
    raise ConnectionError("DB not found")


def close_connection():
    logger.debug("Closing connection")


def get_data(conf):
    create_connection(conf)
    close_connection()
    return [(1, 114, "test_1"), (2, 2015, "test_2")]

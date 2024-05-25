import logging


logger = logging.getLogger("app.repository.file")


def load_config():
    logger.info("Loading configuration from file")
    return {
        "bd_name": "test_db",
        "user_name": "admin",
        "password": "ZapelFisher",
    }

"""
Singleton pattern
Example of a logger class that is a singleton.
It is used to log messages to a file.
The file is opened only once and is closed when the logger is deleted.
The logger is used to log messages to a file.
The logger is used to log messages to a file.

Is kind of an anti-pattern inside Python development because all the modules
in Python are built as singletons.
"""

import logging

logging.basicConfig(level=logging.INFO)


class Logger:
    """ Logger class """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
        return cls._instance

    def __del__(self):
        self.logger.close()

    def log(self, message):
        self.logger.log(message)


if __name__ == "__main__":
    logger = Logger()
    logger.log(logging.INFO, "This is a test message")
    logger.log(logging.INFO, "This is another test message")
    logger.log(logging.INFO, "This is a third test message")
    logger.log(logging.ERROR, "This is an error message")
    logger.log(logging.WARNING, "This is a warning message")
    logger.log(logging.CRITICAL, "This is a critical message")
    logger.log(logging.DEBUG, "This is a debug message")
    logger.log(logging.NOTSET, "This is a notset message")
    logger.log(logging.INFO, "This is a test message")
    logger.log(logging.INFO, "This is another test message")
    logger.log(logging.INFO, "This is a third test message")
    logger.log(logging.ERROR, "This is an error message")
    logger.log(logging.WARNING, "This is a warning message")
    logger.log(logging.CRITICAL, "This is a critical message")
    logger.log(logging.DEBUG, "This is a debug message")
    logger.log(logging.NOTSET, "This is a notset message")

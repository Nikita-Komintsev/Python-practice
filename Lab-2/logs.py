import logging


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._init_logger()
        return cls._instance

    def _init_logger(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        log_file = "Logs.log"
        file_handler = logging.FileHandler(log_file)

        formatter = logging.Formatter("[%(levelname)s] %(asctime)s: %(message)s", "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":
    logger = Logger()
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

    logger2 = Logger()
    logger2.warning("This is a warning message for logger2")

    print(id(logger))
    print(id(logger2))

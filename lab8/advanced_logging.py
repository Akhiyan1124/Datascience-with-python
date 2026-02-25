import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("AdvancedLogger")
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler("app.log", maxBytes=1000000, backupCount=3)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logger.addHandler(handler)

def run():
    logger.debug("Debug message")
    logger.info("Info message")
    logger.error("Error message")

if __name__ == "__main__":
    run()

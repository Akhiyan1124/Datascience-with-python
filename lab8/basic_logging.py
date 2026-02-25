import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("application.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def test_logging():
    logger.info("Application started")
    logger.warning("This is a warning")
    logger.error("This is an error")

if __name__ == "__main__":
    test_logging()

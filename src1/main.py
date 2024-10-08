# src/main.py
import logging
import sys

from data_processing.processor import process_data
from model_training.trainer import train

# instantiate logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# define handler and formatter
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

# add formatter to handler
handler.setFormatter(formatter)

# add handler to root logger
root_logger.addHandler(handler)

# Get logger for this module
logger = logging.getLogger(__name__)

def main_process_data():
    """Dummy data processing function"""
    logger.info("Main Pre-processing data")
    # data preprocessing code here...
    logger.info("Main Data pre-processing complete")

if __name__ == "__main__":
    logger.info("Program started")
    process_data()
    train()
    main_process_data()
    logger.warning("Program warning log test")
    logger.info("Program finished")
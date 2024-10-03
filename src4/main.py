"""Entry point"""
import logging
import logging.config
import os
import json
from datetime import datetime

from data_processing.processor import process_data
from model_training.trainer import train

# find .env file in parent directory
from dotenv import find_dotenv, load_dotenv
env_file = find_dotenv()
load_dotenv()

PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
DATETIME = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_ENV = os.environ["ENV"]
LOG_DIR = "./logs"
CONFIG_DIR = "./config"


def setup_logging():
    """Load logging configuration"""
    log_configs = {
        "dev": "logging.dev.json", 
        "prod": "logging.prod.json"
        }
    log_config = log_configs.get(LOG_ENV, "logging.dev.json")
    log_config_path = os.path.join(PARENT_DIR, CONFIG_DIR, log_config)
    log_file_path = os.path.join(PARENT_DIR, LOG_DIR, f'pyapicapi_{DATETIME}.log')

    with open(log_config_path, 'r') as f:
        config = json.load(f)

    # Update the file handler's filename
    for handler in config['handlers'].values():
        if handler['class'] == 'logging.FileHandler':
            handler['filename'] = log_file_path

    logging.config.dictConfig(config)
    

def main_process_data():
    """Dummy data processing function"""
    logger.info("Main Pre-processing data")
    # data preprocessing code here...
    logger.info("Main Data pre-processing complete")

if __name__ == "__main__":

    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Program started")
    process_data()
    train()
    main_process_data()
    logger.warning("Program warning log test")
    logger.info("Program finished")

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

CONFIG_DIR = "./config"
LOG_DIR = "./logs"


def setup_logging():
    """Load logging configuration"""
    log_configs = {
        "dev": "logging.dev.json", 
        "prod": "logging.prod.json"
        }
    config = log_configs.get(os.environ["ENV"], "logging.dev.json")
    config_path = "/".join([CONFIG_DIR, config])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"{LOG_DIR}/{timestamp}.log"

    with open(config_path, 'r') as f:
        config = json.load(f)

    # Update the file handler's filename
    for handler in config['handlers'].values():
        if handler['class'] == 'logging.FileHandler':
            handler['filename'] = log_file

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

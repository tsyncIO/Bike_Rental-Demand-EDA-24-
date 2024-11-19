# Initialize the src package
import logging
logging.basicConfig(
    filename="logs/model_training.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Initialized src package for Bike Sharing Kaggle Project.")

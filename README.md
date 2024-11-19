# Bike Sharing Demand Prediction

This project is a machine learning pipeline to predict bike-sharing demand based on historical data. The pipeline includes data preprocessing, feature engineering, model training, evaluation, and Kaggle submission file generation.

---

## Project Overview

Bike-sharing systems are a growing mode of urban transportation. Predicting user demand accurately can optimize resource allocation and improve service quality. 

This project:
1. Processes the raw data into usable features.
2. Trains multiple machine learning models.
3. Evaluates model performance.
4. Outputs predictions in the format required for Kaggle submission.

---

## Folder Structure

```plaintext
bike-sharing-demand/
├── config/                   # Configuration files
│   └── config.yaml           # YAML configuration for the pipeline
│
├── data/                     # Dataset folder
│   ├── raw/                  # Raw input data
│   ├── processed/            # Preprocessed data
│   └── submission/           # Final Kaggle submission file
│
├── logs/                     # Logs folder
│   └── model_training.log    # Logs for the model training process
│
├── notebooks/                # Jupyter notebooks for exploration
│   └── exploratory_analysis.ipynb  # Data analysis notebook
│
├── results/                  # Results folder
│   └── metrics.json          # Model evaluation metrics
│
├── src/                      # Source code
│   ├── __init__.py           # Makes src a Python package
│   ├── preprocess.py         # Preprocessing scripts
│   ├── train.py              # Training scripts
│   ├── evaluate.py           # Evaluation scripts
│   ├── predict.py            # Test prediction script
│   └── utils.py              # Helper functions
│
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation

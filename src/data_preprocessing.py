import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
import logging
import yaml


class DateTimeConverter(BaseEstimator, TransformerMixin):
    def __init__(self, datetime_col):
        self.datetime_col = datetime_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X[self.datetime_col] = pd.to_datetime(X[self.datetime_col])
        return X


class TimeFeaturesExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, datetime_col):
        self.datetime_col = datetime_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X['year'] = X[self.datetime_col].dt.year
        X['month'] = X[self.datetime_col].dt.month
        X['day'] = X[self.datetime_col].dt.day
        X['hour'] = X[self.datetime_col].dt.hour
        X['dayofweek'] = X[self.datetime_col].dt.dayofweek
        X['is_weekend'] = (X[self.datetime_col].dt.dayofweek >= 5).astype(int)
        return X


def load_data(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    train_path = config["data"]["train"]
    test_path = config["data"]["test"]
    return pd.read_csv(train_path), pd.read_csv(test_path)


def preprocess_pipeline():
    return Pipeline([
        ("datetime_converter", DateTimeConverter(datetime_col="datetime")),
        ("time_features", TimeFeaturesExtractor(datetime_col="datetime")),
        ("drop_datetime", FunctionTransformer(lambda X: X.drop(columns=["datetime"], errors="ignore"))),
    ])

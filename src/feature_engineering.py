import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class CyclicEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, columns, max_values):
        self.columns = columns
        self.max_values = max_values

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for col, max_val in zip(self.columns, self.max_values):
            X[f"{col}_sin"] = np.sin(2 * np.pi * X[col] / max_val)
            X[f"{col}_cos"] = np.cos(2 * np.pi * X[col] / max_val)
        return X

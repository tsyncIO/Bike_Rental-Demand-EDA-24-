from sklearn.metrics import mean_squared_error
import numpy as np


def evaluate_models(models, X_test, y_test):
    results = {}
    for name, model in models.items():
        predictions = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        results[name] = rmse
    best_model_name = min(results, key=results.get)
    return best_model_name, models[best_model_name]

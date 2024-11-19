from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


def train_models(X_train, y_train, config):
    models = {
        "ridge": Ridge(alpha=config["models"]["ridge"]["alpha"]),
        "random_forest": RandomForestRegressor(
            n_estimators=config["models"]["random_forest"]["n_estimators"],
            max_depth=config["models"]["random_forest"]["max_depth"]
        ),
        "gradient_boosting": GradientBoostingRegressor(
            n_estimators=config["models"]["gradient_boosting"]["n_estimators"],
            learning_rate=config["models"]["gradient_boosting"]["learning_rate"],
            max_depth=config["models"]["gradient_boosting"]["max_depth"]
        )
    }
    trained_models = {name: model.fit(X_train, y_train) for name, model in models.items()}
    return trained_models

import yaml
from src.data_preprocessing import load_data, preprocess_pipeline
from src.feature_engineering import CyclicEncoder
from src.model_training import train_models
from src.model_evaluation import evaluate_models
from src.submission import generate_submission
from sklearn.model_selection import train_test_split


def main():
    # Load configuration
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Load data
    train_data, test_data = load_data("config/config.yaml")

    # Preprocessing pipeline
    preprocessing = preprocess_pipeline()
    train_data_processed = preprocessing.fit_transform(train_data)
    test_data_processed = preprocessing.transform(test_data)

    # Train/test split
    X = train_data_processed.drop(columns=["count"])
    y = train_data_processed["count"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train models
    models = train_models(X_train, y_train, config)

    # Evaluate models
    best_model_name, best_model = evaluate_models(models, X_test, y_test)
    print(f"Best Model: {best_model_name}")

    # Generate Kaggle submission
    generate_submission(best_model, test_data_processed, test_data, config)


if __name__ == "__main__":
    main()

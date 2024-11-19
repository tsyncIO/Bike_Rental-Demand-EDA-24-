import pandas as pd


def generate_submission(model, X_test, test_data, config):
    predictions = model.predict(X_test)
    submission = test_data[["datetime"]].copy()
    submission["count"] = predictions
    submission_path = config["data"]["processed_test"]
    submission.to_csv(submission_path, index=False)
    print(f"Submission saved to {submission_path}")

import mlflow
import mlflow.sklearn

import joblib
import json

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]



MODEL_PATH = (
    ROOT
    / "artifacts"
    / "churn_pipeline.pkl"
)

METRIC_PATH = (
    ROOT
    / "data"
    / "processed"
    / "final_metrics.csv"
)

PARAM_PATH = (
    ROOT
    / "data"
    / "processed"
    / "best_params.json"
)


mlflow.set_experiment("customer-churn")


with mlflow.start_run():
    model = joblib.load(MODEL_PATH)
    
    params = json.load(open(PARAM_PATH))
    
    for key, value in params.items():

        mlflow.log_param(key, value)

    with open(METRIC_PATH) as f:
        lines = f.read().splitlines()

    headers = lines[0].split(",")

    values = lines[1].split(",")

    for h, v in zip(headers,values):
        if h != "model":
            mlflow.log_metric(h, float(v))

    model_info = mlflow.sklearn.log_model(model, name="churn_model")

    mlflow.register_model(model_info.model_uri, "customer-churn-model")
    
print("Experiment logged")
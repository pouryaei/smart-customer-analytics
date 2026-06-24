import json
import joblib
import mlflow
import mlflow.sklearn

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    ROOT
    / "artifacts"
    / "churn_pipeline.pkl"
)

PARAM_PATH = (
    ROOT
    / "data"
    / "processed"
    / "best_params.json"
)

METRIC_PATH = (
    ROOT
    / "data"
    / "processed"
    / "final_metrics.csv"
)


EXPERIMENT_NAME = "customer-churn"

REGISTERED_MODEL = "customer-churn-model"

mlflow.set_experiment(EXPERIMENT_NAME)


def load_metrics():

    with open(METRIC_PATH) as f:

        rows = f.read().splitlines()

    headers = rows[0].split(",")

    values = rows[1].split(",")

    result = {}

    for h, v in zip(headers, values):

        if h != "model":

            result[h] = float(v)

    return result


def load_params():

    with open(PARAM_PATH):

        return json.load(open(PARAM_PATH))


def train():

    model = joblib.load(MODEL_PATH)

    params = load_params()

    metrics = load_metrics()

    with mlflow.start_run():

        mlflow.log_params(params)

        mlflow.log_metrics(metrics)

        model_info = (
            mlflow.sklearn.log_model(
                sk_model=model,
                name="model"
            )
        )

        mlflow.register_model(
            model_uri=model_info.model_uri,
            name=REGISTERED_MODEL
        )

        print(
            "\nModel Registered\n"
        )


if __name__ == "__main__":
    train()
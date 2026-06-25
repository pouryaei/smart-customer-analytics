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


mlflow.set_experiment(
    "customer-churn"
)


with mlflow.start_run() as run:

    model = joblib.load(
        MODEL_PATH
    )

    params = json.load(
        open(PARAM_PATH)
    )

    for k, v in params.items():

        mlflow.log_param(
            k,
            v
        )

    with open(METRIC_PATH) as f:

        rows = (
            f
            .read()
            .splitlines()
        )

    headers = (
        rows[0]
        .split(",")
    )

    values = (
        rows[1]
        .split(",")
    )

    for h, v in zip(
        headers,
        values
    ):

        if h != "model":

            mlflow.log_metric(
                h,
                float(v)
            )

    model_info = (
        mlflow.sklearn.log_model(
            sk_model=model,
            name="model"
        )
    )

    print(
        f"run_id={run.info.run_id}"
    )

    print(
        model_info.model_uri
    )
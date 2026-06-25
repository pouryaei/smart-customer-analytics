import mlflow
import mlflow.sklearn
import joblib

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    ROOT
    / "artifacts"
    / "churn_pipeline.pkl"
)

mlflow.set_experiment(
    "customer-churn"
)


with mlflow.start_run():

    model = joblib.load(
        MODEL_PATH
    )

    model_info = (
        mlflow.sklearn.log_model(
            sk_model=model,
            name="model"
        )
    )

print(
    model_info.model_uri
)
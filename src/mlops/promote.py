from mlflow import MlflowClient


MODEL_NAME = (
    "customer-churn-model"
)

VERSION = 1


client = (
    MlflowClient()
)

client.set_registered_model_alias(
    MODEL_NAME,
    "production",
    VERSION
)

print(
    "promoted"
)
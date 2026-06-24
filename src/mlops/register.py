import mlflow

MODEL_NAME = "customer-churn-model"


client = mlflow.MlflowClient()

versions = client.search_model_versions(f"name='{MODEL_NAME}'")

latest = sorted(versions, key=lambda x:int(x.version))[-1]

client.set_registered_model_alias(
    name=MODEL_NAME,
    alias="production",
    version=latest.version
)

print(f"\nProduction → v{latest.version}\n")
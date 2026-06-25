import mlflow


MODEL_URI = (
    "runs:/"
    "bb942184876b4ddb9843029c272be323"
    "/model"
)

mlflow.register_model(
    MODEL_URI,
    "customer-churn-model"
)

print(
    "registered"
)
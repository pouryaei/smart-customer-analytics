import sys
import mlflow


RUN_ID = sys.argv[1]

MODEL_URI = (
    f"runs:/{RUN_ID}/model"
)

mlflow.register_model(
    MODEL_URI,
    "customer-churn-model"
)

print("registered")
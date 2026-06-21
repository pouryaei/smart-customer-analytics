import joblib
from pathlib import Path


MODEL_PATH = (
    Path(__file__)
    .parent
    .parent
    / "models"
    / "churn_pipeline.pkl"
)


model = (joblib.load(MODEL_PATH))


def predict_customer(customer_df):

    prediction = (model.predict(customer_df)[0])

    probability = (model.predict_proba(customer_df)[0][1])

    return {
        "prediction":
        int(prediction),

        "probability":
        round(float(probability), 3)
        }
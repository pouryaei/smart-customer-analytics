import joblib
import pandas as pd
from pathlib import Path


MODEL_PATH = (
    Path(__file__)
    .parent
    .parent
    / "models"
    / "churn_pipeline.pkl"
)

model = joblib.load(MODEL_PATH)


FEATURE_PATH = (
    Path(__file__)
    .parent.parent.parent
    / "data"
    / "processed"
    / "selected_features.csv"
)

model = joblib.load(MODEL_PATH)

FEATURES = (
    pd.read_csv(FEATURE_PATH)
    .iloc[:,0]
    .tolist()
)


def predict_customer(customer):

    row = {
        col: 0
        for col in FEATURES
    }

    row.update(customer)

    customer_df = pd.DataFrame(
        [row]
    )

    prediction = (
        model.predict(
            customer_df
        )[0]
    )

    probability = (
        model.predict_proba(
            customer_df
        )[0][1]
    )

    return {
        "prediction": int(prediction),
        "probability": round(
            float(probability),
            3
        )
    }
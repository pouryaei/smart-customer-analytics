import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = (
    Path(__file__)
    .parent
    .parent
    .parent
    / "artifacts"
    / "churn_pipeline.pkl"
)

model = joblib.load(MODEL_PATH)

FEATURES = list(model.feature_names_in_)

COEFS = model.named_steps["model"].coef_[0]
feature_importance = dict(zip(FEATURES, COEFS))


def explain_prediction(row: dict):
    contributions = []

    for feature, value in row.items():
        if feature in feature_importance:
            contributions.append(
                (feature, feature_importance[feature] * value)
            )

    contributions.sort(key=lambda x: abs(x[1]), reverse=True)
    return contributions[:5]


def predict_customer(customer: dict):
    row = {col: 0 for col in FEATURES}
    row.update(customer)

    df = pd.DataFrame([row])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    explanation = explain_prediction(row)

    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 3),
        "explanation": explanation
    }
import joblib
import pandas as pd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    ROOT
    / "artifacts"
    / "churn_pipeline.pkl"
)

model = joblib.load(MODEL_PATH)

FEATURES = list(model.feature_names_in_)

COEFS = (
    model
    .named_steps["model"]
    .coef_[0]
)

feature_importance = dict(
    zip(
        FEATURES,
        COEFS
    )
)


def explain_prediction(row):

    scores = []

    for feature, value in row.items():

        if feature in feature_importance:

            scores.append(
                (
                    feature,
                    float(
                        value
                        *
                        feature_importance[
                            feature
                        ]
                    )
                )
            )

    scores.sort(
        key=lambda x:
        abs(x[1]),
        reverse=True
    )

    return scores[:5]


def predict_customer(customer):

    row = {
        f: 0
        for f in FEATURES
    }

    row.update(customer)

    df = pd.DataFrame([row])

    pred = model.predict(df)[0]

    prob = model.predict_proba(df)[0][1]

    return {

        "prediction":
        int(pred),

        "probability":
        round(
            float(prob),
            3
        ),

        "explanation":
        explain_prediction(
            row
        )
    }
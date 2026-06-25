import json
from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]

TRAIN = (
    ROOT
    / "data"
    / "processed"
    / "train_ready.csv"
)

PRED = (
    ROOT
    / "monitoring"
    / "predictions.jsonl"
)


def detect_drift():

    if not PRED.exists():
        return None

    train = pd.read_csv(TRAIN)

    rows = []

    with open(PRED) as f:
        for line in f:
            rows.append(
                json.loads(line)
            )

    if len(rows) < 10:
        return None

    current = pd.DataFrame(
        [
            r["input"]
            for r in rows
        ]
    )

    report = {}

    for col in current.columns:

        if col in train.columns:

            diff = abs(
                current[col].mean()
                -
                train[col].mean()
            )

            report[col] = round(
                float(diff),
                3
            )

    return report

def check_alert():

    report = detect_drift()

    if report is None:
        return

    alerts = []

    for col, value in report.items():

        if value > 100:

            alerts.append(
                col
            )

    return alerts
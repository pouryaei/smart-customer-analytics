import json
from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parents[2]

LOG_FILE = (
    ROOT
    / "monitoring"
    / "predictions.jsonl"
)


def log_prediction(
    payload,
    result
):

    LOG_FILE.parent.mkdir(
        exist_ok=True
    )

    row = {

        "timestamp":
        datetime.utcnow().isoformat(),

        "input":
        payload,

        "prediction":
        result["prediction"],

        "probability":
        result["probability"]

    }

    with open(
        LOG_FILE,
        "a"
    ) as f:

        f.write(
            json.dumps(row)
            + "\n"
        )
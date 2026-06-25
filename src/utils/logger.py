import logging
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

LOG_DIR = ROOT / "logs"

LOG_DIR.mkdir(
    exist_ok=True
)

LOG_FILE = (
    LOG_DIR
    / "api.log"
)


logger = logging.getLogger(
    "axiomeet"
)

logger.setLevel(
    logging.INFO
)


if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_FILE
    )

    file_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    stream_handler = logging.StreamHandler()

    stream_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        stream_handler
    )
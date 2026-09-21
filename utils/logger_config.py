import logging
import sys
from datetime import datetime
from pathlib import Path


#DEBUG<INFO<WARNING<ERROR<CRITICAL
def configure_logging():
    logs_dir = Path(__file__).resolve().parents[1] / "logs"
    logs_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = logs_dir / f"test_{timestamp}.log"

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    logging.getLogger("selenium").setLevel(logging.WARNING)

    formatter = logging.Formatter(
        "%(asctime)s-%(levelname)s-%(name)s-%(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        log_path,
        mode="w",
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


"""
logger

--console handler --> INFO+
--file handler --->DEBUG+

"""
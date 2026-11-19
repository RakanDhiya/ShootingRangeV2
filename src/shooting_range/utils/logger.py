"""
Application logging configuration.

Provides centralized logging setup and logger creation
for the ShootingRangeV2 application.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
LOG_DIRECTORY = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIRECTORY / "application.log"


def configure_logging():
    """
    Configure application-wide logging.

    Logs are written to a rotating file and the console.
    Existing handlers are checked to prevent duplication.
    """
    root_logger = logging.getLogger()

    if root_logger.handlers:
        return

    LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

    log_format = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1_000_000,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(log_format)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)


def get_logger(name):
    """
    Create a named logger.

    Args:
        name (str): Name of the module requesting the logger.

    Returns:
        logging.Logger: Configured module logger.
    """
    return logging.getLogger(name)
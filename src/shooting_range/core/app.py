"""
Application entry point and initialization.

Creates the Qt application, initializes logging,
and starts the application navigation controller.
"""

from PySide6.QtWidgets import QApplication

from shooting_range.config.settings import APP_NAME
from shooting_range.core.navigation import NavigationController
from shooting_range.utils.logger import configure_logging, get_logger


def run_app():
    """
    Initialize and run the desktop application.

    Returns:
        int: Application exit code.
    """
    configure_logging()
    logger = get_logger(APP_NAME)

    logger.info("Application startup.")

    app = QApplication([])
    app.setApplicationName(APP_NAME)

    navigation = NavigationController()
    navigation.start()

    exit_code = app.exec()

    logger.info("Application shutdown. Exit code: %s", exit_code)

    return exit_code
"""
Application entry point and initialization.

Creates the Qt application and starts the application
navigation controller.
"""

from PySide6.QtWidgets import QApplication

from shooting_range.config.settings import APP_NAME
from shooting_range.core.navigation import NavigationController


def run_app():
    """
    Initialize and run the desktop application.

    Returns:
        int: Application exit code.
    """
    app = QApplication([])

    app.setApplicationName(APP_NAME)

    navigation = NavigationController()
    navigation.start()

    return app.exec()
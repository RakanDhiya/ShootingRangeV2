"""
Application navigation controller.

Manages transitions between the start screen, agreement screen,
and main application window.
"""

from shooting_range.ui.screens.start_screen import StartScreen
from shooting_range.ui.screens.agreement_screen import AgreementScreen
from shooting_range.ui.main_window import MainWindow


class NavigationController:
    """Manage application screen transitions."""

    def __init__(self):
        """Initialize screen references."""
        self.start_screen = None
        self.agreement_screen = None
        self.main_window = None

    def start(self):
        """Display the initial application screen."""
        self.start_screen = StartScreen()
        self.start_screen.setWindowTitle("ShootingRangeV2")
        self.start_screen.resize(1000, 650)

        self.start_screen.start_requested.connect(self.show_agreement)

        self.start_screen.show()

    def show_agreement(self):
        """Display the agreement screen."""
        if self.start_screen is not None:
            self.start_screen.hide()

        self.agreement_screen = AgreementScreen()
        self.agreement_screen.setWindowTitle("User Agreement")
        self.agreement_screen.resize(1000, 650)

        self.agreement_screen.agreement_accepted.connect(self.show_main_application)

        self.agreement_screen.show()

    def show_main_application(self):
        """Display the main application window."""
        if self.agreement_screen is not None:
            self.agreement_screen.hide()

        self.main_window = MainWindow()
        self.main_window.showMaximized()
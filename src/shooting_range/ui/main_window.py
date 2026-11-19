"""
Main application window.

Provides the primary application layout and navigation
between the main application pages.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from shooting_range.ui.camera_page import CameraPage


class MainWindow(QMainWindow):
    """Display the main application interface."""

    def __init__(self):
        """Initialize the main window and its pages."""
        super().__init__()

        self.setWindowTitle("ShootingRangeV2")
        self.resize(1280, 800)

        self.nav_buttons = []

        self.setup_ui()
        self.change_page(0)

    def setup_ui(self):
        """Create and arrange the main application interface."""
        central = QWidget()
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        header = QFrame()
        header.setObjectName("header")
        header.setFixedHeight(76)

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(30, 0, 30, 0)

        logo = QLabel("SHOOTING RANGE")
        logo.setObjectName("logo")

        version = QLabel("V2")
        version.setObjectName("version")

        header_layout.addWidget(logo)
        header_layout.addWidget(version)
        header_layout.addStretch()

        main_layout.addWidget(header)

        navigation = QFrame()
        navigation.setObjectName("navigation")
        navigation.setFixedHeight(58)

        navigation_layout = QHBoxLayout(navigation)
        navigation_layout.setContentsMargins(30, 0, 30, 0)
        navigation_layout.setSpacing(10)

        self.pages = QStackedWidget()

        page_definitions = [
            ("QUICK START", self.create_quick_start_page()),
            (
                "PROGRAMS",
                self.create_placeholder_page(
                    "Programs",
                    "Browse available program information.",
                ),
            ),
            (
                "TIMED DRILLS",
                self.create_placeholder_page(
                    "Timed Drills",
                    "View drill configuration information.",
                ),
            ),
        ]

        for index, (name, page) in enumerate(page_definitions):
            button = QPushButton(name)
            button.setObjectName("nav_button")
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(lambda checked=False, i=index: self.change_page(i))

            navigation_layout.addWidget(button)
            self.nav_buttons.append(button)
            self.pages.addWidget(page)

        navigation_layout.addStretch()

        main_layout.addWidget(navigation)

        content_frame = QFrame()
        content_frame.setObjectName("content_frame")

        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.addWidget(self.pages)

        main_layout.addWidget(content_frame, 1)

        bottom_bar = QFrame()
        bottom_bar.setObjectName("bottom_bar")
        bottom_bar.setFixedHeight(42)

        bottom_layout = QHBoxLayout(bottom_bar)
        bottom_layout.setContentsMargins(30, 0, 30, 0)

        application_status = QLabel("APPLICATION READY")
        application_status.setObjectName("bottom_status")

        camera_status = QLabel("CAMERA: DISCONNECTED")
        camera_status.setObjectName("bottom_status")

        bottom_layout.addWidget(application_status)
        bottom_layout.addStretch()
        bottom_layout.addWidget(camera_status)

        main_layout.addWidget(bottom_bar)

        self.setCentralWidget(central)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f4f6f9;
            }

            #header {
                background-color: #172033;
            }

            #logo {
                color: white;
                font-size: 22px;
                font-weight: bold;
                letter-spacing: 2px;
            }

            #version {
                color: #93c5fd;
                font-size: 12px;
                font-weight: bold;
            }

            #navigation {
                background-color: white;
                border-bottom: 1px solid #e2e8f0;
            }

            #nav_button {
                background-color: transparent;
                color: #64748b;
                border: none;
                border-bottom: 3px solid transparent;
                padding: 15px 22px;
                font-size: 13px;
                font-weight: bold;
            }

            #nav_button:hover {
                color: #2563eb;
                background-color: #f8fafc;
            }

            #nav_button[active="true"] {
                color: #2563eb;
                border-bottom: 3px solid #2563eb;
            }

            #content_frame {
                background-color: #f4f6f9;
            }

            #bottom_bar {
                background-color: #172033;
            }

            #bottom_status {
                color: #cbd5e1;
                font-size: 11px;
                font-weight: bold;
            }
        """)

    def create_quick_start_page(self):
        """Create the initial quick start page."""
        return CameraPage()

    def create_placeholder_page(self, title, description):
        """Create a temporary page for unfinished application sections."""
        page = QWidget()

        layout = QVBoxLayout(page)
        layout.setContentsMargins(35, 30, 35, 30)
        layout.setSpacing(12)

        heading = QLabel(title)
        heading.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            color: #172033;
        """)

        subtitle = QLabel(description)
        subtitle.setStyleSheet("""
            font-size: 14px;
            color: #64748b;
        """)

        layout.addWidget(heading)
        layout.addWidget(subtitle)
        layout.addStretch()

        return page

    def change_page(self, index):
        """Switch the active application page."""
        self.pages.setCurrentIndex(index)

        for page_index, button in enumerate(self.nav_buttons):
            button.setProperty("active", page_index == index)
            button.style().unpolish(button)
            button.style().polish(button)
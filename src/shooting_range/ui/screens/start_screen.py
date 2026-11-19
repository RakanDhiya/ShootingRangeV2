"""
Application start screen.

Provides the initial application interface and emits a signal
when the user chooses to continue.
"""

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)


class StartScreen(QWidget):
    """Display the initial screen of the application."""

    start_requested = Signal()

    def __init__(self):
        """Initialize the start screen and its interface."""
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        """Create and arrange the start screen components."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(60, 50, 60, 50)
        layout.setSpacing(20)

        layout.addStretch()

        title = QLabel("SHOOTING RANGE")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color: #172033;
            letter-spacing: 3px;
        """)

        subtitle = QLabel("SHOOTING RANGE SIMULATION")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 14px;
            color: #64748b;
            letter-spacing: 2px;
        """)

        start_button = QPushButton("START")
        start_button.setFixedSize(180, 48)
        start_button.setCursor(Qt.CursorShape.PointingHandCursor)
        start_button.setStyleSheet("""
            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }

            QPushButton:pressed {
                background-color: #1e40af;
            }
        """)

        start_button.clicked.connect(self.start_requested.emit)

        button_container = QVBoxLayout()
        button_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_container.addWidget(start_button)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addLayout(button_container)

        layout.addStretch()

        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f9;
            }
        """)
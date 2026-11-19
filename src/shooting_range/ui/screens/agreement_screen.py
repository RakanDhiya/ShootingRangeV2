"""
Application agreement screen.

Displays the application agreement and allows users
to confirm before entering the main application.
"""

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
)


class AgreementScreen(QWidget):
    """Display the application agreement and confirmation action."""

    agreement_accepted = Signal()

    def __init__(self):
        """Initialize the agreement screen."""
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        """Create and arrange the agreement screen components."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(80, 50, 80, 50)
        layout.setSpacing(20)

        title = QLabel("USER AGREEMENT")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #172033;
        """)

        subtitle = QLabel("Please review the application agreement.")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 14px;
            color: #64748b;
        """)

        agreement_text = QTextEdit()
        agreement_text.setReadOnly(True)
        agreement_text.setPlainText(
            "APPLICATION AGREEMENT\n\n"
            "Please read and understand the applicable rules "
            "and instructions before continuing.\n\n"
            "1. Use the application only for its intended purpose.\n\n"
            "2. Follow the applicable facility rules and "
            "supervisor instructions.\n\n"
            "3. Do not use the application as a substitute "
            "for professional instruction.\n\n"
            "4. Contact the responsible administrator if you "
            "experience an application issue.\n\n"
            "By selecting AGREE & CONTINUE, you confirm that "
            "you have read and accepted this agreement."
        )
        agreement_text.setStyleSheet("""
            QTextEdit {
                background-color: white;
                color: #334155;
                border: 1px solid #e2e8f0;
                border-radius: 8px;
                padding: 15px;
                font-size: 14px;
            }
        """)

        continue_button = QPushButton("AGREE & CONTINUE")
        continue_button.setFixedSize(220, 48)
        continue_button.setCursor(Qt.CursorShape.PointingHandCursor)
        continue_button.setStyleSheet("""
            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }

            QPushButton:pressed {
                background-color: #1e40af;
            }
        """)

        continue_button.clicked.connect(self.agreement_accepted.emit)

        button_container = QVBoxLayout()
        button_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_container.addWidget(continue_button)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(agreement_text, 1)
        layout.addLayout(button_container)

        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f9;
            }
        """)
"""
Quick Start page.

Provides camera source selection, connection controls,
camera status information, and a live camera preview.
"""

import cv2

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from shooting_range.config.settings import CAMERA_FRAME_INTERVAL_MS
from shooting_range.services.camera_service import CameraService
from shooting_range.services.mock_camera_service import MockCameraService
from shooting_range.utils.logger import get_logger

logger = get_logger(__name__)

class CameraPage(QWidget):
    """Display camera controls and preview in the Quick Start page."""

    def __init__(self):
        """Initialize camera services, timer, and page interface."""
        super().__init__()

        self.physical_camera = CameraService()
        self.mock_camera = MockCameraService()
        self.active_camera = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.setup_ui()

    def setup_ui(self):
        """Create and arrange the Quick Start interface."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 25, 30, 25)
        main_layout.setSpacing(18)

        heading = QLabel("QUICK START")
        heading.setObjectName("page_heading")

        description = QLabel(
            "Manage the camera connection and view the live preview."
        )
        description.setObjectName("page_description")

        main_layout.addWidget(heading)
        main_layout.addWidget(description)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)

        # Camera information panel
        control_panel = QFrame()
        control_panel.setObjectName("control_panel")
        control_panel.setFixedWidth(280)

        control_layout = QVBoxLayout(control_panel)
        control_layout.setContentsMargins(20, 22, 20, 22)
        control_layout.setSpacing(14)

        panel_title = QLabel("CAMERA SETTINGS")
        panel_title.setObjectName("panel_title")

        source_label = QLabel("Camera Source")
        source_label.setObjectName("field_label")

        self.camera_selector = QComboBox()
        self.camera_selector.addItems([
            "Mock Camera",
            "Physical Camera",
        ])
        self.camera_selector.setObjectName("camera_selector")

        status_title = QLabel("Connection Status")
        status_title.setObjectName("field_label")

        self.status = QLabel("Disconnected")
        self.status.setObjectName("camera_status")
        self.status.setProperty("connected", False)

        self.connect_button = QPushButton("Connect Camera")
        self.connect_button.setObjectName("connect_button")
        self.connect_button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.disconnect_button = QPushButton("Disconnect")
        self.disconnect_button.setObjectName("disconnect_button")
        self.disconnect_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.disconnect_button.setEnabled(False)

        self.connect_button.clicked.connect(self.connect_camera)
        self.disconnect_button.clicked.connect(self.disconnect_camera)

        information = QLabel(
            "Select a camera source and connect to display its preview."
        )
        information.setObjectName("panel_information")
        information.setWordWrap(True)

        control_layout.addWidget(panel_title)
        control_layout.addSpacing(8)
        control_layout.addWidget(source_label)
        control_layout.addWidget(self.camera_selector)
        control_layout.addSpacing(8)
        control_layout.addWidget(status_title)
        control_layout.addWidget(self.status)
        control_layout.addSpacing(10)
        control_layout.addWidget(self.connect_button)
        control_layout.addWidget(self.disconnect_button)
        control_layout.addStretch()
        control_layout.addWidget(information)

        # Camera preview panel
        preview_panel = QFrame()
        preview_panel.setObjectName("preview_panel")

        preview_layout = QVBoxLayout(preview_panel)
        preview_layout.setContentsMargins(18, 18, 18, 18)
        preview_layout.setSpacing(12)

        preview_header = QHBoxLayout()

        preview_title = QLabel("CAMERA PREVIEW")
        preview_title.setObjectName("panel_title")

        self.preview_indicator = QLabel("● OFFLINE")
        self.preview_indicator.setObjectName("preview_indicator")

        preview_header.addWidget(preview_title)
        preview_header.addStretch()
        preview_header.addWidget(self.preview_indicator)

        self.preview = QLabel("Camera preview is currently unavailable")
        self.preview.setObjectName("camera_preview")
        self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview.setMinimumSize(400, 300)

        preview_layout.addLayout(preview_header)
        preview_layout.addWidget(self.preview, 1)

        content_layout.addWidget(control_panel)
        content_layout.addWidget(preview_panel, 1)

        main_layout.addLayout(content_layout, 1)

        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f9;
                font-family: "Segoe UI";
            }

            #page_heading {
                color: #172033;
                font-size: 25px;
                font-weight: bold;
            }

            #page_description {
                color: #64748b;
                font-size: 13px;
            }

            #control_panel, #preview_panel {
                background-color: white;
                border: 1px solid #e2e8f0;
                border-radius: 10px;
            }

            #panel_title {
                color: #172033;
                font-size: 13px;
                font-weight: bold;
            }

            #field_label {
                color: #475569;
                font-size: 12px;
                font-weight: bold;
            }

            #camera_selector {
                background-color: white;
                color: #172033;
                border: 1px solid #cbd5e1;
                border-radius: 5px;
                padding: 9px;
                min-height: 22px;
            }

            #camera_selector QAbstractItemView {
                background-color: white;
                color: #172033;
                selection-background-color: #2563eb;
                selection-color: white;
                border: 1px solid #cbd5e1;
            }

            #camera_status {
                color: #dc2626;
                font-size: 13px;
                font-weight: bold;
                padding: 5px 0;
            }

            #camera_status[connected="true"] {
                color: #16a34a;
            }

            #connect_button {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 11px;
                font-weight: bold;
            }

            #connect_button:hover {
                background-color: #1d4ed8;
            }

            #disconnect_button {
                background-color: #e2e8f0;
                color: #172033;
                border: none;
                border-radius: 5px;
                padding: 11px;
                font-weight: bold;
            }

            #disconnect_button:hover:enabled {
                background-color: #cbd5e1;
            }

            #disconnect_button:disabled {
                color: #94a3b8;
                background-color: #f1f5f9;
            }

            #panel_information {
                color: #94a3b8;
                font-size: 11px;
            }

            #preview_indicator {
                color: #dc2626;
                font-size: 11px;
                font-weight: bold;
            }

            #camera_preview {
                background-color: #172033;
                color: #cbd5e1;
                border-radius: 6px;
                font-size: 13px;
            }
        """)

    def connect_camera(self):
        """Connect the selected camera source and start frame updates."""
        if self.timer.isActive():
            return

        if self.camera_selector.currentText() == "Mock Camera":
            self.active_camera = self.mock_camera
        else:
            self.active_camera = self.physical_camera

        try:
            if not self.active_camera.connect():
                logger.warning("Failed to connect to the selected camera.")

                self.active_camera = None
                self.status.setText("Camera unavailable")
                self.refresh_status_style()
                return

            logger.info(
                "Camera UI connected using %s.",
                self.camera_selector.currentText(),
            )

            self.status.setText("Connected")
            self.status.setProperty("connected", True)

            self.preview_indicator.setText("● LIVE")
            self.preview_indicator.setStyleSheet("color: #16a34a;")

            self.camera_selector.setEnabled(False)
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(True)

            self.refresh_status_style()
            self.timer.start(CAMERA_FRAME_INTERVAL_MS)

        except Exception:
            logger.exception("Unexpected error while connecting camera.")

            self.active_camera = None
            self.status.setText("Camera unavailable")
            self.refresh_status_style()

    def update_frame(self):
        """Retrieve, validate, convert, and display the latest camera frame."""
        if self.active_camera is None:
            return

        try:
            frame = self.active_camera.get_frame()

            if frame is None:
                logger.warning("Camera frame is unavailable.")
                self.disconnect_camera()
                self.status.setText("Camera disconnected")
                self.refresh_status_style()
                return

            if (
                not hasattr(frame, "shape")
                or frame.ndim != 3
                or frame.shape[2] != 3
                or frame.size == 0
            ):
                logger.warning("Camera returned an invalid frame.")
                self.disconnect_camera()
                self.status.setText("Invalid camera frame")
                self.refresh_status_style()
                return

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            height, width, channels = frame.shape

            image = QImage(
                frame.data,
                width,
                height,
                channels * width,
                QImage.Format.Format_RGB888,
            ).copy()

            if image.isNull():
                logger.warning("Failed to convert camera frame into QImage.")
                return

            pixmap = QPixmap.fromImage(image)

            self.preview.setPixmap(
                pixmap.scaled(
                    self.preview.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )

        except cv2.error:
            logger.exception("OpenCV error while processing camera frame.")
            self.disconnect_camera()
            self.status.setText("Camera error")
            self.refresh_status_style()

        except (ValueError, TypeError, AttributeError):
            logger.exception("Invalid camera frame data.")
            self.disconnect_camera()
            self.status.setText("Invalid camera frame")
            self.refresh_status_style()

    def disconnect_camera(self):
        """Stop frame updates and release the active camera source."""
        self.timer.stop()

        if self.active_camera is not None:
            camera = self.active_camera
            self.active_camera = None

            try:
                camera.disconnect()
                logger.info("Camera UI disconnected.")

            except Exception:
                logger.exception("Unexpected error while disconnecting camera.")

        self.camera_selector.setEnabled(True)
        self.connect_button.setEnabled(True)
        self.disconnect_button.setEnabled(False)

        self.preview.clear()
        self.preview.setText("Camera preview is currently unavailable")

        self.status.setText("Disconnected")
        self.preview_indicator.setText("● OFFLINE")
        self.preview_indicator.setStyleSheet("color: #dc2626;")

        self.refresh_status_style()

    def refresh_status_style(self):
        """Refresh the camera status label after connection changes."""
        connected = self.active_camera is not None

        self.status.setProperty("connected", connected)
        self.status.style().unpolish(self.status)
        self.status.style().polish(self.status)

    def closeEvent(self, event):
        """Release camera resources when the page is closed."""
        self.disconnect_camera()
        super().closeEvent(event)

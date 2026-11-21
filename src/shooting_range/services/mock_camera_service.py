"""
Mock camera service for preview testing.

Generates synthetic camera frames without requiring
a physical camera device.
"""

import cv2
import numpy as np

from shooting_range.config.settings import PREVIEW_WIDTH, PREVIEW_HEIGHT
from shooting_range.utils.logger import get_logger

logger = get_logger(__name__)


class MockCameraService:
    """
    Generate synthetic camera frames for preview testing.

    This service simulates a camera stream without requiring
    a physical camera device.
    """

    FRAME_WIDTH = PREVIEW_WIDTH
    FRAME_HEIGHT = PREVIEW_HEIGHT

    def __init__(self):
        """Initialize the mock camera in a disconnected state."""
        self.connected = False
        self.frame_number = 0

    def connect(self):
        """
        Start the simulated camera stream.

        Returns:
            bool: True when the mock camera is connected.
        """
        self.connected = True
        self.frame_number = 0

        logger.info("Mock camera connected.")

        return True

    def get_frame(self):
        """
        Generate the next synthetic camera frame.

        Returns:
            numpy.ndarray | None: BGR image frame, or None
            when the mock camera is disconnected.
        """
        if not self.connected:
            return None

        try:
            frame = np.zeros(
                (self.FRAME_HEIGHT, self.FRAME_WIDTH, 3),
                dtype=np.uint8,
            )

            frame[:] = (32, 42, 60)

            self.frame_number += 1

            cv2.putText(
                frame,
                "MOCK CAMERA",
                (190, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (255, 255, 255),
                2,
            )

            cv2.putText(
                frame,
                f"Frame: {self.frame_number}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (100, 220, 100),
                2,
            )

            position_x = (self.frame_number * 5) % 540

            cv2.rectangle(
                frame,
                (position_x, 300),
                (position_x + 100, 360),
                (40, 160, 230),
                -1,
            )

            return frame

        except (cv2.error, ValueError):
            logger.exception("Failed to generate mock camera frame.")
            self.disconnect()
            return None

    def disconnect(self):
        """Stop the simulated camera stream."""
        if self.connected:
            self.connected = False
            logger.info("Mock camera disconnected.")

    def is_connected(self):
        """
        Check whether the mock camera is active.

        Returns:
            bool: True if connected, otherwise False.
        """
        return self.connected
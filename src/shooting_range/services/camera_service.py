"""
Physical camera service using OpenCV.

Handles camera connection, frame retrieval,
resource release, and camera-related error logging.
"""

import cv2

from shooting_range.config.settings import DEFAULT_CAMERA_INDEX
from shooting_range.utils.logger import get_logger

logger = get_logger(__name__)


class CameraService:
    """Manage connection and frame retrieval from a physical camera."""

    def __init__(self):
        """Initialize the camera service in a disconnected state."""
        self.camera = None

    def connect(self, camera_index=DEFAULT_CAMERA_INDEX):
        """
        Connect to a physical camera.

        Args:
            camera_index (int): Camera device index.

        Returns:
            bool: True if the camera connects successfully.
        """
        if self.camera is not None:
            self.disconnect()

        try:
            self.camera = cv2.VideoCapture(camera_index)

            if not self.camera.isOpened():
                logger.warning(
                    "Unable to open camera at index %s.",
                    camera_index,
                )
                self.disconnect()
                return False

            logger.info(
                "Physical camera connected at index %s.",
                camera_index,
            )
            return True

        except cv2.error:
            logger.exception(
                "OpenCV error while connecting to camera index %s.",
                camera_index,
            )
            self.disconnect()
            return False

    def get_frame(self):
        """
        Retrieve the latest camera frame.

        Returns:
            numpy.ndarray | None: Camera frame or None if unavailable.
        """
        if self.camera is None:
            return None

        try:
            success, frame = self.camera.read()

            if not success:
                logger.warning("Camera frame retrieval failed. Disconnecting camera.")
                self.disconnect()
                return None

            return frame

        except cv2.error:
            logger.exception("OpenCV error while retrieving camera frame.")
            self.disconnect()
            return None

    def disconnect(self):
        """Release the physical camera resource."""
        if self.camera is not None:
            camera = self.camera
            self.camera = None

            try:
                camera.release()
                logger.info("Physical camera disconnected.")

            except cv2.error:
                logger.exception("OpenCV error while releasing physical camera.")

    def is_connected(self):
        """
        Check whether the physical camera is connected.

        Returns:
            bool: True if the camera is active.
        """
        return self.camera is not None and self.camera.isOpened()
"""
Physical camera service using OpenCV.
"""

import cv2

from shooting_range.config.settings import DEFAULT_CAMERA_INDEX


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

        self.camera = cv2.VideoCapture(camera_index)

        if not self.camera.isOpened():
            self.disconnect()
            return False

        return True

    def get_frame(self):
        """
        Retrieve the latest camera frame.

        Returns:
            numpy.ndarray | None: Camera frame or None if unavailable.
        """
        if self.camera is None:
            return None

        success, frame = self.camera.read()

        if not success:
            return None

        return frame

    def disconnect(self):
        """Release the physical camera resource."""
        if self.camera is not None:
            self.camera.release()
            self.camera = None

    def is_connected(self):
        """
        Check whether the physical camera is connected.

        Returns:
            bool: True if the camera is active.
        """
        return self.camera is not None and self.camera.isOpened()
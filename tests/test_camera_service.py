import cv2
import numpy as np

from shooting_range.services.camera_service import CameraService
from shooting_range.services.mock_camera_service import MockCameraService


class FakeVideoCapture:
    """Simulate an OpenCV video capture device for testing."""

    def __init__(self, opened=True, read_success=True):
        self.opened = opened
        self.read_success = read_success
        self.released = False

    def isOpened(self):
        """Return whether the simulated camera is available."""
        return self.opened

    def read(self):
        """Return a synthetic frame or simulate a failed read."""
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        return self.read_success, frame

    def release(self):
        """Mark the simulated camera as released."""
        self.released = True


def test_mock_camera_starts_disconnected():
    """Verify that mock camera starts in a disconnected state."""
    camera = MockCameraService()

    assert camera.is_connected() is False
    assert camera.get_frame() is None


def test_mock_camera_connects_successfully():
    """Verify that mock camera can connect and generate frames."""
    camera = MockCameraService()

    assert camera.connect() is True
    assert camera.is_connected() is True

    frame = camera.get_frame()

    assert frame is not None
    assert frame.shape == (480, 640, 3)


def test_mock_camera_disconnects_successfully():
    """Verify that mock camera stops after disconnection."""
    camera = MockCameraService()

    camera.connect()
    camera.disconnect()

    assert camera.is_connected() is False
    assert camera.get_frame() is None


def test_physical_camera_connects_successfully(monkeypatch):
    """Verify physical camera connection using a simulated device."""
    fake_camera = FakeVideoCapture()

    monkeypatch.setattr(
        "shooting_range.services.camera_service.cv2.VideoCapture",
        lambda index: fake_camera,
    )

    camera = CameraService()

    assert camera.connect() is True
    assert camera.is_connected() is True

    frame = camera.get_frame()

    assert frame is not None
    assert frame.shape == (480, 640, 3)

    camera.disconnect()

    assert fake_camera.released is True
    assert camera.is_connected() is False


def test_physical_camera_handles_unavailable_device(monkeypatch):
    """Verify that failed camera connections are handled correctly."""
    fake_camera = FakeVideoCapture(opened=False)

    monkeypatch.setattr(
        "shooting_range.services.camera_service.cv2.VideoCapture",
        lambda index: fake_camera,
    )

    camera = CameraService()

    assert camera.connect() is False
    assert camera.is_connected() is False
    assert fake_camera.released is True


def test_physical_camera_disconnects_after_failed_frame_read(monkeypatch):
    """Verify that camera is released when frame retrieval fails."""
    fake_camera = FakeVideoCapture(read_success=False)

    monkeypatch.setattr(
        "shooting_range.services.camera_service.cv2.VideoCapture",
        lambda index: fake_camera,
    )

    camera = CameraService()

    assert camera.connect() is True
    assert camera.get_frame() is None
    assert fake_camera.released is True
    assert camera.is_connected() is False


def test_physical_camera_handles_connection_error(monkeypatch):
    """Verify that OpenCV connection errors are handled correctly."""

    def raise_camera_error(index):
        raise cv2.error("Simulated camera connection error")

    monkeypatch.setattr(
        "shooting_range.services.camera_service.cv2.VideoCapture",
        raise_camera_error,
    )

    camera = CameraService()

    assert camera.connect() is False
    assert camera.is_connected() is False


def test_physical_camera_handles_frame_read_error(monkeypatch):
    """Verify that OpenCV frame retrieval errors are handled correctly."""

    fake_camera = FakeVideoCapture()

    def raise_read_error():
        raise cv2.error("Simulated frame retrieval error")

    fake_camera.read = raise_read_error

    monkeypatch.setattr(
        "shooting_range.services.camera_service.cv2.VideoCapture",
        lambda index: fake_camera,
    )

    camera = CameraService()

    assert camera.connect() is True
    assert camera.get_frame() is None
    assert fake_camera.released is True
    assert camera.is_connected() is False

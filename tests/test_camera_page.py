import os

os.environ["QT_QPA_PLATFORM"] = "offscreen"

import pytest
from PySide6.QtWidgets import QApplication

from shooting_range.ui.camera_page import CameraPage


@pytest.fixture(scope="session")
def app():
    """Create a shared QApplication instance for UI tests."""
    application = QApplication.instance() or QApplication([])
    yield application


@pytest.fixture
def camera_page(app):
    """Create a fresh camera page for each test."""
    page = CameraPage()
    yield page

    page.disconnect_camera()
    page.close()


def test_camera_page_initializes_disconnected(camera_page):
    """Verify that camera page starts in a disconnected state."""
    assert camera_page.status.text() == "Disconnected"
    assert camera_page.connect_button.isEnabled()
    assert not camera_page.disconnect_button.isEnabled()


def test_camera_page_connects_mock_camera(camera_page):
    """Verify that mock camera can connect through the UI."""
    camera_page.camera_selector.setCurrentText("Mock Camera")
    camera_page.connect_camera()

    assert camera_page.active_camera is camera_page.mock_camera
    assert camera_page.status.text() == "Connected"
    assert camera_page.timer.isActive()
    assert camera_page.disconnect_button.isEnabled()


def test_camera_page_disconnects_camera(camera_page):
    """Verify that camera can be disconnected through the UI."""
    camera_page.camera_selector.setCurrentText("Mock Camera")
    camera_page.connect_camera()
    camera_page.disconnect_camera()

    assert camera_page.active_camera is None
    assert camera_page.status.text() == "Disconnected"
    assert not camera_page.timer.isActive()
    assert camera_page.connect_button.isEnabled()
    assert not camera_page.disconnect_button.isEnabled()


def test_camera_page_handles_frame_failure(camera_page):
    """Verify that UI handles unavailable camera frames."""
    camera_page.camera_selector.setCurrentText("Mock Camera")
    camera_page.connect_camera()

    camera_page.active_camera.get_frame = lambda: None
    camera_page.update_frame()

    assert camera_page.active_camera is None
    assert camera_page.status.text() == "Camera disconnected"
    assert not camera_page.timer.isActive()


def test_camera_page_handles_invalid_frame(camera_page):
    """Verify that UI disconnects when camera returns an invalid frame."""
    import numpy as np

    camera_page.camera_selector.setCurrentText("Mock Camera")
    camera_page.connect_camera()

    camera_page.active_camera.get_frame = lambda: np.zeros((100, 100))

    camera_page.update_frame()

    assert camera_page.active_camera is None
    assert camera_page.status.text() == "Invalid camera frame"
    assert not camera_page.timer.isActive()


def test_camera_page_handles_disconnect_error(camera_page):
    """Verify that UI resets even when camera disconnection fails."""
    camera_page.camera_selector.setCurrentText("Mock Camera")
    camera_page.connect_camera()

    def raise_error():
        raise RuntimeError("Simulated disconnection failure")

    camera_page.active_camera.disconnect = raise_error
    camera_page.disconnect_camera()

    assert camera_page.active_camera is None
    assert camera_page.status.text() == "Disconnected"
    assert not camera_page.timer.isActive()
    assert camera_page.connect_button.isEnabled()

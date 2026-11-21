# Changelog

All notable changes to this project are documented in this file.

The format is based on Keep a Changelog.

## [Unreleased]

### Added
- Initial desktop application structure using PySide6.
- Main application window with sidebar navigation.
- Camera Preview interface.
- Camera source selection between Mock Camera and Physical Camera.
- MockCameraService for generating synthetic camera frames.
- CameraService for physical camera integration.
- Centralized application logging with rotating file support.
- Uncaught exception logging.
- Automated service and UI tests using Pytest.
- Project architecture documentation.
- Development guide.
- Testing documentation.

### Changed
- Improved Camera Preview interface styling.
- Added separate camera service handling for mock and physical sources.
- Improved camera connection and disconnection handling.
- Added camera frame validation and error handling.
- Improved camera resource cleanup when errors occur.
- Added logging for camera connection, disconnection, and processing errors.

### Tested
- Mock camera connection and disconnection.
- Synthetic camera frame generation.
- Physical camera connection using a simulated device.
- Handling of unavailable camera devices.
- Handling of camera connection and frame retrieval errors.
- Camera Page initialization and connection controls.
- Handling of unavailable and invalid camera frames.
- UI recovery after camera disconnection errors.
- Manual camera preview testing using a physical webcam.
- All 14 automated tests passed.

### Planned
- Additional physical camera hardware integration testing.
- Application startup and shutdown testing.
- Expanded UI and regression testing.
- Application packaging and distribution.

---

## Versioning

The project has not yet reached its first official release.

Version numbers will be assigned when a stable release is prepared.
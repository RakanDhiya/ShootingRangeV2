# Testing Documentation

## 1. Overview

This document describes the testing procedures and current test coverage for the ShootingRangeV2 application.

The project uses Pytest to verify camera services and camera preview interface behavior.

## 2. Testing Environment

| Component | Version / Configuration |
|---|---|
| Operating System | Windows |
| Python | 3.11.5 |
| Pytest | 9.2.0 |
| OpenCV | 5.1.0 |
| PySide6 | Installed |
| Test Framework | Pytest |

## 3. Testing Scope

The current testing scope covers camera services and the Quick Start camera interface.

### Mock Camera Service
- Verify the initial disconnected state.
- Verify successful connection.
- Verify frame generation.
- Verify successful disconnection.

### Physical Camera Service
- Verify camera connection using a simulated device.
- Verify frame retrieval.
- Verify handling of unavailable camera devices.
- Verify handling of connection errors.
- Verify handling of frame retrieval errors.
- Verify camera resource release.

### Camera Page Interface
- Verify initial disconnected state.
- Verify mock camera connection through the interface.
- Verify camera disconnection through the interface.
- Verify handling of unavailable camera frames.
- Verify handling of invalid camera frames.
- Verify UI recovery when camera disconnection raises an exception.

## 4. Test Execution

Activate the project's virtual environment and configure the Python module path.

```powershell
$env:PYTHONPATH = "src"
python -m pytest -v
```

The UI tests use Qt's offscreen platform to allow automated testing without displaying application windows.

## 5. Test Results

Latest test execution:

| Test Module | Test Cases | Result |
|---|---:|---|
| Camera Service | 8 | PASSED |
| Camera Page | 6 | PASSED |
| **Total** | **14** | **PASSED** |

### Summary

- Total test cases: 14
- Passed: 14
- Failed: 0
- Skipped: 0

**Overall Result: ALL TESTS PASSED**

## 6. Testing Limitations

Physical camera service tests currently use a simulated video capture device (`FakeVideoCapture`).

Camera Page tests verify interface behavior using the mock camera service.

Actual physical camera integration has been manually verified using a webcam. Automated testing with different physical camera devices has not yet been performed.

## 7. Future Testing

The following testing activities are planned:

- Physical camera integration testing across different devices.
- Camera preview interface testing under different display conditions.
- Application startup and shutdown testing.
- Additional error handling and recovery testing.
- Regression testing after code changes.

---

Last updated: November 2026
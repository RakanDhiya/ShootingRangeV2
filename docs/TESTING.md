
# Testing Documentation

## 1. Overview

This document describes the testing procedures for the ShootingRangeV2 application.

The project uses Pytest as its primary testing framework to verify the behavior of application services.

## 2. Testing Environment

| Component | Version / Configuration |
|---|---|
| Operating System | Windows |
| Python | 3.11.5 |
| Pytest | 9.2.0 |
| OpenCV | 5.1.0 |
| Test Framework | Pytest |

## 3. Testing Scope

The current testing scope focuses on camera service functionality.

### Mock Camera Service
- Verify the initial disconnected state.
- Verify successful connection.
- Verify frame generation.
- Verify successful disconnection.

### Physical Camera Service
- Verify camera connection using a simulated device.
- Verify frame retrieval.
- Verify handling of unavailable camera devices.
- Verify camera resource release.

## 4. Test Execution

Activate the project's virtual environment and configure the Python module path.

```powershell
$env:PYTHONPATH = "src"
python -m pytest -v
```

## 5. Test Results

Latest test execution:

| Test Case | Result |
|---|---|
| Mock camera starts disconnected | PASSED |
| Mock camera connects successfully | PASSED |
| Mock camera disconnects successfully | PASSED |
| Physical camera connects successfully | PASSED |
| Physical camera handles unavailable device | PASSED |

### Summary

- Total test cases: 5
- Passed: 5
- Failed: 0
- Skipped: 0

**Overall Result: ALL TESTS PASSED**

## 6. Testing Limitations

Physical camera tests currently use a simulated video capture device (`FakeVideoCapture`).

Actual hardware integration has not yet been verified because a physical camera is not available during this testing stage.

## 7. Future Testing

The following testing activities are planned:

- Physical camera integration testing.
- Camera preview interface testing.
- Application startup testing.
- Error handling and recovery testing.
- Regression testing after code changes.

---

Last updated: November 2026
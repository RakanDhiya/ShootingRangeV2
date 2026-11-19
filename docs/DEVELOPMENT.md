
# Development Guide

## 1. Introduction

This document provides development guidelines for the ShootingRangeV2 project.

It describes the development environment, installation procedures, application execution, coding standards, and recommended development practices.

## 2. Development Environment

The project currently uses the following technologies:

| Technology | Purpose |
|---|---|
| Python 3.11.5 | Main programming language |
| PySide6 | Desktop application interface |
| OpenCV | Image and video processing |
| NumPy | Numerical operations and frame generation |
| Pytest | Automated testing |

Development is currently performed on Windows using PowerShell.

## 3. Project Setup

### Prerequisites

Before starting development, ensure that Python is installed on your system.

### Create Virtual Environment

```powershell
python -m venv .venv
```

### Activate Virtual Environment

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
pip install -r requirements.txt
```

## 4. Running the Application

Configure the Python module path:

```powershell
$env:PYTHONPATH = "src"
```

Start the application:

```powershell
python -m shooting_range.main
```

## 5. Running Tests

Execute the automated test suite:

```powershell
python -m pytest -v
```

Run a specific test file:

```powershell
python -m pytest tests/test_camera_service.py -v
```

## 6. Coding Standards

The project follows these coding practices:

### Naming Conventions

- Classes use PascalCase.
- Functions and methods use snake_case.
- Variables use descriptive snake_case names.
- Constants use UPPER_SNAKE_CASE.

### Documentation

- Every class should have a descriptive docstring.
- Important methods should explain their purpose.
- Parameters and return values should be documented when useful.
- Comments should explain important implementation decisions.
- Avoid unnecessary comments that repeat the code.

### Code Organization

- Keep user interface code inside the `ui` package.
- Keep service logic inside the `services` package.
- Keep application initialization inside the `core` package.
- Place automated tests inside the `tests` directory.
- Avoid placing unrelated responsibilities inside a single class.

## 7. Development Workflow

Recommended development process:

1. Understand the existing module before modifying it.
2. Implement one feature or improvement at a time.
3. Keep responsibilities separated between modules.
4. Add or update automated tests when behavior changes.
5. Run the test suite after modifications.
6. Update project documentation when necessary.

## 8. Development Notes

- Use MockCameraService when a physical camera is unavailable.
- Use CameraService for physical camera integration.
- Do not assume simulated camera tests guarantee compatibility with all physical camera devices.
- Keep the existing application structure consistent when adding new modules.

---

Last updated: November 2026
# ShootingRangeV2

Desktop application built with Python, PySide6, and OpenCV.

## Overview

ShootingRangeV2 is a desktop application project focused on desktop interface development, camera integration, device connectivity, and application management.

The application is developed using a modular architecture to maintain code readability, maintainability, and extensibility.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Main programming language |
| PySide6 | Desktop GUI framework |
| OpenCV | Camera and video processing |
| Pytest | Automated testing |

## Current Features

- Main application window
- Sidebar navigation
- Dashboard interface
- Camera preview page
- Camera service foundation
- Application settings page placeholder

## Planned Features

- Mock camera mode for UI testing
- Real camera integration
- Camera connection status
- Improved dashboard
- Application configuration
- Automated testing

## Project Structure

```text
ShootingRangeV2/
├── assets/
│   └── images/
├── src/
│   └── shooting_range/
│       ├── config/
│       ├── core/
│       ├── services/
│       ├── ui/
│       │   └── styles/
│       └── utils/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ShootingRangeV2
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Windows PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m shooting_range.main
```

## Development Guidelines

- Keep UI components separate from application services.
- Avoid placing business logic directly inside UI classes.
- Use reusable components where appropriate.
- Keep functions and classes focused on a single responsibility.
- Test new features before integrating them into the application.
- Update documentation whenever application behavior or architecture changes.

## Project Status

**Development in progress.**

The application currently has its initial desktop interface and camera service foundation. Additional features will be implemented and tested incrementally.

## License

To be determined.
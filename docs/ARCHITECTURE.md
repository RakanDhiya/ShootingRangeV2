# Software Architecture

## 1. Overview

ShootingRangeV2 is a desktop application developed using Python and PySide6.

The application follows a modular architecture that separates presentation components, application management, configuration, and service logic.

This architecture is designed to improve code organization, maintainability, readability, and testability. Each module has a specific responsibility, allowing individual components to be developed, tested, and maintained independently.

## 2. Architecture Structure

The application is organized into the following main layers.

### 2.1 Presentation Layer

**Location:** `src/shooting_range/ui/`

The Presentation Layer is responsible for displaying the application interface and handling user interactions.

Current components:

- `main_window.py`: Implements the main application window, navigation, dashboard, and page management.
- `camera_page.py`: Provides the camera preview interface and manages camera source selection.
- `styles/`: Contains application stylesheet resources.

### 2.2 Service Layer

**Location:** `src/shooting_range/services/`

The Service Layer handles application services and communication with external devices.

Current components:

- `camera_service.py`: Manages physical camera connections, frame retrieval, and resource release using OpenCV.
- `mock_camera_service.py`: Generates synthetic camera frames without requiring a physical camera device.

Both camera services provide a consistent interface, allowing the presentation layer to interact with different camera sources through a similar workflow.

### 2.3 Core Layer

**Location:** `src/shooting_range/core/`

The Core Layer manages application initialization and lifecycle execution.

Current component:

- `app.py`: Creates the QApplication instance, configures the application name, initializes the main window, and starts the application event loop.

### 2.4 Configuration Layer

**Location:** `src/shooting_range/config/`

The Configuration Layer stores centralized application settings used across different modules.

Current component:

- `settings.py`: Defines shared application configuration values, including application name, default camera index, camera update interval, and preview dimensions.

Centralized configuration reduces hardcoded values and makes application settings easier to maintain.

### 2.5 Utility Layer

**Location:** `src/shooting_range/utils/`

The Utility Layer is reserved for reusable helper functions and shared utilities.

Additional utility modules can be introduced as the application grows.

## 3. Configuration Management

Application settings are centralized in:

`src/shooting_range/config/settings.py`

The current configuration includes:

| Configuration | Description |
|---|---|
| `APP_NAME` | Application name |
| `DEFAULT_CAMERA_INDEX` | Default physical camera device index |
| `CAMERA_FRAME_INTERVAL_MS` | Camera preview update interval in milliseconds |
| `PREVIEW_WIDTH` | Mock camera frame width |
| `PREVIEW_HEIGHT` | Mock camera frame height |

Centralized configuration provides a single location for managing shared application settings and helps maintain consistency across modules.

## 4. Application Structure

The current project structure is organized as follows:

```text
ShootingRangeV2/
├── assets/
│   └── images/
├── docs/
│   ├── ARCHITECTURE.md
│   └── TESTING.md
├── src/
│   └── shooting_range/
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py
│       ├── core/
│       │   ├── __init__.py
│       │   └── app.py
│       ├── services/
│       │   ├── __init__.py
│       │   ├── camera_service.py
│       │   └── mock_camera_service.py
│       ├── ui/
│       │   ├── styles/
│       │   │   └── main.qss
│       │   ├── __init__.py
│       │   ├── camera_page.py
│       │   └── main_window.py
│       ├── utils/
│       │   └── __init__.py
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_camera_service.py
├── requirements.txt
├── .gitignore
├── CHANGELOG.md
└── README.md
```

## 5. Camera Service Workflow

The camera preview feature currently supports two camera sources:

1. Mock Camera
2. Physical Camera

The `CameraPage` component allows users to select the desired camera source.

Each camera service provides the following methods:

- `connect()`: Establishes the camera connection.
- `get_frame()`: Retrieves the latest available frame.
- `disconnect()`: Releases the camera resource.
- `is_connected()`: Checks the current connection state.

The Mock Camera generates synthetic image frames for development and interface testing, while the Physical Camera Service uses OpenCV to access an actual camera device.

This approach keeps camera-related operations separated from the presentation layer.

## 6. Camera Preview Data Flow

The camera preview process follows this workflow:

```text
User
 |
 v
CameraPage
 |
 v
Camera Source Selection
 |
 +----------------------+
 |                      |
 v                      v
MockCameraService   CameraService
 |                      |
 v                      v
Synthetic Frames    Physical Frames
 |                      |
 +----------+-----------+
            |
            v
       update_frame()
            |
            v
      OpenCV Conversion
            |
            v
       QImage / QPixmap
            |
            v
      Camera Preview UI
```

The `CameraPage` periodically requests a frame from the active camera service using a QTimer.

The retrieved frame is converted from OpenCV's BGR format into RGB format. It is then converted into a QImage and displayed as a QPixmap inside the preview interface.

## 7. Testing Architecture

The project uses pytest to verify camera service behavior.

Current automated tests cover:

- Mock camera initial state.
- Mock camera connection.
- Mock camera frame generation.
- Mock camera disconnection.
- Physical camera connection using a simulated device.
- Handling unavailable physical camera devices.

Physical camera service tests use a `FakeVideoCapture` implementation to simulate camera behavior without requiring physical hardware.

Tests can be executed using:

```powershell
python -m pytest -v
```

This testing approach allows core camera service behavior to be verified independently of the graphical interface and physical camera hardware.

## 8. Design Principles

The application follows these software design principles:

- **Separation of Concerns:** Each module has a clearly defined responsibility.
- **Modularity:** Application features are organized into independent components.
- **Reusability:** Services can be reused by different interface components.
- **Testability:** Service logic can be tested independently.
- **Maintainability:** Consistent structure and documentation simplify future development.
- **Centralized Configuration:** Shared settings are maintained in a dedicated configuration module.

## 9. Future Architecture Improvements

Potential improvements for future development include:

- More comprehensive error handling and logging.
- Dedicated service interfaces and abstractions.
- Additional automated UI tests.
- Improved camera resource management.
- Application packaging and deployment.
- Expanded technical documentation.

These improvements will be considered as the application develops and its requirements become more extensive.

---

**Last Updated:** November 2026  
**Project:** ShootingRangeV2  
**Architecture:** Modular Desktop Application
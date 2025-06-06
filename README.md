# AI Virtual Mouse

## Overview

AI Virtual Mouse is an innovative, AI-driven virtual mouse system developed to enhance Human-Computer Interaction (HCI) through a *touch-free* and *hygienic interface*. It empowers users with mobility impairments and addresses hygiene-critical environments by providing precise cursor control via hand gestures.

## Key Features

- **Real-time Hand Tracking & Gesture Recognition**
  - Uses MediaPipe and OpenCV for robust hand landmark detection.
  - Precise gesture recognition for intuitive cursor control and clicking actions.

- **Seamless Cursor Control**
  - Smooth, low-latency tracking with FPS optimization for real-time performance.
  - Cursor movement smoothed by interpolation for fluid user experience.

- **Accessibility-Focused Design**
  - Predicted to benefit over 15% of users with physical disabilities.
  - Offers a safer, contact-free alternative addressing hygiene concerns.

- **Scalable & Optimized Architecture**
  - Modular structure for ease of maintenance and extensibility.
  - Efficient video frame processing to avoid performance bottlenecks.

## Installation & Usage

### Prerequisites

- Python 3.8+
- Required Python packages:
  - `opencv-python`
  - `mediapipe`
  - `numpy`
  - `pyautogui`

### Setup

1. Clone the repository or download the project files.
2. Navigate to the `VirtualMouse` directory.
3. Install dependencies using pip:

   ```bash
     pip install opencv-python mediapipe numpy pyautogui
   ```

### Running the Application
Run the AI Virtual Mouse script

   ```bash
     python AIVirtualMouse.py
   ```

Use your webcam to control the mouse cursor with your hand:

- Index finger raised to move the cursor.
- Index and middle fingers raised and pinched to perform a click.

## Technologies Used

| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white) | ![MediaPipe](https://img.shields.io/badge/MediaPipe-FF6F00?style=for-the-badge&logo=mediapipe&logoColor=white) | ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) |
|---|---|---|---|
| ![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-4B8BBE?style=for-the-badge&logo=python&logoColor=white) | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) |

- Python (main programming language)
- OpenCV (computer vision library)
- MediaPipe (hand tracking and gesture recognition)
- NumPy (numerical operations)
- PyAutoGUI (automating GUI interactions)
- Git & GitHub (version control)
- Virtual Environment (dependency isolation)

## Project Structure
```text
├── VirtualMouse/                # Main directory for the AI Virtual Mouse project
│   ├── AIVirtualMouse.py        # Core script for virtual mouse functionality
│   ├── HandTrackingModule.py     # Module for hand tracking and gesture recognition
│   ├── __pycache__/              # Compiled Python files
│   ├── .idea/                    # IDE configuration files
│   ├── .gitignore                # Files to ignore in version control
│   └── README.md                 # Project documentation
│
├── ImageProcessing/              # Supporting image processing related code
│   └── HandTrackingMin.py        # Basic hand tracking functionality
│
├── pythonProject/                # Miscellaneous project scripts and tests
│   └── main.py                   # Sample entry point for testing
│
└── requirements.txt              # List of dependencies for the project
```

## Technical Overview
1. Video Capture: Utilizes OpenCV for continuous webcam feed.
2. Hand Detection: MediaPipe processes frames to detect and locate hand landmarks.
3. Gesture Logic: Customized algorithms interpret finger states to control mouse actions.
4. Cursor Control: Coordinates are smoothed and mapped to screen dimensions with NumPy.
5. User Feedback: Real-time FPS displayed on screen for performance insight.

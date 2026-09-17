# PROJECT TITLE: Real-Time Road Sign Detection, Alert & Analytics System

A Computer Vision-based road sign detection system that uses a trained YOLOv8n object detection model to detect traffic signs from webcam and video input, generate stop-sign alerts, store detection data, and visualize detection statistics through an analytics dashboard.

## 1. Project Overview

Road signs provide important information to drivers and help maintain road safety. 
The project fine-tunes YOLOv8 on the [Kaggle Road Sign Detection dataset](https://www.kaggle.com/datasets/andrewmvd/road-sign-detection) and deploys the trained model in a live detection loop that runs on a webcam or video file.Detecting these signs automatically from images or video can support intelligent transportation and driver-assistance applications.

## 2. Features
The system:

- Detects road signs using YOLOv8n
- Supports webcam and video input
- Draws bounding boxes around detected signs
- Displays class labels and confidence scores
- Generates an alert when a stop sign is detected
- Logs detected signs and confidence values into SQLite
- Provides an analytics dashboard using Streamlit
- Displays detection statistics and detection timelines

## 3. Problem Statement

Manual identification of road signs from continuous video footage is difficult and cannot provide automated real-time assistance.

The objective of this project is to develop a Computer Vision system that can automatically detect selected road signs from images and video, provide alerts for important signs such as stop signs, and maintain detection records for analysis.

## 4. Objectives

- Detect road signs automatically using Computer Vision.
- Apply YOLOv8n for object detection.
- Process webcam and video input.
- Display bounding boxes and confidence scores.
- Generate alerts for detected stop signs.
- Store detection information in a database.
- Provide visual analytics through a dashboard.
- Maintain a modular and testable project structure.

## 5. Detected Classes

The trained model detects four road-sign classes:

| Class | Description |
|---|---|
| `trafficlight` | Traffic light |
| `stop` | Stop sign |
| `speedlimit` | Speed limit sign |
| `crosswalk` | Crosswalk sign |

## 6. Architecture

```
Module 1: Data & Training          Module 2: Live Detection        Module 3: Analytics
------------------------           -------------------------       --------------------
Kaggle dataset                     Webcam / video file
     |                                    |
VOC -> YOLO conversion             YOLOv8 inference (best.pt)
     |                                    |            \
YOLOv8 training  ---> best.pt ----------->|             \--> alert.py (stop-sign alert)
                                            |
                                     storage/db.py (log each detection)
                                            |
                                     analytics/dashboard.py (summary + charts)
```

## 7. System Modules

### Module 1 – YOLOv8n Road Sign Detection

- Loads the trained `best.pt` model.
- Processes image/video frames.
- Detects road-sign objects.
- Generates bounding boxes.
- Calculates confidence scores.

### Module 2 – Live Detection & Alert System

- Supports webcam input.
- Supports video input.
- Displays detections in real time.
- Generates a stop-sign alert.
- Uses configurable confidence and alert settings.

### Module 3 – Logging & Analytics

- Stores detected classes.
- Stores confidence scores.
- Records detection timestamps.
- Uses SQLite for data storage.
- Applies temporal logging to reduce repeated entries.
- Provides detection statistics through Streamlit.

## 6. System Architecture

```text
             Webcam / Video Input
                     |
                     v
          Live / Video Detection
                     |
                     v
                YOLOv8n
                     |
                     v
        Detection Results
      (Class + Confidence)
             /             \
            /               \
           v                 v
    Stop Sign Alert     SQLite Database
                              |
                              v
                     Analytics Dashboard
```

## 7. Project Structure

```text
road_sign_detection/
│
├── analytics/
│   └── dashboard.py
│
├── config/
│   ├── config.py
│   └── __init__.py
│
├── data/
│   └── test_video.mp4
│
├── detector/
│   ├── alert.py
│   ├── live_detect.py
│   ├── video_detect.py
│   └── __init__.py
│
├── models/
│   └── best.pt
│
├── outputs/
│
├── storage/
│   ├── db.py
│   └── __init__.py
│
├── tests/
│   ├── camera_test.py
│   ├── test_database.py
│   └── __init__.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 8. Technologies Used

- Python
- OpenCV
- YOLOv8n
- Ultralytics
- SQLite
- Streamlit
- Pandas
- Plotly
- Git & GitHub

## 9. Installation and setup

### Prerequisites

- Python 3.x
- Webcam (for live detection)
- Git
- Windows/Linux/macOS

### Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/road-sign-detection.git
cd road-sign-detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## 10. Running the Project

### A. Test the Camera

From the project root:

```bash
python -m tests.camera_test
```

The camera window should open.

Press:

```text
q
```

to close it.

### B. Run Live Road Sign Detection

```bash
python -m detector.live_detect
```

The webcam will open and detected signs will be displayed with:

- Bounding boxes
- Class labels
- Confidence scores

A stop-sign detection generates an alert.

Press:

```text
q
```

to stop detection.

### C. Run Video Detection

```bash
python -m detector.video_detect
```

When prompted, enter:

```text
data/test_video.mp4
```

The system will process the video and display detected road signs.

Press:

```text
q
```

or:

```text
Esc
```

to stop the video.

### D. Run the Analytics Dashboard

From the project root:

```bash
streamlit run analytics/dashboard.py
```

The dashboard displays:

- Total detections
- Average confidence
- Stop-sign detections
- Detection count by class
- Detection timeline
- Recent detection records

## 11. Database

The project uses SQLite to store detection information.

Each detection contains:

```text
id
class_name
confidence
timestamp
```

Example:

```text
stop | 0.9569 | 2026-09-16 21:05:23
speedlimit | 0.5343 | 2026-09-16 21:12:29
trafficlight | 0.6274 | 2026-09-16 21:05:02
```

Repeated detections of the same class within a short time interval are reduced using temporal logging.

## 12. Testing

The project includes basic testing modules.

### Camera Test

```bash
python -m tests.camera_test
```

### Database Test

```bash
python -m tests.test_database
```

The database test verifies:

- Database creation
- Detection insertion
- Detection retrieval

## 14. Non-Functional Requirements

### Performance

The system should process video frames efficiently and provide suitable inference speed for practical use.

### Usability

The system provides simple commands for running webcam detection, video detection, and the analytics dashboard.

### Reliability

The system handles invalid camera/video input and checks whether input sources can be opened.

### Maintainability

The project is divided into separate modules for detection, alerts, configuration, storage, analytics, and testing.

### Resource Efficiency

YOLOv8n is used as a lightweight object-detection model suitable for comparatively resource-efficient inference.

### Error Handling

The system checks for:

- Camera availability
- Video availability
- Frame-reading failures
- Database availability

## 14. Design Decisions

### YOLOv8n

YOLOv8n was selected because it provides object detection while remaining relatively lightweight for real-time applications.

### SQLite

SQLite was selected because the project requires lightweight local storage without requiring a separate database server.

### Streamlit

Streamlit was used to create the analytics dashboard quickly while keeping the application architecture simple.

### Modular Architecture

Detection, alert handling, database operations, configuration, analytics, and testing are maintained as separate modules to improve maintainability and readability.

## 15. References

- Ultralytics YOLO Documentation
- Dataset: Larxel, *Road Sign Detection*, Kaggle,
  https://www.kaggle.com/datasets/andrewmvd/road-sign-detection
- OpenCV Documentation
- Python Documentation
- Streamlit Documentation
- GitHub Documentation
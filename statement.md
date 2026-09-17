# Project Statement

## 1. Problem Statement

Manual identification of road signs from continuous video footage is difficult and cannot provide automated real-time assistance.

The objective of this project is to develop a Computer Vision system that can automatically detect selected road signs from images and video, provide alerts for important signs such as stop signs, and maintain detection records for analysis.

## 2. Project Scope

The project focuses on real-time and video-based detection of four road-sign categories:

- Traffic Light
- Stop Sign
- Speed Limit
- Crosswalk

The system accepts webcam or pre-recorded video as input and performs object detection using the trained YOLOv8n model.

The project includes:

- Road sign detection
- Bounding box visualization
- Confidence score display
- Stop sign alert generation
- Detection logging using SQLite
- Detection analytics using a Streamlit dashboard

The project is intended as a computer vision prototype and does not replace certified vehicle safety or driver-assistance systems.

## 3. Target Users

The system can be useful for:

- Computer Vision students and learners
- AI/ML students working on object detection
- Researchers developing traffic-sign detection systems
- Developers experimenting with real-time object detection
- Academic projects and demonstrations

## 4. High-Level Features

- **Road Sign Detection** — Detects selected road signs using YOLOv8n.
- **Real-Time Detection** — Supports webcam-based detection.
- **Video Detection** — Processes pre-recorded road-sign videos.
- **Bounding Box Visualization** — Displays detected signs with bounding boxes.
- **Confidence Display** — Shows the confidence score for each detection.
- **Stop Sign Alert** — Generates an alert when a stop sign is detected.
- **Detection Logging** — Stores class, confidence, and timestamp information in SQLite.
- **Analytics Dashboard** — Displays detection statistics and visualizations.
- **Detection Timeline** — Shows detections over time.
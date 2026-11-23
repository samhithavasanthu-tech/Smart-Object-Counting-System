# SMART OBJECT COUNTING SYSTEM USING COMPUTER VISION

## Visual Computing Project Report

## 1. Abstract

The Smart Object Counting System is a real-time computer vision application that detects, tracks, and counts objects using a webcam. The system uses YOLOv8n for object detection, ByteTrack for object tracking, and OpenCV for video processing.

A virtual counting line is used to detect objects moving in upward and downward directions. The system displays object names, tracking IDs, total counts, direction-wise counts, and FPS. Counting events are also stored in a CSV file with timestamps.

## 2. Introduction

Computer vision enables computers to understand and analyze images and videos. Object detection and counting are useful in traffic monitoring, crowd management, security, and industrial applications.

Manual counting is time-consuming and prone to errors. This project automates object detection, tracking, and counting using a webcam and computer vision techniques.

## 3. Problem Statement

Manual counting of moving objects is difficult, especially when multiple objects are moving simultaneously. This project aims to develop an automated system that detects, tracks, and counts objects crossing a predefined line in real time.

## 4. Objectives

- Detect objects in real-time video.
- Identify multiple object categories.
- Track objects using unique IDs.
- Count objects crossing a virtual line.
- Detect upward and downward movement.
- Display class-wise counts.
- Calculate and display FPS.
- Store counting events in a CSV file.

## 5. Technologies Used

- Python
- OpenCV
- YOLOv8n
- Ultralytics
- ByteTrack
- NumPy
- CSV
- Webcam
- Visual Studio Code

## 6. Hardware and Software Requirements

### Hardware
- Laptop or desktop computer
- Webcam
- Minimum 4 GB RAM

### Software
- Windows OS
- Python 3
- Visual Studio Code
- OpenCV
- Ultralytics YOLO

## 7. System Architecture

Webcam Input
       ↓
Video Frame Capture
       ↓
YOLO Object Detection
       ↓
ByteTrack Object Tracking
       ↓
Virtual Line Crossing Detection
       ↓
Direction-Based Counting
       ↓
Display Results and FPS
       ↓
CSV Logging

## 8. Methodology

### 8.1 Video Capture
The webcam captures live video frames continuously.

### 8.2 Object Detection
YOLOv8n detects objects in each frame and identifies their categories.

### 8.3 Object Tracking
ByteTrack assigns tracking IDs to detected objects to track their movement across frames.

### 8.4 Virtual Counting Line
A horizontal line is drawn on the video frame to identify object movement.

### 8.5 Direction Detection
The system compares the previous and current positions of tracked objects.

- Down: Top-to-bottom movement.
- Up: Bottom-to-top movement.

### 8.6 Counting
When an object crosses the virtual line, the corresponding directional counter is updated.

### 8.7 FPS Calculation
Frames per second are calculated to measure processing performance.

### 8.8 CSV Logging
The system stores the object category, direction, and timestamp of crossing events in a CSV file.

## 9. Features

- Real-time object detection
- Multi-class object recognition
- Object tracking IDs
- Direction-based counting
- Upward and downward counters
- Class-wise counting
- Virtual counting line
- FPS display
- CSV logging
- Reset counts using R key
- Exit using Q key

## 10. Results

The system successfully detects and tracks objects from live webcam video.

Bounding boxes are displayed around detected objects. Each object is assigned a tracking ID. When an object crosses the virtual line, the system updates the appropriate counter based on its movement direction.

The application displays object categories, directional counts, class-wise counts, and FPS.

Counting events can be saved in CSV format for further analysis.

## 11. Applications

- Traffic monitoring
- Pedestrian counting
- Shopping malls
- Crowd management
- Smart city systems
- Parking monitoring
- Industrial monitoring
- Security surveillance

## 12. Advantages

- Reduces manual counting effort.
- Provides real-time results.
- Tracks objects across frames.
- Counts objects based on direction.
- Supports multiple object classes.
- Stores results for analysis.
- Uses open-source technologies.

## 13. Limitations

- Performance depends on lighting conditions.
- Occlusion may affect detection and tracking.
- Small objects may not be detected accurately.
- Performance depends on system hardware.
- Tracking errors may cause inaccurate counting.

## 14. Future Enhancements

- Multiple counting lines.
- Graphical dashboard.
- Database integration.
- Daily and monthly reports.
- Alert system.
- GPU acceleration.
- Video file processing.
- Improved counting accuracy.

## 15. Conclusion

The Smart Object Counting System demonstrates the practical application of computer vision for real-time object detection, tracking, and counting.

By combining YOLOv8n, ByteTrack, and OpenCV, the system detects objects, tracks their movement, and counts objects crossing a virtual line.

The project provides directional counting, class-wise counting, FPS monitoring, and CSV logging. It demonstrates the usefulness of computer vision in traffic monitoring, crowd analysis, and smart surveillance applications.

## 16. References

1. Ultralytics YOLO Documentation:
   https://docs.ultralytics.com/

2. OpenCV Documentation:
   https://docs.opencv.org/

3. Python Documentation:
   https://docs.python.org/3/

4. ByteTrack GitHub Repository:
   https://github.com/ifzhang/ByteTrack
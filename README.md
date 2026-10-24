![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.13+-green.svg)
![YOLO](https://img.shields.io/badge/YOLOv8-8.4+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Pedestrian counting using YOLOv8 and OpenCV, with line-crossing detection and performance evaluation**

# Metro Exit Counter 🚇

A computer-vision project that detects and tracks pedestrians and counts their crossings over a virtual line using YOLO and OpenCV.

## Overview

Metro Exit Counter explores how object detection and multi-object tracking can be used for pedestrian-flow monitoring.

The project uses a pretrained YOLO model to detect people and ByteTrack to maintain track IDs across video frames. A virtual line is used to count tracked people as they cross.

## Features

- Pedestrian detection using YOLO
- Object tracking using ByteTrack
- Virtual line-crossing counter
- Webcam and video-file input
- Live count and approximate processing FPS
- Keyboard controls to quit or reset

## Technology Stack

- Python
- Ultralytics YOLO
- OpenCV
- ByteTrack

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ORANGE14-11/metro-exit-counter.git
   cd metro-exit-counter
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python main.py
```

The default input is webcam `0`. To process a local video instead, change `SOURCE` in `main.py` to the video filename, for example:

```python
SOURCE = "test_video.mp4"
```

The YOLO model weights are downloaded automatically by Ultralytics if they are not available locally.

### Controls

| Key | Action |
|---|---|
| `Q` | Quit |
| `R` | Reset the count |

## Counting Method

1. Detect people in each frame.
2. Track detected people across frames.
3. Calculate each bounding box's vertical center.
4. Detect a crossing when the center moves from one side of the virtual line to the other.
5. Count each tracked ID at most once until the counter is reset.

## Limitations

- Tracking IDs may change when people are heavily occluded.
- Dense crowds can lead to missed detections or incorrect counts.
- A person who leaves and re-enters may receive a new ID.
- Processing speed depends on the hardware, video resolution, and model configuration.
- The current counter is a prototype and has not yet been validated against a labeled ground-truth dataset.

## Future Improvements

- Evaluate counting accuracy on labeled pedestrian videos.
- Compare different detection and tracking configurations.
- Add precision, recall, and counting-error metrics where appropriate.
- Test performance across different crowd densities and lighting conditions.
- Add automated tests and reproducible experiment scripts.

## Project Status

This project is under development. Performance claims and evaluation results will be added after controlled testing.

## Author

**Mita Nur**  
Computer Science and Technology student, Zhejiang Normal University

[GitHub Profile](https://github.com/ORANGE14-11)

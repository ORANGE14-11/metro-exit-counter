![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.13+-green.svg)
![YOLO](https://img.shields.io/badge/YOLOv8-8.4+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Real-time pedestrian counting system using YOLOv8 and OpenCV**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Demo](#demo) • [Applications](#applications)

</div>

---

## 📋 Overview

The **Metro Exit Counter** is a real-time computer vision system that detects and counts people as they cross a virtual line. Built with YOLOv8 and OpenCV, it achieves 30+ FPS on Mac M5 and can be used for metro stations, retail stores, crowd management, and security applications.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎯 **Real-time Detection** | Detects people instantly using YOLOv8 |
| 📊 **Automatic Counting** | Counts each person crossing the virtual line |
| 🟢 **Visual Feedback** | Green flash animation on every count |
| 🎮 **Interactive Controls** | Reset counter, quit, or save screenshots |
| 💻 **High Performance** | Optimized for Apple Silicon (M1/M2/M3/M5) |
| 📸 **Screenshot Capture** | Save frames with 's' key |

---

## 🖼️ Demo
┌─────────────────────────────────────┐
│ EXITS: 042 │
│ │
│ ┌─────┐ │
│ │Person│ │
│ └─────┘ │
│ ━━━━━━━━━━━━━━━━━━━ │ ← Counting Line (RED)
│ │
│ Q=Quit | R=Reset | S=Screenshot │
└─────────────────────────────────────┘

text

*Actual demo video coming soon! Run the program to see it in action.*

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Git
- Webcam (optional - works with video files too)

### Step 1: Clone the Repository

```bash
git clone https://github.com/ORANGE14-11/metro-exit-counter.git
cd metro-exit-counter
Step 2: Create Virtual Environment

bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies

bash
pip install ultralytics opencv-python
Step 4: Run the Application

bash
python3 metro_counter.py
🎮 Usage Guide

Controls

Key	Action
q	Quit the program
r	Reset counter to zero
s	Save screenshot
How to Use

Position your camera so the counting line is visible
Walk from top to bottom crossing the red line
Watch the counter increase with a green flash
Press 'r' to reset and test again
Press 'q' to exit
Counting Logic

text
     TOP OF FRAME
          │
    ┌─────┴─────┐
    │   Person  │ ← Detected
    └─────┬─────┘
          │
    ══════▼══════  ← RED LINE (Counting Zone)
          │
    ┌─────▼─────┐
    │  Counted! │ ← +1
    └───────────┘
     BOTTOM OF FRAME
📁 Project Structure

text
metro-exit-counter/
│
├── metro_counter.py      # Main application (125+ lines)
├── README.md            # This file
├── requirements.txt     # Dependencies
├── .gitignore          # Git ignore rules
│
└── venv/               # Virtual environment (not tracked)
🔧 Technical Details

Architecture

python
1. Capture frame from camera/video
2. Run YOLOv8 detection (person class only)
3. Draw bounding boxes and tracking points
4. Check if person crosses virtual line
5. Increment counter with visual feedback
6. Display results in real-time
Performance

Metric	Value
FPS	30+ on Mac M5
Model Size	6.2 MB (YOLOv8n)
Detection Classes	Person only (class 0)
Processing	Every 2nd frame
Confidence Threshold	0.5
Technologies Used

YOLOv8 - State-of-the-art object detection
OpenCV - Video capture and image processing
Python - Core programming language
NumPy - Array operations
🎯 Real-World Applications

Industry	Use Case
🚇 Metro/Subway	Count passengers exiting stations
🏪 Retail	Track foot traffic and peak hours
🏢 Office Buildings	Monitor occupancy and flow
🎪 Events	Count attendees at entrances/exits
🔒 Security	Monitor restricted areas
📊 Urban Planning	Gather pedestrian data
🚧 Future Improvements

CSV Export - Save counting data with timestamps
Dashboard - Streamlit web interface with charts
Email Alerts - Notify when threshold reached
Direction Detection - Count entry vs exit separately
Multiple Lines - Count at different zones
Mobile App - Run on iOS/Android devices
Cloud Deployment - API endpoint for counting
🤝 Contributing

Contributions are welcome! Feel free to:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit changes (git commit -m 'Add AmazingFeature')
Push to branch (git push origin feature/AmazingFeature)
Open a Pull Request
📝 License

This project is licensed under the MIT License - see below:

text
MIT License

Copyright (c) 2026 ORANGE14-11

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
👨‍💻 Author

ORANGE14-11
Computer Science Student @ ZJNU

🔗 GitHub
📧 [Your Email]
🎓 ZJNU - Computer Science and Technology
⭐ Show Your Support

If this project helped you or inspired you:

⭐ Star this repository on GitHub
🐦 Share on social media
🔗 Link to it in your portfolio
🙏 Acknowledgments

Ultralytics for YOLOv8
OpenCV for computer vision tools
My professors and peers at ZJNU for support
<div align="center"> Made with 🚇 by ORANGE14-11 | ZJNU Computer Science </div> EOF ```
Now add it to git:

bash
git add README.md
git commit -m "Add professional README documentation"
Create requirements.txt:

bash
cat > requirements.txt << 'EOF'
ultralytics>=8.0.0
opencv-python>=4.8.0
numpy>=1.24.0
EOF

git add requirements.txt
git commit -m "Add requirements.txt for easy installation"
Create a simple .gitignore:

bash
cat > .gitignore << 'EOF'
# Virtual environment
venv/
env/
ENV/

# Python cache
__pycache__/
*.pyc
*.pyo

# Model files (optional - can download)
# yolov8n.pt

# Screenshots
*.png
*.jpg

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
EOF

git add .gitignore
git commit -m "Add .gitignore for cleaner repo"
Now push everything:

bash
git push -u origin main

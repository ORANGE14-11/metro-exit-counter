import cv2
from ultralytics import YOLO
import time
import urllib.request
import ssl

# Fix SSL certificate issue
ssl._create_default_https_context = ssl._create_unverified_context

print("="*50)
print("🚇 METRO EXIT COUNTER")
print("="*50)

# Check if model exists, download if needed
import os
if not os.path.exists('yolov8n.pt'):
    print("Downloading YOLO model...")
    urllib.request.urlretrieve('https://github.com/ultralytics/assets/releases/download/v8.4.0/yolov8n.pt', 'yolov8n.pt')
    print("✅ Model downloaded!")

# Load YOLO
print("Loading AI model...")
model = YOLO('yolov8n.pt')
print("✅ Model ready!")

# Try camera
print("\nOpening camera...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("\n📹 CAMERA NOT FOUND - Using test video instead")
    print("Downloading test video...")
    
    # Download test video
    video_url = "https://github.com/ultralytics/yolo-docs/raw/main/docs/videos/subway_walk.mp4"
    urllib.request.urlretrieve(video_url, "test_video.mp4")
    cap = cv2.VideoCapture('test_video.mp4')
    print("✅ Using test video")
else:
    print("✅ Camera ready!")

# Get frame size
ret, frame = cap.read()
if not ret:
    print("❌ Cannot read video")
    exit()

h, w = frame.shape[:2]
line_y = int(h * 0.6)
total_count = 0
crossed = set()

print(f"\n📐 Screen size: {w}x{h}")
print(f"📍 Counting line at Y={line_y}")
print("\n🎮 Controls: 'q'=quit, 'r'=reset")
print("🚶 People crossing the RED line will be counted\n")

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("\n🏁 Video ended - restarting...")
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    frame_count += 1
    
    # Draw red counting line
    cv2.line(frame, (0, line_y), (w, line_y), (0, 0, 255), 3)
    cv2.putText(frame, "COUNTING LINE", (w//2-80, line_y-10), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    # Detect people every few frames
    if frame_count % 3 == 0:
        results = model(frame, classes=[0], conf=0.5, verbose=False)
        
        if results[0].boxes is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            
            for box in boxes:
                x1, y1, x2, y2 = map(int, box[:4])
                center_y = (y1 + y2) // 2
                center_x = (x1 + x2) // 2
                
                # Draw green box around person
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
                
                # Create simple ID
                person_id = f"{center_x//40}_{frame_count//30}"
                
                # Check if crossing the line
                if abs(center_y - line_y) < 20 and person_id not in crossed:
                    total_count += 1
                    crossed.add(person_id)
                    
                    # Flash green when counted
                    cv2.circle(frame, (w//2, line_y), 80, (0, 255, 0), -1)
                    print(f"🎯 EXIT #{total_count}")
    
    # Display count
    cv2.putText(frame, f"EXITS: {total_count}", (20, 70), 
               cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    
    # Instructions
    cv2.putText(frame, "Q=Quit | R=Reset", (10, h-20), 
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    # Show video
    cv2.imshow('Metro Exit Counter - ZJNU Project', frame)
    
    # Handle keys
    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        total_count = 0
        crossed.clear()
        print("🔄 COUNTER RESET")

# Cleanup
cap.release()
cv2.destroyAllWindows()
print(f"\n📊 FINAL COUNT: {total_count} people")

import cv2 
from ultralytics import YOLO 
from tracker import Tracker

cap = cv2.VideoCapture("videos/test_1.mp4")
model = YOLO("models/yolov8n.pt")

tracker = Tracker()
while True:
    ret, frame = cap.read()
    frame = tracker.read_video(frame, model)
   
            
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break 

cap.release()
cv2.destroyAllWindows()

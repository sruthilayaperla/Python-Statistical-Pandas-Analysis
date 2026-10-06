import cv2
from ultralytics import YOLO
model=YOLO("yolo11n.pt")
results=model("d:/YOLO/images/e1.jpg")
for result in results:
    result.show()
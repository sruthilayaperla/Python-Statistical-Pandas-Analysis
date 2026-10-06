import cv2
from ultralytics import YOLO
model=YOLO("yolo11n.pt")
results=model("d:/YOLO/images/car2.jpg",show=True,save=True,conf=0.5,classes=[0,7])
for result in results:
    result.show()
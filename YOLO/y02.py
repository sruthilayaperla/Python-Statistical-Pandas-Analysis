#YOLO +Open Cv image Detection
import cv2
from ultralytics import YOLO
model=YOLO("yolo11n.pt")
image=cv2.imread("d:/YOLO/images/car.jpg")
results=model(image)
annotated_image=results[0].plot()
cv2.imshow("YOLO Detection",annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

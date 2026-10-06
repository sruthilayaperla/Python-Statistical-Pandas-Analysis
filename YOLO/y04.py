import cv2
import easyocr
from ultralytics import YOLO
model = YOLO("yolov8n.pt")  # general model (fallback)
img = cv2.imread("d:/yolo/images/car10.jpg")
results = model(img)
for r in results:
    for box in r.boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)

        crop = img[y1:y2, x1:x2]

        cv2.imshow("Detected Object", crop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
reader = easyocr.Reader(['en'])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = reader.readtext(gray)

for (bbox, txt, prob) in text:
    print("Detected Text:", txt)
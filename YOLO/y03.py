from ultralytics import YOLO
import cv2
model=YOLO("indian_number_plate.pt")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    results=model(frame)
    frame=results[0].plot()
    cv2.imshow("Indian Number plate",frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("Mansy Camera", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open camera")
    exit(1)

cv2.namedWindow("Webcam", cv2.WINDOW_AUTOSIZE)

while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)

    if key in [ord('q'), 27]: # q or ESC
        break
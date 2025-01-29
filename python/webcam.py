
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open camera")
    exit(1)

cv2.namedWindow("Webcam", cv2.WINDOW_AUTOSIZE)

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1, frame) # flip
    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) in [ord('q'), 27]: # q or ESC
        break
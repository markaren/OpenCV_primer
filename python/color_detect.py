
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open camera")
    exit(1)

window_name = "Color Detection"
cv2.namedWindow(window_name)

def nothing(x):
    pass

cv2.createTrackbar("Lower H", window_name, 100, 179, nothing)
cv2.createTrackbar("Lower S", window_name, 150, 255, nothing)
cv2.createTrackbar("Lower V", window_name, 50, 255, nothing)
cv2.createTrackbar("Upper H", window_name, 140, 179, nothing)
cv2.createTrackbar("Upper S", window_name, 255, 255, nothing)
cv2.createTrackbar("Upper V", window_name, 255, 255, nothing)

def get_mask(hsv: cv2.Mat):
    l_h = cv2.getTrackbarPos("Lower H", window_name)
    l_s = cv2.getTrackbarPos("Lower S", window_name)
    l_v = cv2.getTrackbarPos("Lower V", window_name)
    u_h = cv2.getTrackbarPos("Upper H", window_name)
    u_s = cv2.getTrackbarPos("Upper S", window_name)
    u_v = cv2.getTrackbarPos("Upper V", window_name)

    return cv2.inRange(hsv, np.array([l_h, l_s, l_v]), np.array([u_h, u_s, u_v]))

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1, frame) # flip
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = get_mask(hsv)
    y_coords, x_coords = np.where(mask > 0)

    if len(x_coords) > 0 and len(y_coords) > 0:
        # Compute average position
        cx = int(np.mean(x_coords))
        cy = int(np.mean(y_coords))

        # Draw the center point
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)  # Red dot
    else:
        pass

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    concatenated = cv2.hconcat([frame, mask])

    cv2.imshow(window_name, concatenated)

    if cv2.waitKey(1) in [ord('q'), 27]: # q or ESC
        break


import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit(1)

while True:
    ret, image = cap.read()

    image = cv2.flip(image, 1, image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define the dictionary of ArUco markers
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

    # Define the parameters for marker detection
    parameters = cv2.aruco.DetectorParameters()

    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    # Detect the markers
    corners, ids, rejected = detector.detectMarkers(gray)

    # Draw the detected markers on the image
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(image, corners, ids)

    cv2.imshow("Webcam", image)
    key = cv2.waitKey(1)
    if key in [27, ord('q')]:
        break


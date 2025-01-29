import os
import cv2

marker_path = "marker_23.png"
if not os.path.exists(marker_path):
    from generate import generate_marker
    generate_marker(marker_path, 23, 200)


# Load the image containing the ArUco marker
image = cv2.imread(marker_path)

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
else:
    print("No markers detected")

# Display the result
cv2.imshow("Detected ArUco Markers", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

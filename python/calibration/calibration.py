# calibration board: https://markhedleyjones.com/projects/calibration-checkerboard-collection

import cv2 as cv
from pathlib import Path
import numpy as np

#######################################################################################
calibration_path = "C:\\Users\\larsi\\Pictures\\Camera Roll" # replace with YOUR files
#######################################################################################

images = list(Path(calibration_path).glob("*.jpg"))

ps = (8, 6)  # check vertices of your choosen board

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((ps[0] * ps[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.

for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, ps, None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        if False: # set to True if you want to verify detections manually
            # Draw and display the corners
            cv.drawChessboardCorners(img, ps, corners2, ret)

            cv.imshow('img', img)
            cv.waitKey(500)

cv.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    exit(1)

# Define a 3D cube (starting from chessboard plane)
cube_points = np.float32([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Base
    [0, 0, -1], [1, 0, -1], [1, 1, -1], [0, 1, -1]  # Top
]) * 3  # Scale cube to fit

while True:
    ret, img = cap.read()
    if not ret:
        continue

    img = cv.flip(img, 1)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, ps, None)

    if ret and corners is not None:
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        # Solve PnP (estimate pose)
        ret, rvec, tvec = cv.solvePnP(objp, corners2, mtx, dist, flags=cv.SOLVEPNP_ITERATIVE)

        if ret:

            img_points, _ = cv.projectPoints(cube_points, rvec, tvec, mtx, dist)

            img_points = np.int32(img_points).reshape(-1, 2)

            # Draw cube base
            img = cv.polylines(img, [img_points[:4]], True, (0, 255, 0), 2)

            # Draw cube top
            img = cv.polylines(img, [img_points[4:]], True, (0, 255, 0), 2)

            # Connect top and bottom
            for i in range(4):
                img = cv.line(img, tuple(img_points[i]), tuple(img_points[i + 4]), (0, 255, 0), 2)

    # # undistort
    # h, w = img.shape[:2]
    # newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    #
    # dst = cv.undistort(img, mtx, dist, None, newcameramtx)
    #
    # # crop the image
    # x, y, w, h = roi
    # dst = dst[y:y+h, x:x+w]

    cv.imshow("Augmented Reality", img)
    key = cv.waitKey(1)
    if key in [ord('q')]:
        break

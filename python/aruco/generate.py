
import cv2
import numpy as np

def generate_marker(path, marker_id, marker_size):
    # Define the dictionary of ArUco markers
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

    marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, marker_image, 1)

    padding = 20

    # Create a larger canvas with white padding
    padded_size = marker_size + 2 * padding
    padded_image = 255 * np.ones((padded_size, padded_size), dtype=np.uint8)  # White background

    # Place the marker in the center
    start = padding
    padded_image[start:start + marker_size, start:start + marker_size] = marker_image

    # Save the marker image
    cv2.imwrite(path, padded_image)


if __name__ == "__main__":
    aruco_path = "marker_23.png"
    generate_marker(aruco_path, 23, 200)

    marker_image = cv2.imread(aruco_path)

    # Display the marker
    cv2.imshow("ArUco Marker", marker_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

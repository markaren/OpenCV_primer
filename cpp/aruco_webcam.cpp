#include <opencv2/opencv.hpp>
#include <opencv2/aruco.hpp>
#include <iostream>

int main() {
    // Open the default camera
    cv::VideoCapture cap(0);

    if (!cap.isOpened()) {
        std::cerr << "Could not open camera" << std::endl;
        return -1;
    }

    // Define the dictionary of ArUco markers
    cv::aruco::Dictionary arucoDict = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_250);

    // Define the parameters for marker detection
    cv::aruco::DetectorParameters detectorParams;

    // Create an Aruco detector
    cv::aruco::ArucoDetector detector(arucoDict, detectorParams);

    while (true) {
        cv::Mat image;
        cap >> image; // Capture a frame from the camera

        if (image.empty()) {
            std::cerr << "Failed to capture an image" << std::endl;
            break;
        }

        // Convert the image to grayscale
        cv::Mat gray;
        cvtColor(image, gray, cv::COLOR_BGR2GRAY);

        // Detect the markers
        std::vector<int> ids;
        std::vector<std::vector<cv::Point2f>> corners, rejected;
        detector.detectMarkers(gray, corners, ids, rejected);

        // Draw the detected markers on the image
        if (!ids.empty()) {
            cv::aruco::drawDetectedMarkers(image, corners, ids);
        }

        // Display the result
        imshow("Webcam", image);

        // Exit on 'q' or ESC key
        const auto key = cv::waitKey(1);
        if (key == 27 || key == 'q') {
            break;
        }
    }

    return 0;
}

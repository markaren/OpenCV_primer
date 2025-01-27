#include <opencv2/opencv.hpp>

#include <iostream>

int main() {
    cv::VideoCapture cap(0);

    if (!cap.isOpened()) {
        std::cerr << "Error: Unable to open camera" << std::endl;
    }

    namedWindow("Webcam", cv::WINDOW_AUTOSIZE);

    cv::Mat frame;
    while (true) {
        cap.read(frame);
        imshow("Webcam", frame);
        const auto key = cv::waitKey(1);
        if (key == 27 || key == 'q') {
            break;
        }
    }

}

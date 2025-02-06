#include <opencv2/opencv.hpp>

int main() {
    setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT);

    cv::Mat img = cv::imread("data/images/Lenna.png");

    cv::imshow("Webcam", img);
    cv::waitKey();
}

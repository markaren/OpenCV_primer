#include <opencv2/opencv.hpp>
#include <iostream>

cv::Mat image, grayImage, blurredImage, edges;
const char* window_name = "Combined Images: Original | Grayscale | Blurred | Edges";

// Callback function for trackbar (does nothing but required)
void on_trackbar(int, void*) {

    int blurKsize = cv::getTrackbarPos("Blur Kernel", window_name);
    int cannyMin = cv::getTrackbarPos("Canny Min", window_name);
    int cannyMax = cv::getTrackbarPos("Canny Max", window_name);

    // Ensure the blur kernel size is odd and at least 1
    if (blurKsize % 2 == 0) blurKsize += 1;
    blurKsize = std::max(1, blurKsize);

    // Apply Gaussian blur
    cv::GaussianBlur(grayImage, blurredImage, cv::Size(blurKsize, blurKsize), 0);

    // Perform edge detection using Canny
    cv::Canny(blurredImage, edges, cannyMin, cannyMax);

    // Convert grayscale images to 3-channel for display
    cv::Mat grayDisplay, blurredDisplay, edgesDisplay;
    cv::cvtColor(grayImage, grayDisplay, cv::COLOR_GRAY2BGR);
    cv::cvtColor(blurredImage, blurredDisplay, cv::COLOR_GRAY2BGR);
    cv::cvtColor(edges, edgesDisplay, cv::COLOR_GRAY2BGR);

    // Concatenate images horizontally
    cv::Mat combinedImage;
    cv::hconcat(std::vector{image, grayDisplay, blurredDisplay, edgesDisplay}, combinedImage);

    // Display the combined image
    cv::imshow(window_name, combinedImage);
}

int main() {
    std::string imagePath = "data/images/Lenna.png";
    image = cv::imread(imagePath);

    // Check if the image was loaded successfully
    if (image.empty()) {
        std::cout << "Error: Could not load image." << std::endl;
        return -1;
    }

    // Convert the image to grayscale
    cv::cvtColor(image, grayImage, cv::COLOR_BGR2GRAY);

    // Create a window
    cv::namedWindow(window_name, cv::WINDOW_AUTOSIZE);

    // Create trackbars for Gaussian blur and Canny edge detection
    cv::createTrackbar("Blur Kernel", window_name, nullptr, 20, on_trackbar);
    cv::createTrackbar("Canny Min", window_name, nullptr, 255, on_trackbar);
    cv::createTrackbar("Canny Max", window_name, nullptr, 255, on_trackbar);

    cv::setTrackbarPos("Blur Kernel", window_name, 2);
    cv::setTrackbarPos("Canny Min", window_name, 50);
    cv::setTrackbarPos("Canny Max", window_name, 150);

    // Call the callback function once to initialize
    on_trackbar(0, nullptr);

    // Wait for user interaction
    while (true) {

        if (cv::getWindowProperty(window_name, cv::WND_PROP_VISIBLE) < 1) {
            break;
        }

        const auto key = static_cast<char>(cv::waitKey(10));
        if (key == 'q' || key == 27) break; // Exit on 'q' key press
    }

}
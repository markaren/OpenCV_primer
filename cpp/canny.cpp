#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // Load an image from file
    std::string image_path = "data/images/Lenna.png";
    cv::Mat image = cv::imread(image_path);

    // Check if the image was loaded successfully
    if (image.empty()) {
        std::cerr << "Error: Could not load image." << std::endl;
        return -1;
    }

    // Convert the image to grayscale
    cv::Mat gray_image;
    cvtColor(image, gray_image, cv::COLOR_BGR2GRAY);

    // Apply Gaussian blur to the grayscale image
    cv::Mat blurred_image;
    cv::GaussianBlur(gray_image, blurred_image, cv::Size(5, 5), 0);

    // Perform edge detection using the Canny edge detector
    cv::Mat edges;
    cv::Canny(blurred_image, edges, 50, 150);

    // Convert grayscale images to 3 channels for concatenation
    cv::Mat gray_image_3ch, blurred_image_3ch, edges_3ch;
    cvtColor(gray_image, gray_image_3ch, cv::COLOR_GRAY2BGR);
    cvtColor(blurred_image, blurred_image_3ch, cv::COLOR_GRAY2BGR);
    cvtColor(edges, edges_3ch, cv::COLOR_GRAY2BGR);

    // Concatenate images horizontally
    cv::Mat combined_image;
    hconcat(image, gray_image_3ch, combined_image);
    hconcat(combined_image, blurred_image_3ch, combined_image);
    hconcat(combined_image, edges_3ch, combined_image);

    // Display the combined image
    namedWindow("Combined Images: Original | Grayscale | Blurred | Edges", cv::WINDOW_AUTOSIZE);
    imshow("Combined Images: Original | Grayscale | Blurred | Edges", combined_image);
    cv::waitKey();
}

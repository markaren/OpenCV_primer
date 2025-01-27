#include <opencv2/opencv.hpp>

#include <iostream>
#include <filesystem>

int main() {
    // Define the data folders
    std::filesystem::path data_folder = "data";
    std::filesystem::path image_folder = data_folder / "images";
    std::filesystem::path cascades_folder = data_folder / "cascades";

    // Load the cascades
    cv::CascadeClassifier face_cascade;
    cv::CascadeClassifier eye_cascade;
    if (!face_cascade.load((cascades_folder / "haarcascade_frontalface_default.xml").string())) {
        std::cerr << "Error loading face cascade" << std::endl;
        return -1;
    }
    if (!eye_cascade.load((cascades_folder / "haarcascade_eye.xml").string())) {
        std::cerr << "Error loading eye cascade" << std::endl;
        return -1;
    }

    // Read the input image
    cv::Mat img = cv::imread((image_folder / "Lenna.png").string());
    if (img.empty()) {
        std::cerr << "Error loading image" << std::endl;
        return -1;
    }

    // Convert into grayscale
    cv::Mat gray;
    cvtColor(img, gray, cv::COLOR_BGR2GRAY);

    // Detect faces
    std::vector<cv::Rect> faces;
    face_cascade.detectMultiScale(gray, faces, 1.1, 4);

    // Draw rectangle around the faces and detect eyes
    for (const auto &face: faces) {
        rectangle(img, face, cv::Scalar(255, 0, 0), 2);
        cv::Mat roi_gray = gray(face);
        cv::Mat roi_color = img(face);

        std::vector<cv::Rect> eyes;
        eye_cascade.detectMultiScale(roi_gray, eyes);

        for (const auto &eye: eyes) {
            rectangle(roi_color, eye, cv::Scalar(0, 255, 0), 2);
        }
    }

    // Display the output
    imshow("img", img);
    cv::waitKey(0);

    return 0;
}

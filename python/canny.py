
import cv2

image_path = '../data/images/Lenna.png'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Callback function for trackbar (does nothing but required)
def on_trackbar(val):
    pass

# Create a window
window_name = 'Combined Images: Original | Grayscale | Blurred | Edges'
cv2.namedWindow(window_name)

# Create trackbars for Gaussian blur kernel size and Canny edge thresholds
cv2.createTrackbar('Blur Kernel', window_name, 1, 20, on_trackbar)
cv2.createTrackbar('Canny Min', window_name, 50, 255, on_trackbar)
cv2.createTrackbar('Canny Max', window_name, 150, 255, on_trackbar)


while True:

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

    # Get current trackbar positions
    blur_ksize = cv2.getTrackbarPos('Blur Kernel', window_name)
    canny_min = cv2.getTrackbarPos('Canny Min', window_name)
    canny_max = cv2.getTrackbarPos('Canny Max', window_name)

    # Ensure the blur kernel size is odd and at least 1
    if blur_ksize % 2 == 0:
        blur_ksize += 1
    blur_ksize = max(1, blur_ksize)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (blur_ksize, blur_ksize), 0)

    # Perform edge detection using Canny
    edges = cv2.Canny(blurred_image, canny_min, canny_max)

    # Convert grayscale images to 3 channels for display
    gray_display = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    blurred_display = cv2.cvtColor(blurred_image, cv2.COLOR_GRAY2BGR)
    edges_display = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Concatenate images horizontally
    combined_image = cv2.hconcat([image, gray_display, blurred_display, edges_display])

    # Display the combined image
    cv2.imshow(window_name, combined_image)

    # Break loop on 'q' or ESC key press
    if cv2.waitKey(10) in [ord('q'), 27]:
        break

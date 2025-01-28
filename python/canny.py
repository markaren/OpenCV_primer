
import cv2

image_path = '../data/images/Lenna.png'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform edge detection using the Canny edge detector
edges = cv2.Canny(blurred_image, 50, 150)

gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)  # Convert grayscale to 3 channels for concatenation
blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_GRAY2BGR)  # Convert grayscale to 3 channels for concatenation
edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # Convert grayscale to 3 channels for concatenation

# Concatenate images horizontally
combined_image = cv2.hconcat([image, gray_image, blurred_image, edges])

# Display the combined image
cv2.imshow('Combined Images: Original | Grayscale | Blurred | Edges', combined_image)
cv2.waitKey()


import cv2

data_folder = "../data"
image_folder = f"{data_folder}/images"
cascades_folder = f"{data_folder}/cascades"

# Load the cascade
face_cascade = cv2.CascadeClassifier(f'{cascades_folder}/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(f'{cascades_folder}/haarcascade_eye.xml')

# Read the input image
img = cv2.imread(f'{image_folder}/Lenna.png')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()

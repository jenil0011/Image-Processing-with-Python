# Subtract scalar to image and display. Check brightness before and after the operation.

import cv2
import numpy as np

# Read the image
img = cv2.imread('D:\\opencv\\1.jpg', cv2.IMREAD_GRAYSCALE)

# Display the original image
cv2.imshow('Original Image', img)

# Calculate the brightness of the original image
brightness_before = np.mean(img)
print("Brightness before:", brightness_before)

# Subtract 50 from each pixel value
img_subtracted = img - 50

# Calculate the brightness of the resulting image
brightness_after = np.mean(img_subtracted)
print("Brightness after:", brightness_after)

# Display the resulting image
cv2.imshow('Image with Scalar Subtracted', img_subtracted)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
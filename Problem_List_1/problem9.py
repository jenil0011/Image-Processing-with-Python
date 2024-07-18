# Display the contrast of an image.
# Contrast = (Maximum Pixel Value - Minimum Pixel Value) / (Maximum Pixel Value + Minimum Pixel Value)

import cv2
import numpy as np

# Load the image
img = cv2.imread('D:\\opencv\\1.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the minimum and maximum pixel values
min_pixel = np.min(img)
max_pixel = np.max(img)

# Calculate the contrast
contrast = (max_pixel - min_pixel) / (max_pixel + min_pixel)

print("Contrast of the image:",contrast)
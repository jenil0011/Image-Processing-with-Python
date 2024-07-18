# Display average pixel value.

import cv2
import numpy as np

# Load an image
img = cv2.imread('D:\\opencv\\1.jpg',cv2.IMREAD_GRAYSCALE)

# Calculate the average pixel value
avg_pixel_value = np.average(img)

print("Average pixel value: ", avg_pixel_value)
# Display minimum and maximum value of the pixel

import cv2
import numpy as np

# Load a grayscale image
img = cv2.imread('D:\\opencv\\1.jpg', cv2.IMREAD_GRAYSCALE)

# Display the original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Find the minimum and maximum pixel values
min_pixel = np.min(img)
max_pixel = np.max(img)

print("Minimum pixel value: ", min_pixel)
print("Maximum pixel value: ", max_pixel)

# Close all windows
cv2.destroyAllWindows()
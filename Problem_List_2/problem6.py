# Write a program to perform following image operation on
# grayscale image.
# a. Image negative
# b. Log transformation
# c. Power law transformation
# Also display graph of old intensity versus new intensity.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
img = cv2.imread('D:\\opencv\\1.jpg')

# Convert the image to 32-bit float
img_float = img.astype(np.float32)

# Apply transformations
img_neg = cv2.bitwise_not(img)
img_log = cv2.log(img_float + 1)
img_power = cv2.pow(img_float / 255.0, 0.5) * 255

# Convert the transformed images back to 8-bit unsigned integer
img_log = img_log.astype(np.uint8)
img_power = img_power.astype(np.uint8)

# Display the original and transformed images
cv2.imshow('Original Image:', img)
cv2.imshow('Negative Image:', img_neg)
cv2.imshow('Log Image:', img_log)
cv2.imshow('Power Law Image:', img_power)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Plot the graph of old intensity versus new intensity
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.plot(img.flatten(), img_neg.flatten(), 'b.')
plt.xlabel('Old Intensity')
plt.ylabel('New Intensity')
plt.title('Image Negative')

plt.subplot(1, 3, 2)
plt.plot(img.flatten(), img_log.flatten(), 'b.')
plt.xlabel('Old Intensity')
plt.ylabel('New Intensity')
plt.title('Log Transformation')

plt.subplot(1, 3, 3)
plt.plot(img.flatten(), img_power.flatten(), 'b.')
plt.xlabel('Old Intensity')
plt.ylabel('New Intensity')
plt.title('Power Law Transformation')

plt.tight_layout()
plt.show()
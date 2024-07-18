# Display the percentage of pixels above average and below average..

import cv2
import numpy as np

# Load an image
img = cv2.imread('D:\\opencv\\1.jpg',cv2.IMREAD_GRAYSCALE)

# Calculate the average pixel value
avg_pixel_value = np.average(img)

# Calculate the number of pixels above and below average
above_avg = np.sum(img > avg_pixel_value)
below_avg = np.sum(img <= avg_pixel_value)

# Calculate the total number of pixels
total_pixels = img.size

# Calculate the percentage of pixels above and below average
above_avg_percentage = (above_avg / total_pixels) * 100
below_avg_percentage = (below_avg / total_pixels) * 100

print("Average pixel value: ", avg_pixel_value)
print("Percentage of pixels above average: ",above_avg_percentage,"%")
print("Percentage of pixels below average: ",below_avg_percentage,"%")
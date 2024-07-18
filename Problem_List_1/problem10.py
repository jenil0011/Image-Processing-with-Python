# Calculate the size of an image.

import cv2

# Load the image
img = cv2.imread('D:\\opencv\\1.jpg',cv2.IMREAD_GRAYSCALE)

# Get the dimensions of the image
height, width = img.shape

# Calculate the size of the image in bytes
size_in_bytes = img.size

# Calculate the size of the image in kilobytes
size_in_kb = size_in_bytes / 1024

print("Image dimensions: {}x{}".format(width, height))
print("Image size in bytes:",size_in_bytes)
print("Image size in kilobytes:",size_in_kb)
# Apply the addition, subtraction, multiplication and division on both the image.

import cv2

# Read the images
img1 = cv2.imread('D:\\opencv\\2.jpg')
img2 = cv2.imread('D:\\opencv\\3.jpg')

# Display the original images
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)

# Addition
cv2.imshow('Image Addition', cv2.add(img1, img2))

# Subtraction
cv2.imshow('Image Subtraction', cv2.subtract(img1, img2))

# Multiplication
cv2.imshow('Image Multiplication', cv2.multiply(img1, img2))

# Division
cv2.imshow('Image Division', cv2.divide(img1, img2))

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
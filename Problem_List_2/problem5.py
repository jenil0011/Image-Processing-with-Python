# Perform logical operations on image(s)

import cv2
import numpy as np

# Load the image
img = cv2.imread("D:\\opencv\\1.jpg")
img1 = cv2.imread("D:\\opencv\\2.jpg")
img2 = cv2.imread("D:\\opencv\\3.jpg")

# Perform bitwise NOT operation
not_img = cv2.bitwise_not(img)

# Perform bitwise AND operation
and_img = cv2.bitwise_and(img1, img2)

# Perform bitwise OR operation
or_img = cv2.bitwise_or(img1, img2)

# Perform bitwise XOR operation
xor_img = cv2.bitwise_xor(img1, img2)

# Display the inverted image
cv2.imshow('img', img)
cv2.imshow('not_img', not_img)
cv2.imshow('and_img', and_img)
cv2.imshow('xor_img', xor_img)
cv2.imshow('or_img', or_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
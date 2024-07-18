# Apply image blending.
# This code blends two images with equal weights (0.5), resulting in a 50/50 blend of the two images. You can adjust the weights to change the blending ratio.


import cv2

# Read the images
img1 = cv2.imread("D:\\opencv\\2.jpg")
img2 = cv2.imread("D:\\opencv\\3.jpg")

# Blend the images
result = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Display the blended image
cv2.imshow('result', result)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
# program to display a grayscale image

import cv2

# Load the image in grayscale
image = cv2.imread("D:\\opencv\\1.jpg", cv2.IMREAD_GRAYSCALE)

# Display the image
cv2.imshow('Grayscale Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Contrast stretching first find min and max and apply formula directly

# fistly import cv2 and numpy
import cv2
import numpy as np

image = cv2.imread("D:\\opencv\\1.jpg", cv2.IMREAD_GRAYSCALE)

# firstly find min and max
min = np.min(image)
max = np.max(image)

# then apply formula for contrast stretching - unit8
contrast_stretching = ( (image-min) / (max-min) * 255).astype(np.uint8)

cv2.imshow("Normal image",image)
cv2.imshow("contrast stretching image",contrast_stretching)
print("Contrast stretching is :",contrast_stretching)

cv2.waitKey(0)
cv2.destroyAllWindows()
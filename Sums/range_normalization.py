# Range Normalization (same formula as clipping)

import cv2
import numpy as np

image = cv2.imread("D:\\opencv\\1.jpg", cv2.IMREAD_GRAYSCALE)

# first find out min and max and assign it to a and b
a = np.min(image)
b = np.max(image)

# now define range to the variable c and d
c = 166
d = 210

# now,apply formula
range_normalize = ((d-c) / (b-a) * (image-a) + c).astype(np.uint8)

# now clip the values from 0 to 255
range_normalize = np.clip(range_normalize, 0 , 255)

# display image
cv2.imshow("Normalize Image",range_normalize)
cv2.waitKey(0)
cv2.destroyAllWindows()

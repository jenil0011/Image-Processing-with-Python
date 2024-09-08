# Intensity slicing without background

import cv2
import numpy as np

def intensity_slicing(image,t1,t2,L):

    # previously in output_image = image.copy()
    #now
    output_image = np.zeros_like(image)

    # max_intensity
    max_intensity = L-1

    output_image[(image>=t1) & (image<=t2)] = max_intensity

    return output_image

image = cv2.imread("D:\\opencv\\1.jpg", cv2.IMREAD_GRAYSCALE)

# now,define three variables
t1 = 140
t2 = 255
L = 256

output_image = intensity_slicing(image,t1,t2,L)

cv2.imshow("Output Image",output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

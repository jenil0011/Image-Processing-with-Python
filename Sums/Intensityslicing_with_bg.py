# Intensity Slicing with Background

import cv2
import numpy as np

def intensity_slicing(image,t1,t2,L):
    # firstly creat a copy of image
    output_image = image.copy()

    # now, find max_intensity
    max_intensity = L-1

    output_image[(image>=t1) & (image<=t2)] = max_intensity

    cv2.imshow("Output",output_image)
    return output_image

image = cv2.imread("D:\\opencv\\1.jpg", cv2.IMREAD_GRAYSCALE)

# now define three variables
t1 = 140
t2 = 255
L = 256

output_image = intensity_slicing(image,t1,t2,L)

#cv2.imshow("Output Image",output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Image Clipping

import cv2
import numpy as np

def clipping(image,t1,t2):
    # now, first find min and max
    a = np.min(image)
    b = np.max(image)

    # now, assign t1 and t2 to c and d
    c = t1
    d = t2

    # now apply formula
    s = ((d-c)/(b-a)*(image-a)+c).astype(np.uint8)

    # now clip the image
    s_clip = np.clip(s, 0, 255)

    # now, convert output image to unit8
    output_image = s_clip.astype(np.uint8)

    return output_image

image = cv2.imread("D:\\opencv\\1.jpg")

# define two variables
t1 = 0
t2 = 255

output_image = clipping(image,t1,t2)

cv2.imshow("Output image",output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
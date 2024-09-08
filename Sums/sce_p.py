# read an grayscal image and find whether image is bright, dark , has high contrast or low contrast.

# firstly import cv2,numpy,matplotlib.pyplot librarys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# second, step is to read an image as grayscale
image = cv2.imread("D:\\opencv\\1.jpg", cv2.IMREAD_GRAYSCALE)

# now, calculate histogram and fltten the array
hist = cv2.calcHist([image],[0],None,[256],[0,256])
hist = hist.ravel()

# now, normalised the histogram
hist_normalised = hist / hist.sum()

# now, calculate brightness
brightness = np.mean(image)

if brightness>150:
    print("Image is bright")
elif brightness<100:
    print("Image is dark")
else:
    print("Image has normal brightness")

# now, calculate contrast
contrast = np.sqrt(np.mean(image-brightness)**2)

if contrast>70:
    print("Image has high contrast")
elif contrast<40:
    print("Image has low contrast")
else:
    print("Image has normal contrast")

plt.plot(hist)
plt.title("Histogram of Grayscale")
plt.xlabel("Intensity values of pixels")
plt.ylabel("Frequency")
plt.show()
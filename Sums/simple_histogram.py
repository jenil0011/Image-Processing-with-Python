# calculate simple histogram

# firstly import cv2 and matplotlib.pyplot library
import cv2
import matplotlib.pyplot as plt

# read an image
image = cv2.imread("D:\\opencv\\1.jpg", cv2.IMREAD_GRAYSCALE)

# calculate histogram
hist = cv2.calcHist([image],[0],None,[256],[0,256])

# display in graph
plt.plot(hist)
plt.title("Displaying Histogram")
plt.xlabel("Intensity of pixels")
plt.ylabel("frequency")
plt.show()
# histogram equalization

# firstly, we need to import cv2 and matplotlib library
import cv2
import matplotlib.pyplot as plt

# now, read an image as a grayscale
image = cv2.imread("D:\\opencv\\3.jpg", cv2.IMREAD_GRAYSCALE)

# now convert it in equliseimage
# this functions is important cv2.equalizeHist() for performing
equaliseHist_image = cv2.equalizeHist(image)

# now calculate histogram for both images
hist_image = cv2.calcHist([image],[0],None,[256],[0,256])
hist_equalizeHist_image = cv2.calcHist([equaliseHist_image],[0],None,[256],[0,256])

# now,display graphs of both images
# for Normal Image
plt.plot(hist_image)
plt.title("For Normal Image")
plt.xlabel("Intensity of Pixels")
plt.ylabel("Frequency")
plt.show()

# for Equlize Image
plt.plot(hist_equalizeHist_image)
plt.title("For Equalize Image")
plt.xlabel("Intensity of Pixels")
plt.ylabel("Frequency")
plt.show()


# 2 necessary lines
cv2.waitKey(0)
cv2.destroyAllWindows()
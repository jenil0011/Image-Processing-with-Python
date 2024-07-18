import cv2

# Load a grayscale image
img = cv2.imread('D:\\opencv\\1.jpg', cv2.IMREAD_GRAYSCALE)

# Display the original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Manipulate pixel values
# Let's say we want to increase the brightness of the image by 50
img_brightness = cv2.add(img, 50)

# Display the manipulated image
cv2.imshow('Brightness Increased', img_brightness)
cv2.waitKey(0)


# Close all windows
cv2.destroyAllWindows()
# Resize image and display.
import cv2

# Load an image
img = cv2.imread('D:\\opencv\\1.jpg',cv2.IMREAD_GRAYSCALE)

# Display the original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Resize the image
resized_img = cv2.resize(img, (800, 600))  # Resize to 800x600

# Display the resized image
cv2.imshow('Resized', resized_img)

# Save the resized image
cv2.imwrite('genereatedimg.jpg', resized_img)

cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
# Save resized image.
# we can also perform this operation in problem 5

import cv2

# Load an image
img = cv2.imread('D:\\opencv\\1.jpg',cv2.IMREAD_GRAYSCALE)

# Get the original dimensions
height, width = img.shape

# Calculate the new dimensions (e.g., half the size)
new_width = int(width / 2)
new_height = int(height / 2)

# Resize the image
resized_img = cv2.resize(img, (new_width, new_height))

# Save the resized image
cv2.imwrite('resized_image.jpg', resized_img)

print("Resized image saved as 'resized_image.jpg'")
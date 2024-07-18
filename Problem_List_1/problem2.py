# Display image resolutions with appropriate attributes.

import cv2

# Load the image in grayscale
image_path = 'D:\\opencv\\1.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Get image dimensions
height, width = image.shape

# Display the resolution and attributes
print(f'Resolution: {width}x{height}')
print(f'Data Type: {image.dtype}')


# Display the image
cv2.imshow('Grayscale Image', image)

# Wait until a key is pressed, then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

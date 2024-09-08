# averaging filter (same for spatial filtering)
import cv2

# Load the image
image = cv2.imread(r'D:\\opencv\\1.jpg')


# Apply averaging filter with a 5x5 kernel
blurred_image = cv2.blur(image, (9, 9))

    # Display the original and blurred images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image (Averaging Filter)", blurred_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

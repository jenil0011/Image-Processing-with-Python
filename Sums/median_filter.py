# medianBlur
import cv2

# Load the image in grayscale
image = cv2.imread(r'D:\\opencv\\1.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error loading image")
else:
    # Apply median filtering with a kernel size of 5
    filtered_image = cv2.medianBlur(image, 9)

    # Display the original and filtered images
    cv2.imshow("Original Image", image)
    cv2.imshow("Median Filtered Image", filtered_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

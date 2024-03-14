import cv2

# Load the image
image_path = 'img1.jpg'
image = cv2.imread(image_path)

# Display the image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Write the image to a new file
output_path = 'output_image.jpg'
cv2.imwrite(output_path, image)

# Release resources
cv2.destroyAllWindows()

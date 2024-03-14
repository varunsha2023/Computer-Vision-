import cv2
import os

# Load the image
#image_path = 'Img1.jpg'
for i in range (10):
    image_path='Img'+str(i)+'.jpg'
    save_path='Cropped'+str(i)+'.jpg'
    image = cv2.imread(image_path)

    # Load pre-trained face detector from OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale for face detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

    # Create a directory to save cropped faces if it doesn't exist
    output_dir = 'cropped_faces'
    os.makedirs(output_dir, exist_ok=True)

    # Loop through the detected faces
    for i, (x, y, w, h) in enumerate(faces):
        # Draw a rectangle around each face
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Crop the face region from the image
        face_roi = image[y:y + h, x:x + w]

        # Save the cropped face with a unique filename

        cv2.imwrite(save_path, face_roi)

    # Display each cropped face separately
    for i in range(len(faces)):
        # Load the cropped face image
        cropped_face_path = os.path.join(output_dir, f"face_{i}.jpg")
        cropped_face = cv2.imread(cropped_face_path)

        # Display the cropped face
        cv2.imshow('Cropped Face', cropped_face)
        cv2.waitKey(1000)  # Display each face for 1 second

    # Save or display the image with rectangles around faces
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(1)
    cv2.destroyAllWindows()

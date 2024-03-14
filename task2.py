import cv2
import os

# Function to detect faces and save them
def detect_and_save_faces(Img0.jpg):
    # Load the image
class Img0:
    pass


image = cv2.imread(Img0.jpg)

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
        output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(image_path))[0]}_face_{i}.jpg")
        cv2.imwrite(output_path, face_roi)

# Process multiple images
class Img0:
    pass
class Img1:
    pass
class Img2:
    pass
class Img3:
    pass
class Img4:
    pass
class Img5:
    pass
class Img6:
    pass
class Img7:
    pass
class Img8:
    pass
class Img9:
    pass


for i in range(10):  # Img0.jpg to Img9.jpg
    Img0.jpg = f'Img{0}.jpg'
    Img1.jpg= f'Img{1}.jpg'
    Img2.jpg = f'Img{2}.jpg'
    Img3.jpg = f'Img{3}.jpg'
    Img4.jpg= f'Img{4}.jpg'
    Img5.jpg = f'Img{5}.jpg'
    Img6.jpg = f'Img{6}.jpg'
    detect_and_save_faces(image_path)

# Display or save the image with rectangles around faces
# (uncomment the following lines if you want to display)
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print('done')
# Function to perform face detection
#def detect_single_face(image_path):
    # Read the image

# img = cv2.imread('Face.jpg')
#imgre=cv2.resize(img,[500,500])
cap = cv2.VideoCapture(0)
while True:
        success,img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        if len(faces) > 0:
                (x, y, w, h) = faces[0]
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imshow('Detected Face', img)
                cv2.waitKey(10)
        else:
                     print("No face detected in the provided image.")


# Example usage
#image_path = 'Zee3.jpg'
#detect_single_face(image_path)
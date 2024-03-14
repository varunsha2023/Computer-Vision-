import cvzone
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,100)
cap.set(4,150)
while True:
    success,img=cap.read()
    cv2.imshow('test',img)
    if cv2.waitKey(1) & 0xFF==ord("x"):
     break
    cv2.waitKey(1)


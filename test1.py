import cv2
img=cv2.imread('badebhai.jpg')
img2=cv2.resize(img,[300,200])
img3=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
img4=cv2.Canny(img3,100,100)
cv2.imshow('Merabhai',img4)
cv2.waitKey(0)
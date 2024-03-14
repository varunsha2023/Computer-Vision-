import cv2
import numpy as np

img = np.ones((500,500,3),np.uint8)

img[:]=0,0,0
print(img)
for r in range (10,250):
    cv2.circle(img,(0,0),r,(0,0+r,255),5)
    cv2.circle(img,(250,250),r,(0,0+r,255-r),5)
    cv2.circle(img,(0,500),r,(0,0+r,255),5)
    cv2.circle(img,(500,0),r,(0,0+r,255),5)
    cv2.circle(img,(500,500),r,(0,0+r,255),5)
    cv2.imshow("Image",img)
    cv2.waitKey(10)

cv2.waitKey(0)
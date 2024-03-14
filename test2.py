import cv2
import numpy as np

img = np.ones( (512,512,3),np.uint8)
img[:]=12,150,250
cv2.line(img,(200,200),(512,512),(0,0,0),10)
cv2.rectangle(img,(0,0),(200,200),(20,20,20),7)
cv2.circle(img,(200,150),30,20,20)

print(img)




cv2.imshow("Image",img)
cv2.waitKey(0)





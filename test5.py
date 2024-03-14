import cv2
import numpy as np
img = np.ones((500,500,3),np.uint8)
img[:] = 0,150,120
cv2.line(img,(0,0),(250,250),(0,0,0),5)
cv2.imshow('image',img)

cv2.waitKey(0)

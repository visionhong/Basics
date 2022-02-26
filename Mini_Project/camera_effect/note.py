import numpy as np
import cv2

hat = cv2.imread('img/hat.jpg')
hat = hat[100:,:,:]

cv2.imshow('hat', hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
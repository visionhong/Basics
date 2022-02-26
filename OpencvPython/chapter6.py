import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    print(rows)
    cols = len(imgArray[0])
    print(cols)
    rowsAvailable = isinstance(imgArray[0], list)
    print(rowsAvailable)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


img = cv2.imread('Resources/man.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

stack = stackImages(0.5, ([img,imgGray,img],[img,img,img]))

# imghor = np.hstack((img,img))
# print(imghor.shape)
#
# imgver = np.vstack((img,img))
# print(imgver.shape)
#
# cv2.imshow('Horizontal', imghor)
# cv2.imshow('Vertical', imgver)

cv2.imshow('ImageStack', stack)

cv2.waitKey(0)
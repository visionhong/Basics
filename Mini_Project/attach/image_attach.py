import cv2
import numpy as np

x0, y0 = -1, -1
x1, y1 = -1, -1

def capture(event, x, y, flags, param):
    global x0, y0, x1, y1

    if event == cv2.EVENT_LBUTTONDOWN:
        x0, y0 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (x0, y0), (x, y), (0, 120, 0), 1)
        x1 = x
        y1 = y
        print(f"원본이미지 좌표 x0:{x0} y0:{y0} x1:{x1} y1:{y1}")

def attach(event, x, y, flags, param):
    global x0, y0, x1, y1

    if event == cv2.EVENT_LBUTTONDOWN:
        w = x1 - x0
        h = y1 - y0
        empty[y:y+h, x:x+w] = img2[y0:y1, x0:x1]
        print(f"attach 이미지 좌표 x0:{x} y0:{y} x1:{x+w} y1:{y+h}")

img = cv2.imread('cat.jpg')
img2 = img.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image', capture)

h,w,c = img.shape
empty = np.full((h,w,c), (255, 255, 255), dtype=np.uint8)
cv2.namedWindow('empty')
cv2.setMouseCallback('empty', attach)

while True:
    cv2.imshow('image', img)
    cv2.imshow('empty', empty)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # esc를 누르면 종료
        break

cv2.destroyAllWindows()
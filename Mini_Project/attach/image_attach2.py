import cv2
import numpy as np

src = cv2.imread('cat.jpg')  # d.jpg 파일. src는 메모리에 저장된 배열
h, w, c = src.shape
dst = np.full((h, w, c), [255, 255, 255], dtype=np.uint8)

p0 = None
p1 = None
roi = None

cv2.imshow('src', src)
cv2.imshow('dst', dst)


def handdler_src(event, x, y, flags, param):
    global p0, p1
    if event == cv2.EVENT_LBUTTONDOWN:
        p0 = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        p1 = (x, y)
        make_roi()


def make_roi():
    global roi
    roi = src[p0[1]:p1[1], p0[0]:p1[0]]


def handdler_dst(event, x, y, flags, param):
    global roi
    if event == cv2.EVENT_LBUTTONDOWN:
        if roi is not None:
            h = np.abs(p0[1] - p1[1])
            w = np.abs(p0[0] - p1[0])
            dst[y:y + h, x:x + w] = roi
            cv2.imshow('dst', dst)
            roi = None


# 빈 Image 생성
img = np.zeros((512, 512, 3), np.uint8)
cv2.setMouseCallback('src', handdler_src)
cv2.setMouseCallback('dst', handdler_dst)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
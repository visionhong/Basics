'''
과제: 다각형 앨범

각 도형을 추출해서 roi선별해서 리스트에 저장
도형리스트에는 사각형, 삼각형 등의 이미지 저장
for i in list:#도형 이미지 하나씩 추출
   추출한 도형과 매칭이 되는 위치를 찾아서
   거기에 본인 사진 이미지 합성
   결과 이미지 출력
'''

import sys
import numpy as np
import cv2

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 70, 70)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=1)
    return imgDial

def getContour(imgThres):
    contours, _ = cv2.findContours(imgThres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     print(contours)
    for pts in contours:
        area = cv2.contourArea(pts)  #  너무 작으면 무시
        if area > 50:
            approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True) # 근사치 뽑음(꺾이는 부분의 좌표만 뽑음)
            poly_approx.append(len(approx))
            poly_pts.append(len(pts))
            (x, y, w, h) = cv2.boundingRect(pts)

            new_img = image[-40+y:y+h+40, -40+x:x+w+40]

            if y <40: # 직사각형 주위 rectangle이 이미지 밖에 넘어가서
                new_img = image[0:y+h+30, -30+x:x+w+30]

            poly_list.append(new_img)


def homography(src1, src2):
    if src1 is None or src2 is None:
        print('Image load failed!')
        sys.exit()

    # 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
    feature = cv2.KAZE_create()
    # feature = cv2.AKAZE_create()
    # feature = cv2.ORB_create()

    # 특징점 검출 및 기술자 계산
    kp1, desc1 = feature.detectAndCompute(src1, None)
    kp2, desc2 = feature.detectAndCompute(src2, None)

    # 특징점 매칭
    # : L2 노름(L2 norm) 사용
    # cv2.NORM_HAMMING: 해밍 거리 사용
    # cv2.NORM_HAMMING2

    matcher = cv2.BFMatcher_create()
    # matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING)
    matches = matcher.match(desc1, desc2)

    # 좋은 매칭 결과 선별
    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:10]

    #     print('# of kp1:', len(kp1))
    #     print('# of kp2:', len(kp2))
    #     print('# of matches:', len(matches))
    #     print('# of good_matches:', len(good_matches))

    # 호모그래피 계산
    pts1 = np.array([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2).astype(np.float32)
    pts2 = np.array([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2).astype(np.float32)

    # 변환 행렬 생성
    H, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC)
    # 호모그래피를 이용하여 기준 영상 영역 표시
    dst = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None,
                          flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    (h, w) = src1.shape[:2]
    # src1이미지의 4꼭지점 좌표 계산
    corners1 = np.array([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2).astype(np.float32)

    # 위 네 점의 투영 좌표 계산
    corners2 = cv2.perspectiveTransform(corners1, H)

    # 변환 좌표 x축에 800 더해줌. 이미지 2개를 함께 보여주므로 src2 이미지의 x축은 src1의 가로 길이만큼 오른쪽으로 이동
    corners2 = (corners2 + np.float32([w, 0]))
    corners2 = corners2.reshape(-1, 2)
    # print(corners2)
    return corners2, dst

def processing(corners2, dst):
    x = int(corners2[0][0] + 30)
    y = int(corners2[0][1] + 30)
    w = int(corners2[2][0] - corners2[0][0] - 60)
    h = int(corners2[2][1] - corners2[0][1] - 60)

    cv2.rectangle(dst, (x,y,w,h), (0, 0, 255), 2)
    cv2.polylines(dst, [np.int32(corners2)], True, (0, 255, 0), 2, cv2.LINE_AA)

    setting = poly_list[idx].shape[1]
    src = cv2.resize(nature_list[idx], (w,h))

    poly = image[y:y+h, x-setting:x+w-setting]
    gray = cv2.cvtColor(poly, cv2.COLOR_BGR2GRAY)
    if num == 5:
        _, mask = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)
    else:
        _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    mask_inv = cv2.bitwise_not(mask) # 반전

    edge = cv2.bitwise_and(poly, poly, mask=mask)
    main = cv2.bitwise_and(src,src, mask = mask_inv)
    dst2 = cv2.add(edge,main)
    image[y:y+h, x-setting:x+w-setting] = dst2

    cv2.imshow('src', src)
    cv2.imshow('gray', gray)
    cv2.imshow('mask', mask)
    cv2.imshow('mask_inv', mask_inv)
    cv2.imshow('edge', edge)
    cv2.imshow('main', main)
    cv2.imshow('dst2', dst2)

    cv2.imshow('image', image)

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    image = cv2.imread('img/polygon.bmp')

    poly_list = []
    poly_approx = []
    poly_pts = []
    imgThres = preProcessing(image)
    getContour(imgThres)

    nature_list = []
    for i in range(len(poly_list)):
        nature_list.append(cv2.imread(f'img/nature{i+1}.jpg'))


    num = int(input('도형 번호 선택 1.정사각형 2.직사각형 3.ㄱ모양 4.이등변삼각형 5.직각삼각형 6.별 7.원 8.타원   '))
    if num == 1:
        res_list = list(filter(lambda x: poly_approx[x] == 4, range(len(poly_approx))))
        idx = poly_pts.index(min([poly_pts[res_list[0]],poly_pts[res_list[1]]]))
    elif num == 2:
        res_list = list(filter(lambda x: poly_approx[x] == 4, range(len(poly_approx))))
        idx = poly_pts.index(max([poly_pts[res_list[0]],poly_pts[res_list[1]]]))
    elif num == 3:
        idx = poly_approx.index(6)
    elif num == 4:
        res_list = list(filter(lambda x: poly_approx[x] == 3, range(len(poly_approx))))
        idx = poly_pts.index(max([poly_pts[res_list[0]],poly_pts[res_list[1]]]))
    elif num == 5:
        res_list = list(filter(lambda x: poly_approx[x] == 3, range(len(poly_approx))))
        idx = poly_pts.index(min([poly_pts[res_list[0]],poly_pts[res_list[1]]]))
    elif num == 6:
        idx = poly_approx.index(10)
    elif num == 7:
        res_list = list(filter(lambda x: poly_approx[x] == 8, range(len(poly_approx))))
        idx = poly_pts.index(min([poly_pts[res_list[0]],poly_pts[res_list[1]]]))
    elif num == 8:
        res_list = list(filter(lambda x: poly_approx[x] == 8, range(len(poly_approx))))
        idx = poly_pts.index(max([poly_pts[res_list[0]],poly_pts[res_list[1]]]))

    src1 = poly_list[idx]
    src2 = image
    corners2,dst = homography(src1,src2)
    processing(corners2,dst)

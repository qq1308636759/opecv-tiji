import math
import cv2
import matplotlib.pyplot as plt
import numpy as np
def v(path):

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#图像灰度化
    ret, binary = cv2.threshold(gray, 0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    binary = cv2.bitwise_not(binary)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 矩形结构
    close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=30)


    binary,contours, hierarchy = cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    a = 0
    for i in range(len(contours)):
        area =cv2.contourArea(contours[i])
        if(area>10000):
            a = i
    rbox = cv2.minAreaRect(contours[a])
    pingjunzhijing = (rbox[1][1]+rbox[1][0])/2

    a = 0.017316017316017316
    r = pingjunzhijing/2
    r = r*a
    v = 4*math.pi*r*r*r/3
    plt.subplot(111)
    plt.imshow(binary,cmap='gray')
    plt.show()



    cv2.drawContours(img,contours,-1,(0,0,255),5)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.subplot(111)
    plt.imshow(img)
    plt.show()
    return v

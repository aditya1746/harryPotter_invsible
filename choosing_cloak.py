import cv2 
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('track')

cv2.createTrackbar('low_hue','track',0,180,nothing)
cv2.createTrackbar('up_hue','track',0,180,nothing)
cv2.createTrackbar('low_sat','track',0,255,nothing)
cv2.createTrackbar('up_sat','track',0,255,nothing)
cv2.createTrackbar('low_val','track',0,255,nothing)
cv2.createTrackbar('up_val','track',0,255,nothing)
cv2.createTrackbar('ksize','track',0,20,nothing)
cv2.createTrackbar('itr','track',0,10,nothing)

while(cap.isOpened()):

    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('low_hue','track')
    uh = cv2.getTrackbarPos('up_hue','track')
    ls = cv2.getTrackbarPos('low_sat','track')
    us = cv2.getTrackbarPos('up_sat','track')
    lv = cv2.getTrackbarPos('low_val','track')
    uv = cv2.getTrackbarPos('up_val','track')
    k = cv2.getTrackbarPos('ksize','track')
    i = cv2.getTrackbarPos('itr','track')

    low = np.array([lh,ls,lv],np.uint8)
    up = np.array([uh,us,uv],np.uint8)

    mask1 = cv2.inRange(hsv,low,up)
    mask1 = cv2.dilate(mask1,(k,k),iterations=i)
    cv2.imshow('mask1',mask1)

    mask2 = cv2.bitwise_not(mask1)
    cv2.imshow('mask2',mask2)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()

cv2.destroyAllWindows()
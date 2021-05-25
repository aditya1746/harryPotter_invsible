import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    cv2.imshow('frame',frame)

    if(cv2.waitKey(10) & 0xFF == ord('s')):

        cv2.imwrite('background.jpg',frame)
        break

    elif (cv2.waitKey(10) & 0xFF == 27):
    
        break

cap.release()

cv2.imshow('saved image',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
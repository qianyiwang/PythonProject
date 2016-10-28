import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # retval, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    # gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_color = np.array([110,100,100])
    high_color = np.array([130,255,255])
    mask = cv2.inRange(hsv, low_color, high_color)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    gaus = cv2.GaussianBlur(res, (15,15), 0)

    position =  np.where( gaus[:,:,0] > 100 )
    if len(position[0])>0 and len(position[1]) > 0:
        col1 = min(position[0])
        col2 = max(position[0])
        row1 = min(position[1])
        row2 = max(position[1])
        cv2.rectangle(frame,(row1,col1),(row2,col2),(0,255,255),5)

    gray = np.float32(gray)
    corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
    corners = np.int0(corners)

    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(frame, (x,y),3, 255, -1)

    cv2.imshow('res', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

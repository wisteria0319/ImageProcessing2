import numpy as np
import cv2

def myfunc(i):
    global output
    
    output = cv2.bilateralFilter(frame,15,i,i)


cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   0, # min
                   70, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue

    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win

    ## do something by using v
    myfunc(v)

    cv2.imshow('title', output)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
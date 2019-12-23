import cv2
import datetime

cap=cv2.VideoCapture(0)
while (cap.isOpened()):
    ret, frame=cap.read()
    if ret==True:
        datet=str(datetime.datetime.now())
        frame=cv2.rectangle(frame,(10,25),(510,60),(255,0,0),3)
        frame=cv2.putText(frame,datet,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break   
    else:
        break
    
    
cap.release()
cv2.destroyAllWindows()
    
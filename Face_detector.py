import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")
img=cv2.imread('istockphoto-623600600-612x612.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
net=cv2.dnn.readNet('yolov3.weights',"yolov3.cfg")

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("GRAY",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
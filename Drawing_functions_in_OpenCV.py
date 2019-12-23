import cv2
import numpy as np

#img=cv2.imread('lena.jpg',1)
img=np.zeros([512,512,3],np.uint8)

img=cv2.line(img,(0,0),(255,255),(0,96,0),3)
img=cv2.arrowedLine(img,(0,255),(255,255),(147,96,),3)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,155),1)
img=cv2.circle(img,(447,63),(63),(0,125,10),-1)
img=cv2.putText(img,"OpenCV",(10,500),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=4,color=(255,0,255),thickness=4,lineType=cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
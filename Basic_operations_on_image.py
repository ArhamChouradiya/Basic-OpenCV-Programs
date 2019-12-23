import cv2
import numpy as np

img=cv2.imread('messi5.jpg')
img2=cv2.imread('opencv-logo.png')

print(img.shape)
print(img.size)
print(type(img))            #still some doubt about it
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
#img2=cv2.merge((g,r,b))    #interchanged bgr values will affect image

ball = img[280:340,330:390]
img[273:333,100:160]= ball
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

#dst=cv2.add(img2,img)  #just add images
dst2=cv2.addWeighted(img,.5,img2,.5,0)

#cv2.imshow('images',dst)
cv2.imshow('image',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
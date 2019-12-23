import cv2
import numpy as np

img=cv2.imread('lena.jpg',1)
layer=img.copy()
gp=[layer]
#Gaussian Pyramid
for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer=gp[5]
cv2.imshow('Upper level Gaussian pyramid',layer)

lp=[layer]
#Laplacian Pyramid
for i in range(5,0,-1):
    gaussian_extended=cv2.pyrUp(gp[i])
    lp=cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),lp)

#lr=cv2.pyrDown(img)        
#lr1=cv2.pyrDown(lr)
#up=cv2.pyrUp(img)
#up=cv2.pyrUp(lr1)

#cv2.imshow('Image',img)
#cv2.imshow('PyrDown',lr)
#cv2.imshow('PyrDown2',lr1)
#cv2.imshow('PyrUp',up)
#cv2.imshow('PyrUp',up)
cv2.waitKey(0)
cv2.destroyAllWindows()
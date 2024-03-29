import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img=cv.imread('gradient.png',0)
_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
_,th2=cv.threshold(img,50,255,cv.THRESH_BINARY_INV)
_,th3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
#_,th8=cv.threshold(img,127,255,cv.THRESH_MASK)
#_,th4=cv.threshold(img,127,255,cv.THRESH_OTSU)
_,th4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
_,th5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
#_,th7=cv.threshold(img,127,255,cv.THRESH_TRIANGLE)

titles=['Original','Binary','BinaryInv','Trunc','Tozero','TozeroInv']
images=[img,th1,th2,th3,th4,th5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
#cv.imshow('Image',img)
#cv.imshow('th1',th1)
#cv.imshow('th2',th2)
#cv.imshow('th3',th3)
#cv.imshow('th4',th4)
#cv.imshow('th5',th5)
#cv.imshow('th6',th6)
#cv.imshow('th7',th7)
#cv.imshow('th8',th8)
 
plt.show()
#cv.waitKey(0)
#cv.destroyAllWindows()
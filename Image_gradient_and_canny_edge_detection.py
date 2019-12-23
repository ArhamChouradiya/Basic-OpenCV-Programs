import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
#img=cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)
canny=cv2.Canny(img,100,200)

sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))

sobelcmb=cv2.bitwise_or(sobelx,sobely)


titles=['images','Laplacian','sobelx','sobely','sobelcmb','Canny']
images=[img,lap,sobelx,sobely,sobelcmb,canny]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
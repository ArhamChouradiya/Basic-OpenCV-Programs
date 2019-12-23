import cv2
import numpy as np
from matplotlib import pyplot as plt

#img=cv2.imread('Noise_salt_and_pepper.png',1)
img=cv2.imread('lena.jpg',1)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,3)        #must be odd and not 1
bilateral=cv2.bilateralFilter(img,9,75,75)
#<bilateral>highly effective in noise removal while keeping edges preserved in much better way

titles=['image','2D Convolution','Blur','Gaussian Blur','Median Filter','Bilateral Filter']
images=[img,dst,blur,gblur,median,bilateral]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
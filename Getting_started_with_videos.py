#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 12:18:30 2019

@author: arham
"""

import cv2

cap=cv2.VideoCapture('vtest.avi')
#fourcc=cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('output.avi',fourcc,20,(640,480))

while (True):
    ret, frame=cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #out.write(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame',frame)
        cv2.imshow('Gray',gray)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break   
    else:
        break
    
    
cap.release()
#out.release()
cv2.destroyAllWindows()
    
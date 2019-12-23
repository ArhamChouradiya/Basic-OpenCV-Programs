#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 12:18:30 2019

@author: arham
"""

import cv2

cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,640)
cap.set(4,480)
print(cap.get(3))
print(cap.get(4))
while (cap.isOpened()):
    ret, frame=cap.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break   
    else:
        break
    
    
cap.release()
cv2.destroyAllWindows()
    
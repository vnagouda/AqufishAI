# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:01:44 2024

@author: vnago
"""

import cv2
import numpy as np

kernel = np.ones((3,3), np.uint8)
cap = cv2.VideoCapture("D:\Viresh\Assignment_Tutorials\Assignment_Tutorials\FishVideo2.mp4")


while True:
    ret, frame = cap.read()    
    blurred = cv2.GaussianBlur(frame, (7,7), cv2.BORDER_DEFAULT)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    
    ret, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY_INV)
    
    dilated = cv2.dilate(thresh, (5,5), iterations =9)
    #print(os.listdir(directory))
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print(len(contours))
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        #print(area)
        if area>50 and area<200:
            
            cv2.drawContours(frame, cnt, -1 , (255,0,0), 3)  
            rect = cv2.minAreaRect(cnt)
            (x,y), (w,h), angle = rect
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            #print(box)
            #cv2.circle(frame, (int(x),int(y)), 5, (0,0,0), -1)
            cv2.polylines(frame, [box],True, (255,0,0),1)
            #cv2.polylines(thresh, [box],True, (255,0,0),1)
            #cv2.putText(frame, "Perfect IC", (int(x-100),int((y-30))), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0),2)
    
    print("/////////////////")
    cv2.imshow("frame", frame)
    
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
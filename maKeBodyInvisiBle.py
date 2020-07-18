import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'XVID') # Video Codec
out = cv2.VideoWriter('InvisibleAnshuK.avi',codec,20.0,(640,480)) 
time.sleep(2)
background = 0#capturing background (Whole idea is replacing background with red color)
for i in range(30):
    ret, background = cap.read()#capturing image
while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,70])# divide the whole range of 0 to 360 of hue into two parts of 180 as the maximum range is 0 to 255 
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv , lower_red , upper_red)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv , lower_red , upper_red)
    mask1 = mask1 + mask2 #OR
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=2)        
    mask2=cv2.morphologyEx(mask1, cv2.MORPH_DILATE ,np.ones((3,3) , np.uint8) , iterations=1)    
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1 , 1, res2 , 1, 0)
    cv2.imshow('AnshuTheBoss' , final_output)
    out.write(final_output)
    if cv2.waitKey(1)==13:
    	break
cap.release()
cv2.destroyAllWindows()        
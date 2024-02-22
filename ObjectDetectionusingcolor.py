#Object detection using color using HSV (HUE SATURATION VALUE)

# with the help of hsv we easily can detect objects by their colors.

import cv2
import numpy as np

img=cv2.imread("Colorball.jpeg")

while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
    u_v=np.array([28,252,252])
    l_v=np.array([22,171,171])
    #creating mask
    mask=cv2.inRange(hsv,l_v,u_v)
    
    #filter mask with image
    res=cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow("Image",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    if cv2.waitKey(0) & 0xFF==ord('s'):
        break   
    
cv2.destroyAllWindows() 
   


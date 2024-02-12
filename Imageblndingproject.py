import cv2
import numpy as np

img1=cv2.imread("messi.webp")
img1=cv2.resize(img1,(500,500))

img2=cv2.imread("ronaldo.webp")
img2=cv2.resize(img2,(500,500))

def blend(x):
    pass

img=np.zeros((400,400,3),np.uint8)
cv2.namedWindow(winname="window")
cv2.createTrackbar("alpha","window",1,100,blend)

#create switch
switch='0:off\n1:on'
cv2.createTrackbar(switch,"window",0,1,blend)

while True:
    s=cv2.getTrackbarPos(switch,"window")
    a=cv2.getTrackbarPos("alpha","window")
    n=float(a/100) # the value of alpha which is 1 to 100 is continuously putting here so that we can find the value of n then with the help of n we  can find img1 alpha and img2 beta 
    print(n)
    
    if s==0:
        dst=img[:]
    else:
        dst=cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst,str(a),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)   
    cv2.imshow("dst",dst)
    k=cv2.waitKey(1)&0xff
    if k==ord('q'):
        break


# cv2.imshow("ronaldo",img2)
# cv2.imshow("messi",img1)
# cv2.waitKey(0)
cv2.destroyAllWindows()
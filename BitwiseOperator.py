import cv2
import numpy as np

img1=np.zeros((250,500,3),np.uint8)
img1=cv2.rectangle(img1,(50,60),(450,190),(255,255,255),-1)

img2=np.zeros((250,500,3),np.uint8)
img2=cv2.rectangle(img2,(150,200),(40,70),(255,255,255),-1)


#bitwise AND
res_and = cv2.bitwise_and(img1, img2)
cv2.imshow("Bitwise And", res_and)

#bitwise OR
res_or=cv2.bitwise_or(img1,img2)
cv2.imshow("Bitwise OR", res_or)

#bitwise  XOR  0 0---> 0 | 0 1 --->1 | 1 0 ----> 1 | 1 1 ----> 0
res_xor=cv2.bitwise_xor(img1,img2)
cv2.imshow("Bitwise XOR", res_xor)

#bitwise NOT
res_not=cv2.bitwise_not(img1)
cv2.imshow("Bitwise Not", res_not)


cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.waitKey(0)
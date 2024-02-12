import cv2
import numpy as np

 #we can using cv2.add and cv2.addWeight to binding or merging the images 
 #cv2.add is used when we want to add two image with same size, it will give sum of RGB values for each pixel in corresponding positions.
#cv2.add is used for adding two image with same size, but it will not work if the both image have different sizes
#cv2.add: It is used to add two images together, pixel wise sum of two images

# if and only if the  both image have the same size otherwise it will give error

img=cv2.imread("messi.webp")
img=cv2.resize(img,(500,700))

img1=cv2.imread("ronaldo.webp")
img1=cv2.resize(img1,(500,700))

##blending
result=cv2.add(img1,img)
# cv2.imshow("result=",result)

##weighted blending
alpha=0.3 # this is weight
beta=(1-alpha)
gama=cv2.addWeighted(img,alpha,img1,beta,0)

cv2.imshow("Gama",gama)

# cv2.imshow("ronaldo",img1)
# cv2.imshow("messi",img)
cv2.waitKey(0)
cv2.destroyAllWindows
import cv2
import numpy as  np

img=cv2.imread("messi.webp")
img=cv2.resize(img,(300,300))
print("shape==",img.shape)
print("no. of pixels",img.size)
print("datatype",img.dtype)
print("image_types",type(img))

[b,g,r]=cv2.split(img)

#displaying the color channels separately
# cv2.imshow("Red",r)
# cv2.imshow("green",g)
# cv2.imshow("blue",b)
# cv2.imshow("original",img)

#merge image

# mr1 = cv2.merge((g,b,r))
# mr2 = cv2.merge((r,g,b))
# cv2.imshow("merge1",mr1)
# cv2.imshow("merge2",mr2)
# cv2.imshow("original",img)


px=img[50,58] #accessing pixel value by giving row and column index
print("Pixel Value is: ", px)

blue=img[50,58,0] #blue means 0
print("Pixel Value is: ", blue)

red=img[50,58,2] #red means 2
print("Pixel Value is: ", red)

green=img[50,58,1] #green means 1
print("Pixel Value is: ", green)

cv2.imshow("original",img)


cv2.waitKey(0)
cv2.destroyAllWindows
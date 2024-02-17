#Thresolding
#use to extract selected data from the images by using pixels 
#Also use to manage pixels and divide all values in two parts
# we select a pixel 
import cv2
import numpy as np

img=cv2.imread('messi.webp',0) # '0' use to convert into gray

#simple thresolding (img,pixel_thresold,max_thresh_pixel,style)
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print("Original Image")
cv2.imshow("Original", img)
print("\nThresholded Image")
cv2.imshow("Thresholded", thresh)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#Otsu's Thresholding
_, otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Otsu's Thresholded Image")
cv2.imshow("Otsu_Thresholded", otsu)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#Adaptive Thresholding
#Gaussian Blur is used for smoothing the image while reducing noise
blur = cv2.GaussianBlur(img,(5,5),0)
adaptive_thr = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
print("Adaptive Thresholded Image")
cv2.imshow("Adaptive_Thresholded", adaptive_thr)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()


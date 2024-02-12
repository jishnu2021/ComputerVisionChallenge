import cv2
import numpy as np

img=cv2.imread("messi.webp")
img=cv2.resize(img,(500,500))

brdr=cv2.copyMakeBorder(img,10,10,5,5,cv2.BORDER_CONSTANT,value=[255,0,125])

cv2.imshow("messi",brdr)
cv2.waitKey(0)
cv2.destroyAllWindows
import cv2
import numpy as np

img=cv2.imread("messi.webp")
img=cv2.resize(img,(650,650))

#How to find ROI - Region Of Interest
# Im using paint and select the region then collect the pixels of 2 corners
#[(y1:y2) ,(x1:x2)]
# diff of y1 and y2 = 254
# diff of x1 and x2 = 200
roi=img[140:394,203:403]

# now passing data into image x axis
img[140:394,424:624]=roi
img[140:394,3:203]=roi
#y axis
img[395:649,3:203]=roi

cv2.imshow("Messi",img)


# cv2.imshow("Messi",img)




cv2.waitKey(0)
cv2.destroyAllWindows()
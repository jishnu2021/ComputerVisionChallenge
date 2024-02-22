import cv2
import numpy as np

img1=cv2.imread("hero1.jpg")
img2=cv2.imread("strom_breaker.jpg")

img1=cv2.resize(img1,(1024,650)) #Resizing the
img2=cv2.resize(img2,(600,650))
#i want to fix img2 data into img1
r,c,ch=img2.shape
print(r,c,ch)

#roi
roi=img1[0:r,0:c] #in img1 we select the portion where we put the img2 

img_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) # its mandatory to convert image in gray for thresholding

#create mask using threshold
mask=cv2.threshold(img_gray,45,255,cv2.THRESH_BINARY)[1]

#remove background
mask_inv=cv2.bitwise_not(mask)


#now black out the area which is not part of hand i.e., backround
img2_with_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)


#bitwise operation
img2_fg=cv2.bitwise_and(img2,img2,mask=mask) # img 2 and mask both are of same size so no need to resize
                                             #it will give us the partaily transparent area of img2

# Put img in ROI and modify the main image
res=cv2.add(img2_with_bg,img2_fg)

final=img1
final[0:r,0:c]=res
# cv2.imshow("Thor",img1)
# cv2.imshow("Strom Breaker",img2)
# cv2.imshow("roi==",roi)
# cv2.imshow("gray",img_gray)
# cv2.imshow("mask",mask)
# cv2.imshow("mask inverse",mask_inv)
cv2.imshow("Img2_figure",img2_fg)
cv2.imshow("Image with bg",img2_with_bg)
cv2.imshow("result",res)
# cv2.imshow("Final result",final)
cv2.waitKey(0)
cv2.destroyAllWindows()
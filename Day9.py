import cv2
import  numpy as np

# img=cv2.imread("messi.webp")
# img=cv2.resize(img,(600,600))

# img=np.zeros([512,512,3],np.uint8)*255  #for black color
img=np.ones([512,512,3],np.uint8)*255  #for black color

#here line accept 5 parameter (img,starting,ending,color code ,thickness)
img=cv2.line(img,(0,0),(300,300),(252,40,3),5)

#here line accept 5 parameter (img,starting,ending,color code ,thickness)
img=cv2.arrowedLine(img,(0,120),(250,350),(3, 40, 252),10)

#Here rectangle accept 5 parameter (img,starting,ending,color code ,thickness, -1(negative value) is defined full color)
img=cv2.rectangle(img,(384,10),(510,128),(3, 40, 252),-1)

#Here circle accept 5 parameter (img,starting,radius,color code ,thickness, -1(negative value) is defined full color)
img=cv2.circle(img,(500,450),60,(3, 40, 252),-5)

#Here text accept 8 parameter (img,starting,start,font,fontsize,color code ,thickness,linetype)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,"Messi",(50,450),font,5,(33,32,33),10,cv2.LINE_AA)


cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows
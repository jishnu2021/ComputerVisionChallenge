# # Binding Mouse Events with OpenCV Functions

# import cv2
# import numpy as np

# def draw(event,x,y,flags,param):
#     print("x==",x)
#     print("y==",y)
#     print("flag==",flags)
#     print("param==",param)
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 100, (255, 0, 255),5)
#     if event == cv2.EVENT_RBUTTONDBLCLK:
#         cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
        
# cv2.namedWindow(winname="res")

# img=np.zeros((512,512,3),np.uint8)
# cv2.setMouseCallback("res",draw)


# while True:
#     cv2.imshow("res",img)
#     if cv2.waitKey(1) & 0xFF == 27: # 27 means escape button
#         break
    
# cv2.destroyAllWindows()

 
 

# Create a function which help t find cordinate of any pixel and its color

import cv2

def draw(event,x,y,flags,param):
    print("x==",x)
    print("y==",y)
    print("flag==",flags)
    print("param==",param)
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        
        cord=". "+str(x)+', '+str(y)
        cv2.putText(img,cord,(x,y),font,1,(155,125,100),2)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]  # for blue channel is 0
        g=img[y,x,1]  # for green channel is 1
        r=img[y,x,2]  # for red channel is 2
        
        
        color_bgr= "Blue :"+ str(b) +" Green :"+str(g) +" Red :"+str(r)
        cv2.putText(img,color_bgr,(x,y),font,2,(152,255,130),2)
        
cv2.namedWindow(winname="res")

img=cv2.imread("messi.webp")
cv2.setMouseCallback("res",draw)


while True:
    cv2.imshow("res",img)
    if cv2.waitKey(1) & 0xFF == 27: # 27 means escape button
        break
    
cv2.destroyAllWindows()

        
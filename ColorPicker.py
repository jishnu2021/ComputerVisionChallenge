import cv2
import numpy  as np

def cross(x):
    pass

#blank
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Color Picker")

#create switch

switch="0:OFF\n1:ON"
cv2.createTrackbar(switch,"Color Picker",0,1,cross)

#Creating for rgb
#Creating trackbars for adjusting colors
cv2.createTrackbar("R","Color Picker",0,255,cross)
cv2.createTrackbar("G","Color Picker",0,255,cross)
cv2.createTrackbar("B","Color Picker",0,255,cross)


while True:
    cv2.imshow("Color Picker",img)
    if cv2.waitKey(1) & 0xFF == 's':
        break
    # get the current positions of four trackbars
    r_val = cv2.getTrackbarPos("R","Color Picker")
    g_val = cv2.getTrackbarPos("G","Color Picker")
    b_val = cv2.getTrackbarPos("B","Color Picker")
    
    s_val = cv2.getTrackbarPos(switch,"Color Picker")
    
    # take a look at the image and see what color is being displayed
    
    print ("Red: ",r_val," Green: ",g_val," Blue: ",b_val)
    # turn on or off based on switch value
    if s_val==1:
        img[:]=[b_val,g_val,r_val]  
    else:
        img[:]=0
        
cv2.destroyAllWindows()
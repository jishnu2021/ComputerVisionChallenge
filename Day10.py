import cv2
import datetime

cap=cv2.VideoCapture(0)
print("Height==",cap.get(4)) # here 4 is height
print("Width==",cap.get(3)) # here 3 is width

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX_SMALL
        frame=cv2.resize(frame,(1200,800)) #resizing the image to 135
        text='Height: '+str(cap.get(4))+', Width: '+str(cap.get(3))
        date_data="Date: "+str(datetime.datetime.now())
        cv2.putText(frame,text,(100,200),font,3,(33,32,33),5,cv2.LINE_AA)
        cv2.putText(frame,date_data,(200,300),font,3,(33,32,33),5,cv2.LINE_AA)
        
        # Display the resulting frame
        
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()        
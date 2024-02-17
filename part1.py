import cv2

# Video access

# vid=cv2.VideoCapture("Stay.mp4")

# while(True):
#     ret,frame=vid.read()
#     frame=cv2.resize(frame,(700,450))
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('frame',frame)
#     cv2.imshow("gray",gray)
    
#     k=cv2.waitKey(25)
#     if k==ord('s') & 0xFF:
#         break
    
# vid.release()
# cv2.destroyAllWindows()    


# web cam access

vid=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('new.mp4',fourcc,20.0,(640,480),0)
while vid.isOpened():
    ret,frame=vid.read()
    if ret == True:
        
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        cv2.imshow("gray",gray)
        output.write(frame)
        k=cv2.waitKey(25)
        if k==ord('s') & 0xFF:
            break
    
vid.release()
output.release()
cv2.destroyAllWindows() 





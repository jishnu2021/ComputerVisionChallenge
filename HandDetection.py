import cv2
import  numpy as np

img=cv2.imread("hand.jpg")
img=cv2.resize(img,(500,500))
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=cv2.medianBlur(img1,11)
ret,thresh = cv2.threshold(img1,240,255,cv2.THRESH_BINARY)
dilate=cv2.dilate(thresh,(1,1),iterations=6)
#findcontour(img,contour_retrival_mode,method)
cnt,hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Number of colors ==",cnt,"\nTotal Contour==",len(cnt))
print("Hierarchy==\n",hier)


for c in cnt:
    epsilon = 0.0001 * cv2.arcLength(c, True)
    data = cv2.approxPolyDP(c, epsilon, True)

    hull = cv2.convexHull(data)

    cv2.drawContours(img, [c], -1, (50, 50, 150), 2)
    cv2.drawContours(img, [hull], -1, (0, 255, 0), 2)

    hull2 = cv2.convexHull(c, returnPoints=False)
    defect = cv2.convexityDefects(c, hull2)

    if defect is not None:
        for i in range(defect.shape[0]):
            s, e, f, d = defect[i, 0]
            start = tuple(c[s][0])
            end = tuple(c[e][0])
            far = tuple(c[f][0])
            cv2.circle(img, far, 5, [0, 0, 255], -1)



c_max = max(cnt, key=cv2.contourArea)

# determine the most extreme points along the contour
extLeft = tuple(c_max[c_max[:, :, 0].argmin()][0])
extRight = tuple(c_max[c_max[:, :, 0].argmax()][0])
extTop = tuple(c_max[c_max[:, :, 1].argmin()][0])
extBot = tuple(c_max[c_max[:, :, 1].argmax()][0])

# draw the outline of the object, then draw each of the
# extreme points, where the left-most is red, right-most
# is green, top-most is blue, and bottom-most is teal

cv2.circle(img, extLeft, 8, (255, 0, 255), -1)  #pink
cv2.circle(img, extRight, 8, (0, 125, 255), -1) #brown
cv2.circle(img, extTop, 8, (255, 10, 0), -1)  #blue
cv2.circle(img, extBot, 8, (19, 152, 152), -1) #green










cv2.imshow("Thresh", thresh)
cv2.imshow("Origial==",img)
cv2.imshow("Gray==",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


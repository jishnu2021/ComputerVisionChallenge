import cv2
import numpy as np

img1=cv2.imread("messi.webp")
img1=cv2.resize(img1,(500,500))
roi=img1[129:219,193:319]

img2=cv2.imread("ronaldo.webp")
img2=cv2.resize(img2,(500,500))
img2[129:219,193:319]=roi


cv2.imshow("Modified image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows
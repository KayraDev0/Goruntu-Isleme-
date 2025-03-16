# Goruntuleri karistirma
import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("manzara.JPG")
cv2.imshow("img1",img1)
cv2.waitKey(0)
img2 = cv2.imread("bird.JPG")
cv2.imshow("img2",img2)
cv2.waitKey(0)

print(img1.shape)
print(img2.shape)
img1 = cv2.resize(img1,(800,600))
img2 = cv2.resize(img2,(800,600))
    
img3 = cv2.addWeighted(src1=img1,src2=img2,alpha=0.4,beta=0.6,gamma=0)
cv2.imshow("img3",img3)
cv2.waitKey(0)

cv2.destroyAllWindows()
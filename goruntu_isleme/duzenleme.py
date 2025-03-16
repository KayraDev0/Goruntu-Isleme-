import numpy as np
import cv2
import matplotlib.pyplot as plt

img1=cv2.imread("manzara.jpg")
img2=cv2.imread("bird.jpg")

img1=cv2.resize(img1,(300,300))
img2=cv2.resize(img2,(300,300))

cv2.imshow("img1",img1)
cv2.waitKey(0)
cv2.imshow("img2",img2)
cv2.waitKey(0)

yanyana=np.hstack((img1,img2))
cv2.imshow("yanyana",yanyana)
cv2.waitKey(0)

ustuste=np.vstack((img1,img2))
cv2.imshow("ustuste",ustuste)
cv2.waitKey(0)

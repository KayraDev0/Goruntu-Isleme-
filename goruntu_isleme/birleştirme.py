import numpy as np
import matplotlib.pyplot as plt
import cv2

img1=cv2.imread("lena.jpg")
img2=cv2.imread("bird.jpg")

cv2.imshow("img1",img1)
cv2.waitKey(0)
img2=cv2.resize(img2,(225,225))
cv2.imshow("img2",img2)
cv2.waitKey(0)

yanyana=np.hstack((img1,img2))
cv2.imshow("yanyana",yanyana)
cv2.waitKey(0)

ustuste=np.vstack((img1,img2))
cv2.imshow("ustuste",ustuste)
cv2.waitKey(0)

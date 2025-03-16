# Perspektif du�zeltme         #YAPILMADI
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("lena2.jpg")
print(type(img))
print(img.shape)
cv2.imshow("img",img)
cv2.waitKey(0)

width = 225
height = 225

pts1 = np.float32([[95,7],[10,127],[125,212],[212,95]])
pts2 = np.float32([[0,0],[0,height],[width,height],[width,0]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_perspective = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Kart Perspective",img_perspective)
cv2.waitKey(0)

cv2.destroyAllWindows()
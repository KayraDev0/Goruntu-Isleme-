# Histogram Esitleme
import numpy as np
import cv2
import matplotlib.pyplot as plt


img=cv2.imread("lena.JPG",0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img,cmap="gray")
plt.title("Original")
plt.show()

eq_hist = cv2.equalizeHist(img)
plt.figure()
plt.imshow(eq_hist,cmap="gray")
plt.title("Contrast")
plt.show()
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("lena.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.title("İlk")
plt.show()

hist_img=cv2.equalizeHist(img)
plt.figure()
plt.imshow(hist_img,cmap="gray")
plt.title("İkinci")
plt.show()

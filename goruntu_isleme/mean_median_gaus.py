import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("lena.jpg",0)

plt.figure()
plt.imshow(img,cmap="gray")
plt.axis()
plt.title("orjinal")
plt.show()

mean_img=cv2.blur(img,ksize=(3,3))
plt.figure()
plt.imshow(mean_img,cmap="gray")
plt.axis()
plt.title("mean")
plt.show()

median_img=cv2.medianBlur(img,ksize=3)
plt.figure()
plt.imshow(median_img,cmap="gray")
plt.axis()
plt.title("median")
plt.show()

gaus_img=cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(gaus_img,cmap="gray")
plt.axis()
plt.title("gaussian")
plt.show()




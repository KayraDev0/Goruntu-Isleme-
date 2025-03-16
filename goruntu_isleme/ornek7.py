# Bulanıklaştırma
import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("lena.JPG")

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("original")
plt.show()


mean_blur =cv2.blur(img,ksize=(3,3))
plt.figure(),plt.imshow(mean_blur),plt.axis("off"),plt.title("mean_bluring"),plt.show()

gb =cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("gaussian_bluring"),plt.show()

median_blur =cv2.medianBlur(img,ksize=3)
plt.figure(),plt.imshow(median_blur),plt.axis("off"),plt.title("median_bluring"),plt.show()


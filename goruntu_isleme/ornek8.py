# Gradyanlar
import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("lena.JPG",0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("orjinal resim"),plt.show()

sobelx = cv2.Sobel(img,ddepth=cv2.CV_16S,dx=1,dy=0,ksize=3)
plt.figure(),plt.imshow(sobelx,cmap="gray"),plt.axis("off"),plt.title("SobelX"),plt.show()

sobely = cv2.Sobel(img,ddepth=cv2.CV_16S,dx=0,dy=1,ksize=3)
plt.figure(),plt.imshow(sobely,cmap="gray"),plt.axis("off"),plt.title("SobelY"),plt.show()

laplacian = cv2.Laplacian(img,ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplacian,cmap="gray"),plt.axis("off"),plt.title("Laplacian"),plt.show()

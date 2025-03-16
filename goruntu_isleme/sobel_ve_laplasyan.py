import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("lena.jpg",0)

plt.figure()
plt.imshow(img,cmap="gray")
plt.axis()
plt.title("orjinal")
plt.show()

sobelx_img=cv2.Sobel(img,ddepth=cv2.CV_16S,dx=1,dy=0,ksize=3)
plt.figure()
plt.imshow(sobelx_img,cmap="gray")
plt.axis()
plt.title("x yönünde sobel")
plt.show()

sobely_img=cv2.Sobel(img,ddepth=cv2.CV_16S,dx=0,dy=1,ksize=3)
plt.figure()
plt.imshow(sobely_img,cmap="gray")
plt.axis()
plt.title("y yönünde sobel")
plt.show()

laplacian_img=cv2.Laplacian(img,ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(laplacian_img,cmap="gray")
plt.axis()
plt.title("laplasyan")
plt.show()


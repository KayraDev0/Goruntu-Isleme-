import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plot
import cv2

img1=cv2.imread("lena.jpg")
img2=cv2.imread("bird.jpg")

img1=cv2.resize(img1,(400,400))
img2=cv2.resize(img2,(400,400))

cv2.imshow("resim1",img1)
cv2.waitKey(0)
cv2.imshow("resim2",img2)
cv2.waitKey(0)

img3=np.hstack((img1,img2))
cv2.imshow("resim3",img3)
cv2.waitKey(0)

img1=cv2.imread("lena.jpg",0)

sobelx_img1=cv2.Sobel(img1,ddepth=cv2.CV_16S,dx=1,dy=0,ksize=3)
plt.figure()
plt.imshow(sobelx_img1,cmap="gray")
plt.axis()
plt.title("x yönünde sobel")
plt.show()

sobely_img1=cv2.Sobel(img1,ddepth=cv2.CV_16S,dx=0,dy=1,ksize=3)
plt.figure()
plt.imshow(sobely_img1,cmap="gray")
plt.axis()
plt.title("y yönünde sobel")
plt.show()





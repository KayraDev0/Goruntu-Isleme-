# Görüntü Eşikleme              #YAPILMADI
import numpy as np
import cv2
import matplotlib.pyplot as plt

# %matplotlib qt

img = cv2.imread("manzara.JPG",0)

plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.title("Original Image")
plt.show()

_,thresh_img = cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img,cmap="gray")
plt.axis("off")
plt.title("thresh_img")
plt.show()

_,thresh_img_inverse = cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(thresh_img_inverse,cmap="gray")
plt.axis("off")
plt.title("thresh_img_inverse")
plt.show()

thresh_img2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh_img2,cmap="gray")
plt.axis("off")
plt.title("adaptiveThreshold")
plt.show()

#cv2.waitKey(0)

cv2.destroyAllWindows()
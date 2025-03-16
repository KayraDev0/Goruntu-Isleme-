#Görüntülerin Birleştirilmesi
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("lena.jpg")
print(type(img))
print(img.shape)
cv2.imshow("img",img)
cv2.waitKey(0)

hor = np.hstack((img,img))
cv2.imshow("Horizontal img",hor)
cv2.waitKey(0)

ver = np.vstack((img,img))
cv2.imshow("Vertical img",ver)
cv2.waitKey(0)

cv2.destroyAllWindows()
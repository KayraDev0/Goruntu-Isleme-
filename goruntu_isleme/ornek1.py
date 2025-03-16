#Yeniden Boyutlandırma Ve Kırpma
import numpy as np
import cv2
import matplotlib.pyplot as plt


#orijinalResim = cv2.imread('DATA/2_rgb.png',0)

#img=cv2.imread("C:\\python_goruntuisleme\\ayasofya.jpg")
#img=cv2.cvtColor(resim1a,cv2.COLOR_BGR2RGB)

img=cv2.imread("ayasofya.jpg")
print(type(img))
print(img.shape)

cv2.imshow("ayasofya",img)
cv2.waitKey(0)
img_resized = cv2.resize(img,(400,400))
cv2.imshow("img resized",img_resized)
cv2.waitKey(0)
img_cropped = img[100:300,100:600]
cv2.imshow("img Cropped",img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Sekil ve Metin Ekleme
import numpy as np
import cv2
import matplotlib.pyplot as plt


#orijinalResim = cv2.imread('DATA/2_rgb.png',0)

#img=cv2.imread("C:\\python_goruntuisleme\\ayasofya.jpg")
#img=cv2.cvtColor(resim1a,cv2.COLOR_BGR2RGB)
img=cv2.imread("ayasofya.jpg")
print(type(img))
print(img.shape)
cv2.imshow("Ayasofya",img)
cv2.waitKey(0)


cv2.line(img, (0,0), (512,512), (0,0,255), 3)
cv2.imshow("Line",img)
cv2.waitKey(0)
cv2.rectangle(img,(300,300), (512,512), (255,0,0),cv2.FILLED)
cv2.imshow("Rectangle",img)
cv2.waitKey(0)
cv2.circle(img,(100,100),45,(0,255,0),10)
cv2.imshow("Circle",img)
cv2.waitKey(0)
cv2.putText(img,"Goruntu isleme",(300,50),cv2.FONT_HERSHEY_SIMPLEX,0.8,(100,100,100))
cv2.imshow("Metin",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
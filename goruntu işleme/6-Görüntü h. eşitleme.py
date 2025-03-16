import cv2
import numpy as np
import matplotlib.pyplot as plt

I1 = cv2.imread("indir.jpeg")

R = I1[:, :, 2]
G = I1[:, :, 1]
B = I1[:, :, 0]

I_gray = 0.299 * R + 0.587 * G + 0.114 * B

I_gray_flattened = I_gray.flatten().astype(int)

hist = [0] * 256

for pixel_value in I_gray_flattened:
    hist[pixel_value] += 1

cdf = [0] * 256

cdf[0] = hist[0]
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + hist[i]

cdf_min = min([value for value in cdf if value > 0])
cdf_max = max(cdf)
cdf_normalized = [(value - cdf_min) * 255 // (cdf_max - cdf_min) for value in cdf]
cdf_normalized = np.array(cdf_normalized).astype(np.uint8)

I2 = cdf_normalized[I_gray.astype(np.uint8)]

plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(I_gray, cmap='gray')
plt.title('Gri Tonlamaya Dönüştürülmüş Orijinal Görüntü')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(I_gray_flattened, bins=256, color='gray', alpha=0.7)
plt.title('Gri Tonlamaya Dönüştürülmüş Orijinal Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')

plt.subplot(2, 2, 3)
plt.imshow(I2, cmap='gray')
plt.title('Histogram Eşitlenmiş Görüntü')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(I2.flatten(), bins=256, color='gray', alpha=0.7)
plt.title('Yeni Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Frekans')

plt.tight_layout()
plt.show()

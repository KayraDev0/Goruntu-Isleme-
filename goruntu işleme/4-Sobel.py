import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_sobel_filter(image):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    padded_image = np.pad(image, 1, mode='constant')

    sobel_x_img = np.zeros_like(image)
    sobel_y_img = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i+3, j:j+3]
            sobel_x_img[i, j] = np.sum(region * sobel_x)
            sobel_y_img[i, j] = np.sum(region * sobel_y)

    return np.sqrt(sobel_x_img**2 + sobel_y_img**2)

image_path = "indir.jpeg"

if os.path.exists(image_path):
    image = np.array(Image.open(image_path).convert("L"))
    filtered_image = apply_sobel_filter(image)

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Orijinal Görüntü")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap="gray")
    plt.title("Sobel Filtresi")
    plt.axis("off")
    plt.show()
else:
    print("Dosya bulunamadı.")

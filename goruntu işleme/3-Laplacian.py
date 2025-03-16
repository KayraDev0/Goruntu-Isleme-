import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_laplacian_filter(image):
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    pad = kernel.shape[0] // 2
    padded_image = np.pad(image, pad_width=pad, mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i + 3, j:j + 3]
            filtered_image[i, j] = np.sum(region * kernel)

    return filtered_image

image_path = "indir.jpeg"
if os.path.exists(image_path):
    image = np.array(Image.open(image_path).convert("L"))
    filtered_image = apply_laplacian_filter(image)

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Orijinal Görüntü")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap="gray")
    plt.title("Laplacian Filtresi")
    plt.axis("off")

    plt.show()
else:
    print(f"Dosya bulunamadı: {image_path}")
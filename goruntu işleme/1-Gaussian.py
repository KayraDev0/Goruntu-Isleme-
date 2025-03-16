import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_gaussian_filter(image, kernel):
    padded_image = np.pad(image, pad_width=kernel.shape[0] // 2, mode='constant', constant_values=0)
    return np.array([[np.clip(np.sum(padded_image[i:i+kernel.shape[0], j:j+kernel.shape[1]] * kernel), 0, 255)
                      for j in range(image.shape[1])] for i in range(image.shape[0])])

def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma**2)) * np.exp(-((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * sigma ** 2)),
        (size, size)
    )
    return kernel / np.sum(kernel)

image_path = "indir.jpeg"
kernel_size = 5
sigma = 1.0

if os.path.exists(image_path):
    image = Image.open(image_path).convert("L")
    image_array = np.array(image)
    gaussian_kernel_matrix = gaussian_kernel(kernel_size, sigma)
    blurred_image = apply_gaussian_filter(image_array, gaussian_kernel_matrix)

    plt.subplot(1, 2, 1)
    plt.title("Orijinal Görüntü")
    plt.imshow(image_array, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Gaussian Filtresi")
    plt.imshow(blurred_image, cmap="gray")
    plt.axis("off")

    plt.show()
else:
    print("Dosya bulunamadı.")

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def apply_prewitt_filter(image):
    prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    padded_image = np.pad(image, 1, mode='constant')

    prewitt_x_img = np.zeros_like(image)
    prewitt_y_img = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded_image[i:i + 3, j:j + 3]
            prewitt_x_img[i, j] = np.sum(region * prewitt_x)
            prewitt_y_img[i, j] = np.sum(region * prewitt_y)

    edge_magnitude = np.sqrt(prewitt_x_img ** 2 + prewitt_y_img ** 2)

    return edge_magnitude



image_path = "indir.jpeg"

if os.path.exists(image_path):
    image = np.array(Image.open(image_path).convert("L"))
    filtered_image = apply_prewitt_filter(image)

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Orijinal Görüntü")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap="gray")
    plt.title("Prewitt Filtresi")
    plt.axis("off")
    plt.show()
else:
    print("Dosya bulunamadı.")
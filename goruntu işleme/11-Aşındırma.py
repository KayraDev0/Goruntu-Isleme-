import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_erosion(image, kernel_size=3):
    padded_image = np.pad(image, pad_width=kernel_size // 2, mode='constant', constant_values=255)
    return np.min(np.lib.stride_tricks.sliding_window_view(padded_image, (kernel_size, kernel_size)), axis=(2, 3))

#
image_path = "indir.jpeg"

if os.path.exists(image_path):
    image = np.array(Image.open(image_path).convert("L"))
    eroded_image = apply_erosion(image)

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Orijinal Görüntü")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(eroded_image, cmap="gray")
    plt.title("Aşındırma")
    plt.axis("off")

    plt.show()
else:
    print("Dosya bulunamadı.")

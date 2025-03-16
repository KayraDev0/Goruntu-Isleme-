import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_opening(image, kernel_size=3):

    padded_image = np.pad(image, kernel_size // 2, mode='constant', constant_values=255)
    eroded = np.min(np.lib.stride_tricks.sliding_window_view(padded_image, (kernel_size, kernel_size)), axis=(2, 3))
    dilated = np.max(np.lib.stride_tricks.sliding_window_view(np.pad(eroded, kernel_size // 2, mode='constant', constant_values=0),
                                                              (kernel_size, kernel_size)), axis=(2, 3))
    return dilated

image_path = "indir.jpeg"
kernel_size = 5

if os.path.exists(image_path):
    image = np.array(Image.open(image_path).convert("L"))
    opened_image = apply_opening(image, kernel_size)

    plt.subplot(1, 2, 1), plt.imshow(image, cmap="gray"), plt.title("Orijinal Görüntü"), plt.axis("off")
    plt.subplot(1, 2, 2), plt.imshow(opened_image, cmap="gray"), plt.title("Opening"), plt.axis("off")
    plt.show()
else:
    print("Dosya bulunamadı.")

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_closing(image, kernel_size=3):
    pad = kernel_size // 2
    dilated = np.max(np.lib.stride_tricks.sliding_window_view(np.pad(image, pad, mode='constant', constant_values=0), (kernel_size, kernel_size)), axis=(2, 3))
    return np.min(np.lib.stride_tricks.sliding_window_view(np.pad(dilated, pad, mode='constant', constant_values=255), (kernel_size, kernel_size)), axis=(2, 3))

image_path = "indir.jpeg"
kernel_size = 5

if os.path.exists(image_path):
    image = np.array(Image.open(image_path).convert("L"))
    closed_image = apply_closing(image, kernel_size)

    plt.subplot(1, 2, 1), plt.imshow(image, cmap="gray"), plt.title("Orijinal"), plt.axis("off")
    plt.subplot(1, 2, 2), plt.imshow(closed_image, cmap="gray"), plt.title("Closing"), plt.axis("off")
    plt.show()
else:
    print("Dosya bulunamadı.")


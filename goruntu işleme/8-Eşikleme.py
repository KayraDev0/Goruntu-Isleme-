import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as \
    plt

def apply_thresholding(image, threshold=128):
    return np.where(image > threshold, 255, 0).astype(np.uint8)

image_path = "indir.jpeg"

if os.path.exists(image_path):
    image = np.array(Image.open(image_path).convert("L"))
    thresholded_image = apply_thresholding(image)

    plt.subplot(1, 2, 1), plt.imshow(image, cmap="gray"), plt.title("Orijinal Görüntü"), plt.axis("off")
    plt.subplot(1, 2, 2), plt.imshow(thresholded_image, cmap="gray"), plt.title(f"Eşikleme (Threshold: 128)"), plt.axis("off")
    plt.show()
else:
    print("Dosya bulunamadı.")

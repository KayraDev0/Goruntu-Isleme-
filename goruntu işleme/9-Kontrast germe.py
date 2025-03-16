import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_contrast_stretching(image):
    return ((image - image.min()) / (image.max() - image.min()) * 255).astype(np.uint8)

image_path = "indir.jpeg"

if os.path.exists(image_path):
    image = np.array(Image.open(image_path).convert("L"))
    contrast_stretched_image = apply_contrast_stretching(image)

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Orijinal Görüntü")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(contrast_stretched_image, cmap="gray")
    plt.title("Kontrast Germe")
    plt.axis("off")

    plt.show()
else:
    print("Dosya bulunamadı.")

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def plot_histogram(image_path):
    if os.path.exists(image_path):
        image = np.array(Image.open(image_path).convert("L"))
        hist, bins = np.histogram(image.flatten(), bins=256, range=(0, 255))
        plt.bar(bins[:-1], hist, width=1, color='black', alpha=0.7)
        plt.title("Görüntü Histogramı"), plt.xlabel("Piksel Değeri"), plt.ylabel("Frekans"), plt.xlim(0, 255), plt.grid(True)
        plt.show()
    else:
        print("Dosya bulunamadı.")

plot_histogram("indir.jpeg")

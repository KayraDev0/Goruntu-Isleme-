import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def kontrast_germe(image):
    min_vol = np.min(image)
    max_vol = np.max(image)
    stretched_image = (image - min_vol) / (max_vol - min_vol) * 255
    stretched_image = np.clip(stretched_image, 0, 255).astype(np.uint8)  # Doğru veri tipi
    return stretched_image


image_path = "indir.jpeg"


image = Image.open(image_path).convert("L")
image_array = np.array(image)


stretched_image = kontrast_germe(image_array)


plt.imshow(stretched_image, cmap="gray")
plt.title("Kontrast Germe Görüntü")
plt.axis("off")
plt.show()
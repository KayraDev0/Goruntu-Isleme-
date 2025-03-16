import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def histogram_esitleme(image):

    hist,_= np.histogram(image.flatten(), bins=256, range=(0, 256))
    cdf = hist.cumsum()
    cdf = ((cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())).astype(np.uint8)  #
    return cdf[image]

image_path = "indir.jpeg"


image = Image.open(image_path).convert("L")
image_array = np.array(image)


stretched_image = histogram_esitleme(image_array)


plt.imshow(stretched_image, cmap="gray")
plt.title("Histogram Eşitlenmiş Görüntü")
plt.axis("off")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.transform import ProjectiveTransform
from skimage.transform import warp


image_path = 'matkap.jpg'
image = Image.open(image_path)
image_array = np.array(image)


src_points = np.array([[100, 100],  # Sol üst
                       [500, 100],  # Sağ üst
                       [500, 500],  # Sağ alt
                       [100, 500]]) # Sol alt


dst_points = np.array([[0, 0],    # Sol üst
                       [400, 0],   # Sağ üst
                       [400, 400], # Sağ alt
                       [0, 400]])  # Sol alt


transform = ProjectiveTransform()
transform.estimate(src_points, dst_points)


transformed_image = warp(image_array, transform)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image_array)
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(transformed_image)
plt.title('Perspektif Düzeltme')
plt.axis('off')

plt.show()
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('ex.png').convert('L'))

rows, cols = img.shape
for i in range(rows):
    for j in range(cols):
        if img[i, j] <= 128:
            img[i, j] = 0
        else:
            img[i, j] = 1

plt.figure("lena")
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

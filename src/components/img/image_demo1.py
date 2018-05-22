import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.array(Image.open('ex.png'))  # 打开图像并转化为数字矩阵
plt.figure("dog")
plt.imshow(img)
plt.axis('off')
plt.show()

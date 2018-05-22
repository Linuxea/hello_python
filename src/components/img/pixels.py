import numpy as np
from PIL import Image


def random_img(output, width, height):
    array = np.random.random_integers(0, 255, (width, height, 3))

    array = np.array(array, dtype=np.uint8)
    img = Image.fromarray(array)
    img.save(output)


random_img('random.png', 50, 50)

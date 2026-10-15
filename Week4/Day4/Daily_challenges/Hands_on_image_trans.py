import os
import numpy as np
from PIL import Image, ImageOps
from scipy.ndimage import rotate
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'flowers', 'flowers', '19_010.png')

img = Image.open(image_path)

rotated = Image.fromarray(np.uint8(rotate(np.array(img), 30, reshape=False, mode='nearest')))
h_flipped = ImageOps.mirror(img)
v_flipped = ImageOps.flip(img)

w, h = img.size
nw, nh = int(w * 1.2), int(h * 1.2)
zoomed = img.resize((nw, nh), Image.Resampling.LANCZOS).crop(((nw - w) / 2, (nh - h) / 2, (nw + w) / 2, (nh + h) / 2))

for i, im in enumerate([img, rotated, h_flipped, v_flipped, zoomed]):
    plt.subplot(1, 5, i + 1)
    plt.imshow(im)
    plt.axis('off')
plt.show()
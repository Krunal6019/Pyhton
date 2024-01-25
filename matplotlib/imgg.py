import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fname=r'horse.jpeg'

#opening image using pil

image=Image.open(fname).convert('L')

#mapping image to gray scale
plt.imshow(image,cmap='PuRd') #gray
plt.show()
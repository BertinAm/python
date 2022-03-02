from PIL import Image #helps to read images
import numpy as np #calling numpy
image = Image.open("pic2.png") #opening the image you want to use
image_array = np.array(image)
print(image)
#print(image_array[0][0])

import random
import sys

import numpy as np
from PIL import Image
from rsa import encrypt

testimage = Image.open("chest_mri_stego.png")
testimage_array = np.asarray(testimage)

diagnostic = open("diagnostic_decrypted.txt", "w")

key = np.load('key.npy')
diagnostic_text = ''

for [i, j] in key:
    diagnostic_text += chr(testimage_array[i, j][0])
    testimage_array[i, j] = np.array([0, testimage_array[i, j][1], testimage_array[i, j][2]])

diagnostic.write(diagnostic_text)
output = Image.fromarray(testimage_array)
output.show()
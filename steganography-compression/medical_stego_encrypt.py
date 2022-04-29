import random
import sys

import numpy as np
from PIL import Image
from rsa import encrypt

testimage = Image.open("chest_mri.jpeg")
testimage_array = np.asarray(testimage)

diagnostic = open("diagnostic.txt", "r")
diagnostic_text = diagnostic.read()
diagnostic_text = list(diagnostic_text)[-1::-1]

key = list()
flag = False
for i in range(testimage_array.shape[1]):
    for j in range(testimage_array.shape[0]):
        if testimage_array[i, j][0] < 1:
            key.append([i,j])
            x = ord(diagnostic_text.pop())
            print(chr(x), end='')
            testimage_array[i, j][0] = x
        if len(diagnostic_text) < 1:
            break
    if len(diagnostic_text) < 1:
        break
np.save('key.npy', key)
            

output = Image.fromarray(testimage_array)
output.show()
output.save("chest_mri_stego.png")
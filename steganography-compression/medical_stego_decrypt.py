import random
import sys

import numpy as np
from PIL import Image
from rsa import encrypt

def medical_stego_decrypt(input_image_file):
    testimage = Image.open(input_image_file)
    testimage_array = np.asarray(testimage)

    diagnostic = open("diagnostic_decrypted.txt", "w")

    key = list(np.load('key.npy', allow_pickle=True))
    mode_pixel = key.pop()
    print(key)
    diagnostic_text = ''

    for x in range(3):
        for [i, j] in key[x]:
            diagnostic_text += chr(testimage_array[i, j][x])
            # if x == 0:
            #     testimage_array[i, j] = np.array([mode_pixel, testimage_array[i, j][1], testimage_array[i, j][2]])
            # elif x == 1:
            #     testimage_array[i, j] = np.array([testimage_array[i, j][0], mode_pixel, testimage_array[i, j][2]])
            # elif x == 2:
            #     testimage_array[i, j] = np.array([testimage_array[i, j][0], testimage_array[i, j][1], mode_pixel])
            testimage_array[i, j][x] = mode_pixel

    diagnostic.write(diagnostic_text)
    print("The diagnostic report was recovered into ", diagnostic.name)
    output = Image.fromarray(testimage_array)
    output.show()
    output_image_file = input_image_file.split('_stego.')[0] + "_decrypted.jpeg"
    output.save(output_image_file)

if __name__ == "__main__":
    input_image_file = "chest_mri_stego.png"
    medical_stego_decrypt(input_image_file)
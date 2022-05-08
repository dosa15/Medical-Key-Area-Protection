import random
from string import hexdigits
import sys
from turtle import width

import numpy as np
from PIL import Image
from rsa import encrypt

def medical_stego_decrypt(input_image_file):
    testimage = Image.open(input_image_file)
    testimage_array = np.asarray(testimage)
    width = height = 0

    diagnostic = open("diagnostic_decrypted.txt", "w")

    key = list(np.load('key.npy', allow_pickle=True))
    mode_pixel = key.pop()
    # print(key)
    diagnostic_text = ''

    frame_size = 31
    for x in range(0,width,frame_size):
        for y in range(0,height,frame_size):
            for i in range(0,frame_size-1):
                for j in range(0,frame_size-1):
                    if (width-x <= frame_size) or (height-y <= frame_size):
                        break
                    p1 = testimage_array[x+i, y+j]
                    p2 = testimage_array[abs(i-frame_size)+x, abs(j-frame_size)+y]

                    testimage_array[abs(i-frame_size)+x, abs(j-frame_size)+y] = p1
                    testimage_array[x+i, y+j] = p2

    for x in range(3):
        for [i, j] in key[x]:
            diagnostic_text += chr(testimage_array[i, j][x])
            testimage_array[i, j][x] = mode_pixel

    diagnostic.write(diagnostic_text)
    print("The diagnostic report was recovered into ", diagnostic.name)
    output = Image.fromarray(testimage_array)
    output.show()
    output_image_file = input_image_file.split('_stego.')[0] + "_decrypted.jpeg"
    output.save(output_image_file)

if __name__ == "__main__":
    input_image_file = "chest_mri_processed.png"
    medical_stego_decrypt(input_image_file)
import random
import sys

import numpy as np
from PIL import Image
from rsa import encrypt

def medical_stego_encrypt(input_image_file):
    testimage = Image.open(input_image_file)
    testimage_array = np.asarray(testimage)

    arr = testimage_array.flatten(order='C')
    # with np.printoptions(threshold=np.inf):
    #     print(np.sort(arr))
    mode_pixel = np.bincount(testimage_array.flatten(order='C')).argmax()
    print("Most common pixel value = ", mode_pixel, " occurring ", np.bincount(testimage_array.flatten(order='C'))[mode_pixel], " times")

    diagnostic = open("diagnostic.txt", "r")
    diagnostic_text = diagnostic.read()
    diagnostic_text = list(diagnostic_text)[-1::-1]

    key0 = list()
    for i in range(testimage_array.shape[1]):
        for j in range(testimage_array.shape[0]):
            if testimage_array[i, j][0] == mode_pixel:
                key0.append([i,j])
                x = ord(diagnostic_text.pop())
                # print(chr(x), end='')
                testimage_array[i, j][0] = x
            if len(diagnostic_text) < 1:
                break
        if len(diagnostic_text) < 1:
            break
    
    key1 = list()
    if len(diagnostic_text) > 0:
        for i in range(testimage_array.shape[1]):
            for j in range(testimage_array.shape[0]):
                if testimage_array[i, j][1] == mode_pixel:
                    key.append([i,j])
                    x = ord(diagnostic_text.pop())
                    # print(chr(x), end='')
                    testimage_array[i, j][1] = x
                if len(diagnostic_text) < 1:
                    break
            if len(diagnostic_text) < 1:
                break
    
    key2 = list()
    if len(diagnostic_text) > 0:
        for i in range(testimage_array.shape[1]):
            for j in range(testimage_array.shape[0]):
                if testimage_array[i, j][2] == mode_pixel:
                    key.append([i,j])
                    x = ord(diagnostic_text.pop())
                    # print(chr(x), end='')
                    testimage_array[i, j][2] = x
                if len(diagnostic_text) < 1:
                    break
            if len(diagnostic_text) < 1:
                break

    key = np.array([key0, key1, key2, mode_pixel], dtype=object)
    np.save('key.npy', key)

    output = Image.fromarray(testimage_array)
    output.show()
    output_image_file = input_image_file.split('.')[0] + "_stego.png"
    output.save(output_image_file)

if __name__ == '__main__':
    input_image_file = "chest_mri.jpeg"
    medical_stego_encrypt(input_image_file)

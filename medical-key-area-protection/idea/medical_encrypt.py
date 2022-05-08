import random
import sys

import numpy as np
from PIL import Image
from rsa import encrypt

def medical_stego_encrypt(input_image_file):
    testimage = Image.open(input_image_file)
    testimage_array = np.asarray(testimage)
    width, height=testimage.size

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
                    key1.append([i,j])
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
                    key2.append([i,j])
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
    output_image_file = input_image_file.split('.')[0] + "_processed.png"
    output.save(output_image_file)
    
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

    output = Image.fromarray(testimage_array)
    output.show()

if __name__ == '__main__':
    input_image_file = "chest_mri.jpeg"
    medical_stego_encrypt(input_image_file)

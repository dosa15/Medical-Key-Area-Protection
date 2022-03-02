import docx
import zipfile
import random
import sys

import numpy as np
from PIL import Image
import cv2

# docxpath = sys.argv[1]
destpath = './tmp/'
intmpath = "word/media/"
cmppath = './output/'

if __name__ == '__main__':
    image1 = Image.open(destpath + 'compressed/op1_image1.tif')
    image1_array = np.asarray(image1)

    decryption_key = np.load('key.npy')
    
    docText = ''
    for dni in decryption_key:
        # print(image1_array[dni[0], dni[1]])
        docText += chr(image1_array[dni[0], dni[1], 0])
    print(docText)

    output = cv2.fastNlMeansDenoisingColored(image1_array, None, 2, 2, 7, 21)
    Image.fromarray(output).show()
import docx
import zipfile
import random
import sys

import numpy as np
from PIL import Image
from rsa import decrypt, encrypt

# docxpath = sys.argv[1]
destpath = './tmp/'
intmpath = "word/media/"
cmppath = './output/'

if __name__ == '__main__':
    image1 = Image.open(destpath + intmpath + "image1.tif")
    image1_array = np.asarray(image1)

    decryption_key = np.load('key.npy')
    
    docText = ''
    for dni in decryption_key:
        print(image1_array[dni[0], dni[1]])
        docText += chr(image1_array[dni[0], dni[1], 0])
    print(docText)
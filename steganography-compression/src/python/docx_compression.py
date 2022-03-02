import docx
import zipfile
import random
import sys

import numpy as np
from PIL import Image
from rsa import encrypt

docxpath = sys.argv[1]
destpath = './tmp/'
intmpath = "word/media/"


def get_document_text(path):
    document_text = docx.Document(path)
    docText = '\n\n'.join(
        paragraph.text for paragraph in document_text.paragraphs
    )
    return docText


def get_document_images(file_path, destination_path):
    image_names = list()
    document_media = zipfile.ZipFile(file_path)
    for info in document_media.infolist():
        if info.filename.endswith((".png", ".jpeg", ".gif", ".tif", ".tiff")):
            image_names.append(info.filename)
            document_media.extract(info.filename, destination_path)
    document_media.close()
    return image_names


def steganography_text2img(image_array):
    width = image_array.shape[1]
    encryption_noise_indices = random.sample(range(1, image_array.shape[0] * image_array.shape[1]), len(docText))
    encryption_noise = []
    for eni, char in zip(encryption_noise_indices, list(docText)):
        encryption_noise.append([int(eni / width), eni % width])
        image_array[int(eni / width), eni % width] = [ord(char), 0, 0]
    return encryption_noise


# encryption_key = np.empty(image1_array.shape)
# for i in range(image1_array.shape[0]):
#     for j in range(image1_array.shape[1]):
#         pixel = image1_array[i, j]
#         encrypt_pixel = [False] * len(pixel)
#         encrypt_pixel[np.where(pixel == min(pixel))[0][0]] = True
#         encryption_key[i, j] = encrypt_pixel
# # print(encryption_key)
# print(np.where(encryption_key == 1))


if __name__ == '__main__':
    docText = get_document_text(docxpath)
    # print(docText)
    images = get_document_images(docxpath, destpath)

    image1 = Image.open(destpath + images[0])
    image1.show()
    image1_array = np.asarray(image1)
    encryption_key = steganography_text2img(image1_array)

    output = Image.fromarray(image1_array)
    output.show()
    output_filetype = images[0].split('/')[-1].split('.')[-1]
    output.save(destpath + 'compressed/op1_' + docxpath.split('.')[0] + '.' + output_filetype)
    np.save('key.npy', encryption_key)

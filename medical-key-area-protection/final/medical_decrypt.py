from pickletools import optimize
import qrcode
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode
import ast
import cv2


def numpy_to_bytes(arr: np.array) -> str:
    arr_dtype = bytearray(str(arr.dtype), 'utf-8')
    arr_shape = bytearray(','.join([str(a) for a in arr.shape]), 'utf-8')
    sep = bytearray('|', 'utf-8')
    arr_bytes = arr.ravel().tobytes()
    to_return = arr_dtype + sep + arr_shape + sep + arr_bytes
    return to_return

def bytes_to_numpy(serialized_arr: str) -> np.array:
    sep = '|'.encode('utf-8')
    i_0 = serialized_arr.find(sep)
    i_1 = serialized_arr.find(sep, i_0 + 1)
    arr_dtype = serialized_arr[:i_0].decode('utf-8')
    arr_shape = tuple([int(a) for a in serialized_arr[i_0 + 1:i_1].decode('utf-8').split(',')])
    arr_str = serialized_arr[i_1 + 1:]
    arr = np.frombuffer(arr_str, dtype = arr_dtype).reshape(arr_shape)
    return arr


def medical_stego_decrypt(med_img_file, diagnostic_file):
    med_img = Image.open(med_img_file)
    med_img_array = np.asarray(med_img)

    diagnostic = open(diagnostic_file, "w")

    key = list(np.load('key.npy', allow_pickle=True))
    # print(key)
    
    key_area_str = ''
    key_area_loc = key.pop()
    mode_pixels = key.pop()
    for key0, mode_pixel in zip(key, mode_pixels):
        for [i, j, x] in key0:
            key_area_str += chr(med_img_array[i, j][x])
            med_img_array[i, j][x] = mode_pixel

    img_qr_array = med_img_array[key_area_loc[1]:key_area_loc[3], key_area_loc[0]:key_area_loc[2]]
    img_qr = Image.fromarray(img_qr_array)
    img_qr.show()
    res = decode(img_qr)
    for i in res:
        diagnostic.write(i.data.decode("utf-8"))
        print("The diagnostic report was recovered into ", diagnostic.name)
    med_img = Image.fromarray(med_img_array)
    med_img.show()
    open("temp2.txt", "w").write(key_area_str)
    key_area = np.load(".ka.npy")
    med_img.paste(Image.fromarray(key_area), key_area_loc)
    med_img.show()
    output_file = med_img_file.split('_stego.')[0] + "_decrypted.jpeg"
    med_img.save(output_file)


if __name__ == "__main__":
    med_img_file = "chest_mri_processed.png"
    diagnostic_file = "diagnostic_decrypted.txt"
    medical_stego_decrypt(med_img_file, diagnostic_file)


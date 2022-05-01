from pickletools import optimize
import qrcode
import pyqrcode
import numpy as np
from PIL import Image
import ast

med_img = Image.open('chest_mri.jpeg')
med_img_array = np.asarray(med_img)

diagnostic = open("diagnostic.txt", "r")
diagnostic_text = diagnostic.read()

qr = qrcode.QRCode(box_size=1)
qr.add_data(diagnostic_text)
qr.make(fit=True)
img_qr = qr.make_image()
img_qr_array = np.asarray(img_qr)
print(img_qr_array.shape)
# with np.printoptions(threshold=np.inf):
#     print(img_qr_array)
img_qr.show()
<<<<<<< HEAD
img_qr.save('QR.jpeg')
=======

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

temp = med_img_array[0:img_qr.size[0], 0:img_qr.size[1]]
temp_str = bytes(numpy_to_bytes(temp))
x = str(temp_str) + "-KEY-AREA-" + diagnostic_text
print(len(x))
# qr1 = qrcode.QRCode(
#     version=2,      # use upper level version
#     error_correction=qrcode.constants.ERROR_CORRECT_M,
#     box_size=1
# )
# qr1.add_data(x, optimize=0)
# qr1.make()
# img_qr = qr1.make_image()
url = pyqrcode.create(x)
url.png('med-qr.png', scale = 1)
img_qr = Image.open("med-qr.png")
print(img_qr.size)
temp_str = ast.literal_eval(x.split("-KEY-AREA-")[0])
temp = bytes_to_numpy(temp_str)
# print(temp)

# Hide img_qr inside med_img here
# 
#  
# for i in range(img_qr_array.shape[1]):
#     for j in range(img_qr_array.shape[0]):
#         print(img_qr_array[i, j], med_img_array[i, j][0])
#         med_img_array[i, j][0] += int(img_qr_array[i, j])

# with np.printoptions(threshold=np.inf):
# print(med_img_array)
output = Image.fromarray(med_img_array)
output.show()
>>>>>>> 56dd61946ce4c8dbc42f931986c95901a70e7c44

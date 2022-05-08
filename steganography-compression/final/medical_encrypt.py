from pickletools import optimize
import qrcode
import numpy as np
from PIL import Image
import ast
import cv2
KAS = None

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


def medical_stego_encrypt(med_img_file, diagnostic_file):
    med_img = Image.open(med_img_file)
    med_img_array = np.asarray(med_img)

    diagnostic = open(diagnostic_file, "r")
    diagnostic_text = diagnostic.read()

    qr = qrcode.QRCode(box_size=1)
    qr.add_data(diagnostic_text)
    qr.make(fit=True)
    img_qr = qr.make_image()
    print(img_qr.size)
    # img_qr_array = np.asarray(img_qr)
    # print(img_qr_array.shape)
    # with np.printoptions(threshold=np.inf):
    #     print(img_qr_array)
    img_qr.show()

    med_img2 = cv2.imread(med_img_file)
    ROI = cv2.selectROI("Select Rois",med_img2)
    print(ROI)

    key_area_loc = [ROI[0] + ROI[2]/2, ROI[1] + ROI[3]/2]
    key_area_loc = [int(key_area_loc[0]-img_qr.size[0]/2), int(key_area_loc[1]-img_qr.size[1]/2)]
    key_area_loc[0] = 0 if key_area_loc[0] < 0 else key_area_loc[0]
    key_area_loc[0] = med_img.size[0]-img_qr.size[0] if key_area_loc[0] > med_img.size[0]-img_qr.size[0] else key_area_loc[0]
    key_area_loc[1] = 0 if key_area_loc[1] < 0 else key_area_loc[1]
    key_area_loc[1] = med_img.size[1]-img_qr.size[1] if key_area_loc[1] > med_img.size[1]-img_qr.size[1] else key_area_loc[1]
    print(key_area_loc)

    key_area = med_img_array[key_area_loc[1]:key_area_loc[1]+img_qr.size[1], key_area_loc[0]:key_area_loc[0]+img_qr.size[0]]
    Image.fromarray(key_area).show(title="Key Area")
    np.save(".ka.npy", key_area)
    key_area_str = numpy_to_bytes(key_area)
    global KAS
    print(len(key_area_str))
    # print(type(key_area_str))
    # print(key_area_str)
    # key_area_str = key_area_str.decode()
    # print("kal")
    # print(key_area_loc)
    med_img.paste(img_qr, key_area_loc)
    # print(key_area_loc)
    med_img_array = np.asarray(med_img)
    Image.fromarray(med_img_array).show()

    mode_pixels = list()
    mode_pixels.append(np.argsort(np.bincount(med_img_array.flatten()))[-1])
    mode_pixels.append(np.argsort(np.bincount(med_img_array.flatten()))[-2])
    print("Most common pixel value = ", mode_pixels[0], " occurring ", np.bincount(med_img_array.flatten())[mode_pixels[0]], " times")
    print("Second most common pixel value = ", mode_pixels[1], " occurring ", np.bincount(med_img_array.flatten())[mode_pixels[1]], " times")

    key_area_enc = list(str(key_area_str))[-1::-1]
    # print("LEN to encode:", len(key_area_enc))
    # print(key_area_str)
    open("temp1.txt", "w").write(str(bytes(key_area_str)))
    key = list()

    for mode_pixel in mode_pixels:
        key0 = list()
        for i in range(med_img_array.shape[0]):
            for j in range(med_img_array.shape[1]):
                
                if len(key_area_enc) > 0 and med_img_array[i, j][0] == mode_pixel:
                    key0.append([i,j,0])
                    x = ord(key_area_enc.pop())
                    # print(chr(x), end='')
                    med_img_array[i, j][0] = x
                
                if len(key_area_enc) > 0 and med_img_array[i, j][1] == mode_pixel:
                    key0.append([i,j,1])
                    x = ord(key_area_enc.pop())
                    # print(chr(x), end='')
                    med_img_array[i, j][1] = x
                
                if len(key_area_enc) > 0 and med_img_array[i, j][2] == mode_pixel:
                    key0.append([i,j,2])
                    x = ord(key_area_enc.pop())
                    # print(chr(x), end='')
                    med_img_array[i, j][2] = x
                
                if len(key_area_enc) < 1:
                    break

            if len(key_area_enc) < 1:
                break
        
        key.append(key0)
        if len(key_area_enc) < 1:
            break
    # print("LEN:", len(key_area_enc))
    key.append(mode_pixels)
    key.append(key_area_loc)
    # img_qr_array = med_img_array[key_area_loc[1]:key_area_loc[3], key_area_loc[0]:key_area_loc[2]]
    # Image.fromarray(img_qr_array).show(title="QR CODE")
    key = np.array(key, dtype=object)
    np.save("key.npy", key)
    output = Image.fromarray(med_img_array)
    output_image_file = med_img_file.split('.')[0] + "_processed.png"
    output.save(output_image_file)
    output.show()


if __name__ == "__main__":
    med_img_file = 'chest_mri.jpeg'
    diagnostic_file = 'diagnostic.txt'
    medical_stego_encrypt(med_img_file, diagnostic_file)
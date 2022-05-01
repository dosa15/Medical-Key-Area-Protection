import qrcode
import numpy as np
from PIL import Image

med_img = Image.open('chest_mri.jpeg')
med_img_array = np.asfarray(med_img)

diagnostic = open("diagnostic.txt", "r")
diagnostic_text = diagnostic.read()

qr = qrcode.QRCode(box_size=1)
qr.add_data(diagnostic_text)
qr.make()
img_qr = qr.make_image()
img_qr_array = np.asfarray(img_qr)
print(img_qr_array.shape)
# with np.printoptions(threshold=np.inf):
#     print(img_qr_array)
img_qr.show()

# Hide img_qr inside med_img here
# 
# 
for i in range(img_qr_array.shape[1]):
    for j in range(img_qr_array.shape[0]):
        print(img_qr_array[i, j])
        med_img_array[i, j][0] += int(img_qr_array[i, j])

# with np.printoptions(threshold=np.inf):
# print(med_img_array)
output = Image.fromarray(med_img_array)
output.show()
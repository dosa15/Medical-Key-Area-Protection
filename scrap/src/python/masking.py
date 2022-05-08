from PIL import Image

Scanreport= Image.open('chest_mri.jpeg')
QRimage= Image.open('QR.jpeg')

Scanreport.paste(QRimage,(0,0))
Scanreport.show()

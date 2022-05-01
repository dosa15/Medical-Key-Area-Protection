import numpy as np
import argparse
import cv2
from PIL import Image

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "chest_mri.jpeg")
#ap.add_argument("-r", "--radius", type = int,
#	help = "radius of Gaussian blur; must be odd")
#args = vars(ap.parse_args())
# load the image and convert it to grayscale
img = cv2.imread('dental.jpeg')
orig = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# perform a naive attempt to find the (x, y) coordinates of
# the area of the image with the largest intensity value
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
cv2.circle(img, maxLoc, 5, (255, 0, 0), 2)
# display the results of the naive attempt
print(maxLoc)
cv2.imshow("Naive", img)
cv2.waitKey(0)
maxLoc=tuple([x-60 for x in maxLoc])
Scanreport= Image.open('dental.jpeg')
QRimage= Image.open('QR.jpeg')

Scanreport.paste(QRimage,maxLoc)
Scanreport.show()

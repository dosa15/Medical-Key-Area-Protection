from msilib.schema import File
from functools import reduce
import numpy as np

from PIL import Image
from pandas import array

testimage=Image.open('src\\python\\dice.jpg')
testimage_array= np.asarray(testimage)
width,height=testimage.size

for x in range(0,width,6):
    for y in range(0,height,6):
        #r,g,b=testimage.getpixel((x,y))
        #r1,b1,g1 = testimage.getpixel((x+1,y+1))
        #rt,bt,gt = r,g,b
        #r,g,b = testimage.putpixel((x,y),(r1,b1,g1))
        #r1,g1,b1 =testimage.putpixel((x+1,y+1),(rt,bt,gt))
        for i in range(0,6):
            try:    
                pixel1 = testimage_array[x+i,y+i]
                pixel2 = testimage_array[i-x,i-y]
                pixel3 = testimage_array[x+i,y]
                pixel4 = testimage_array[x,y+i]
                pixel5 = testimage_array[i-x,y]
                pixel6 = testimage_array[x,i-y]
                testimage_array[x+i,y+i]= pixel2
                testimage_array[i-x,i-y]= pixel1
                testimage_array[x,y+i]= pixel6
                testimage_array[x+i,y]= pixel5
                testimage_array[i-x,y]= pixel3
                testimage_array[x,i-y]= pixel4
            except:
                print(x,y)
testimage= Image.fromarray(testimage_array)
testimage.show()



from msilib.schema import File
from functools import reduce
import numpy as np

from PIL import Image
from pandas import array

testimage=Image.open('chest_mri.jpeg')
testimage.show()
#testimage= Image.open('src\\python\\distored.jpg')
testimage_array= np.asarray(testimage)
width,height=testimage.size

for x in range(0,width,32):
    for y in range(0,height,32):
        #r,g,b=testimage.getpixel((x,y))
        #r1,b1,g1 = testimage.getpixel((x+1,y+1))
        #rt,bt,gt = r,g,b
        #r,g,b = testimage.putpixel((x,y),(r1,b1,g1))
        #r1,g1,b1 =testimage.putpixel((x+1,y+1),(rt,bt,gt))
    
        for i in range(0,32):
            for j in range(0,16):
                try:
                    p1= testimage_array[x+i,y+j]
                    p2= testimage_array[abs((x+i)-(x+31))+x,abs((y+j)-(y+31))+y]

                    testimage_array[abs((x+i)-(x+31))+x,abs((y+j)-(y+31))+y]=p1
                    testimage_array[x+i,y+j] = p2
                except:
                    
                    print()
        
testimage= Image.fromarray(testimage_array)
testimage.save('src\python\distored.jpg')
testimage.show()




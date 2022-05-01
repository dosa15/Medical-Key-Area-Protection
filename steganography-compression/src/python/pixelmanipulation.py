# from msilib.schema import File
from functools import reduce
import numpy as np

from PIL import Image
from pandas import array

testimage=Image.open('chest_mri.jpeg')
testimage.show()
#testimage= Image.open('src\\python\\distored.jpg')
testimage_array= np.asarray(testimage)
width,height=testimage.size

frame_size = 31
for x in range(0,width,frame_size):
    for y in range(0,height,frame_size):
        # r,g,b=testimage.getpixel((x,y))
        # r1,b1,g1 = testimage.getpixel((x+1,y+1))
        # rt,bt,gt = r,g,b
        # r,g,b = testimage.putpixel((x,y),(r1,b1,g1))
        # r1,g1,b1 =testimage.putpixel((x+1,y+1),(rt,bt,gt))
    
        # for i in range(0,frame_size-1):
        #     for j in range(0,frame_size-1):
        #         try:
        #             if (width-x <= frame_size) or (height-y <= frame_size):
        #                 break
        #             p1 = testimage_array[x+i, y+j]
        #             p2 = testimage_array[abs(i-frame_size)+x, abs(j-frame_size)+y]

        #             testimage_array[abs(i-frame_size)+x, abs(j-frame_size)+y] = p1
        #             testimage_array[x+i, y+j] = p2
        #         except:
        #             print(x, y, i, j)
        testimage_array[x:x+frame_size, y:y+frame_size] = np.swapaxes(testimage_array[x:x+frame_size, y:y+frame_size], 0, 1)
        
testimage = Image.fromarray(testimage_array)
# testimage.save('src\python\distorted.jpeg')
testimage.save('distorted.jpeg')

testimage.show()




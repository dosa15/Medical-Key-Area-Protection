from ast import For, If
from PIL import Image
from functools import reduce
from math import gcd

def lcm(x,y):
    try:
        if(x>y):
            greater = x
        else:
            greater = y
        while(True):
            if((greater%x==0) and (greater%y==0)):
                lcm=greater
                break
            greater=greater+1
        return lcm
    except:
        print("")
    


one=Image.open('testimage.jpg')
two= Image.open('final.jpg')
one.show()
two.show()
def manipulation(first, second):
    width,height = first.size
    new_image=Image.new("RGB",(width,height),"white")
    for x in range(width):
        for y in range(height):
            r,g,b =first.getpixel((x,y))
            r1,g1,b1= second.getpixel((x,y))
            if(r==0) or (g==0) or (b==0):
                r_=0
                b_=0
                g_=0
            else:
                r_=r1/r
                g_=g1/g
                b_=b1/b

            new_pixel=(int(r_),int(g_),int(b_))
            new_image.putpixel((x,y),new_pixel)
    return new_image

new_image = manipulation(one,two)
new_image.show()
new_image.save('final.jpg',"PNG")

#print(image.size)
#print(new_image.size)
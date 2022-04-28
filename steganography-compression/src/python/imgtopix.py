from ast import For, If
from turtle import width
from PIL import Image
from functools import reduce
from math import gcd

def lcm(x,y):
    if(x==0) or (y==0):
        if(x>y):
            lcm=x
        else:
            lcm=y
       
    else:
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


one=Image.open('two1.jpg')
two= Image.open('two2.jpg')
one.show()
two.show()
def manipulation(first, second):
    width,height = first.size
    new_image=Image.new("RGB",(width,height),"white")
    for x in range(width):
        for y in range(height):
            r,g,b =first.getpixel((x,y))
            r1,g1,b1= second.getpixel((x,y))
            r_=lcm(r,r1)
            g_=lcm(g,g1)
            b_=lcm(b,b1)

            new_pixel=(int(r_),int(g_),int(b_))
            new_image.putpixel((x,y),new_pixel)
    return new_image

new_image = manipulation(one,two)
new_image.show()
new_image.save('final.jpg',"PNG")

width,height= new_image.size
key1=Image.new("RGB",(width,height),"white")
key2=Image.new("RGB",(width,height),"white")

for x in range(width):
    for y in range(height):
        r,g,b=new_image.getpixel((x,y))
        r1,g1,b1=one.getpixel((x,y))
        r2,g2,b2=two.getpixel((x,y))
        if(r1==0)or(g1==0)or(b1==0)or(r2==0)or(g2==0)or(b2==0):
            r1=1
            g1=1
            b1=1
            r2=1
            g2=1
            b2=1            
            
        rk1=r/r1
        gk1=g/g1        
        bk1=b/b1

        rk2=r/r2
        gk2=g/g2        
        bk2=b/b2

        new_pixelkey1=(int(rk1),int(gk1),int(bk1))
        key1.putpixel((x,y),new_pixelkey1)

        new_pixelkey2=(int(rk2),int(gk2),int(bk2))
        key2.putpixel((x,y),new_pixelkey2)
key1.show()
key2.show()

key1.save('key1.jpg','PNG')
key2.save('key2.jpg','PNG')


#print(image.size)
#print(new_image.size)
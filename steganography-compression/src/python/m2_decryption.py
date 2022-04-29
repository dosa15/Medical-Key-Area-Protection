from PIL import Image
from functools import reduce

encryptedfile=Image.open('final.jpg')

key1= Image.open('key1.jpg')
key2= Image.open('key2.jpg')
width,height=encryptedfile.size

new_image1=Image.new("RGB",(width,height),"white")
new_image2=Image.new("RGB",(width,height),"white")


for x in range(width):
    for y in range(height):
        r,g,b=encryptedfile.getpixel((x,y))
        rk1,gk1,bk1=key1.getpixel((x,y))
        rk2,gk2,bk2=key2.getpixel((x,y))
        if(rk1==0)or(gk1==0)or(bk1==0)or(rk2==0)or(gk2==0)or(bk2==0):
            rk1=1
            gk1=1
            bk1=1
            rk2=1
            gk2=1
            bk2=1            
        
        r1=r/rk1
        g1=g/gk1
        b1=b/bk1
        
        r2=r/rk2
        g2=g/gk2
        b2=b/bk2

        new_pixel1=(int(r1),int(g1),int(b1))
        new_image1.putpixel((x,y),new_pixel1)

        new_pixel2=(int(r2),int(g2),int(b2))
        new_image2.putpixel((x,y),new_pixel2)        

new_image1.show()
new_image2.show()

new_image1.save('image1afterdecrytion.jpg','PNG')
new_image2.save('image2afterdecrytion.jpg','PNG')

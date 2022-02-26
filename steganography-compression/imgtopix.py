from ast import For
from PIL import Image

image=Image.open('testimage.jpg')
def manipulation(image):
    width,height = image.size
    new_image=Image.new("RGB",(width,height),"white")
    for x in range(width):
        for y in range(height):
            r,g,b =image.getpixel((x,y))

            r_=g_=b_=(r+g+b)/3

            new_pixel=(int(r_),int(g_),int(b_))
            new_image.putpixel((x,y),new_pixel)
    return new_image

new_image = manipulation(image)
new_image.show()
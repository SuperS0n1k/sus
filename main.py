from PIL import Image
import numpy as np
img = Image.open("file.png")
print(img.mode) #RGB
print(img.size)



width = img.size[0] 
height = img.size[1] 
for i in range(0,width):# process all pixels
    for j in range(0,height):
        data = img.getpixel((i,j))
        #print(data) #(255, 0, 0)
        if (data[0]==255 and data[1]==255 and data[2]==255):
            img.putpixel((i,j),(44, 44, 44))
            
            
            for i in range(0,width):# process all pixels
    for j in range(0,height):
        data = img.getpixel((i,j))
        #print(data) #(0, 0, 255)
        if (data[0]==255 and data[1]==255 and data[2]==255):
            img.putpixel((i,j),(44, 44, 44))
            
img.show()

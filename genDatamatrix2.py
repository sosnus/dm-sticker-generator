import os
import treepoem
from PIL import Image, ImageDraw, ImageFilter, ImageFont

print("start")


#Settings
#30x15mm
output_picsize = (300, 150)


def gen_label(inputdata):
    
    output_picture = Image.new('RGB', output_picsize, (255, 255, 255))

    #Datamatrix
    datamatrix_image = treepoem.generate_barcode(barcode_type = 'datamatrix', data = inputdata[0])
    output_picture.paste(datamatrix_image, (20, 20))
    
    #datamatrix label
    fnt = ImageFont.truetype("Arial", 20)
    d = ImageDraw.Draw(output_picture)
    d.text((20,100), inputdata[0],font = fnt ,fill=(0,0,0))

    #labels
    fnt2 = ImageFont.truetype("Arial", 50)
    d2 = ImageDraw.Draw(output_picture)
    d2.text((100,15), inputdata[1],font = fnt2 ,fill=(0,0,0))


    fnt3 = ImageFont.truetype("Arial", 80)
    d3 = ImageDraw.Draw(output_picture)
    d3.text((100,50), inputdata[2],font = fnt3 ,fill=(0,0,0))


    #save image to file
    return output_picture    


tmp_file = gen_label(["qrcodecontent", "upline", "downline"])
tmp_file.convert('1').save('output.png')

print("DONE")






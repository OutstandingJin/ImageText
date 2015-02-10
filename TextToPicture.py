#-*- coding:UTF-8-*-
from PIL import ImageFont, ImageDraw
import sys
import Image
import chardet
import re

path = '/home/autstanding/Code/Python/ImageText/resources/'
content_text = path + '双城记.txt'

def DrawText():
    font_size = 5 

    font = ImageFont.truetype(path + "truetypefont.ttf", int(500/font_size))
    #font = ImageFont.truetype("aria.ttf", 100)
    im_base = Image.new("1", (int(1120/font_size), int(792/font_size)), "white")
    draw = ImageDraw.Draw(im_base)
    draw.text((0,0), unicode('雪', 'UTF-8'), font = font)
    draw.text((int(500/font_size),0), unicode('国', 'UTF-8'), font = font)
    im_base_data = list(im_base.getdata())
    
    #font = ImageFont.truetype(path + "truetypefont.ttf", font_size)
    font = ImageFont.truetype('/media/autstanding/066CA48F6CA47B57/Windows/Fonts/simsun.ttc', font_size)
    im = Image.new("1", (1120, 792), "white")
    line_space = 1
    line_number = 0
    row_number = 0
    content_traverse_index = 0
    content = ReadContent(path + "双城记.txt")
    draw = ImageDraw.Draw(im)

    for i in range(0, len(im_base_data)):
        if im_base_data[i] != 255:
            draw.text((int(i % int(1120/font_size)) * font_size,  int(i / int(792/font_size)) * font_size), content[i], font = font)
    del draw
    im.save(path + "test.jpg", "JPEG")
   
def ReadContent(content_text):
    content = ''
    with open(content_text, 'r') as content_file:
        content = content_file.read()
        content = content.decode(chardet.detect(content)['encoding'])
    content = re.sub(ur"([^\u4e00-\u9fa5])+",''  , content)
    return content

DrawText()

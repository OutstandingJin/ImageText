#-*- coding:UTF-8-*-
from PIL import ImageFont, ImageDraw
import sys
import Image
import chardet
import re

path = '/home/autstanding/Code/Python/ImageText/resources/'
content_text = path + '双城记.txt'

def DrawText():
    font_size = 23
    base_width = 1120 * 4
    base_height = 792
    font = ImageFont.truetype(path + "truetypefont.ttf", int(790/font_size))
    #font = ImageFont.truetype("aria.ttf", 100)
    im_base = Image.new("1", (int(base_width/font_size), int(base_height/font_size)), "white")
    draw = ImageDraw.Draw(im_base)
    draw.text((0,0), unicode('嘿', 'UTF-8'), font = font)
    draw.text((int(790/font_size),0), unicode('嘿', 'UTF-8'), font = font)
    draw.text((int(790 * 2/font_size),0), unicode('嘿', 'UTF-8'), font = font)
    draw.text((int(790 * 3/font_size),0), unicode('嘿', 'UTF-8'), font = font)
    im_base_data = list(im_base.getdata())
    
    #font = ImageFont.truetype(path + "truetypefont.ttf", font_size)
    font = ImageFont.truetype('/media/autstanding/066CA48F6CA47B57/Windows/Fonts/simkai.ttf', font_size)
    im = Image.new("1", (base_width , base_height), "white")
    line_space = 1
    row_space = 3
    line_number = 0
    row_number = 0
    min_line = 4096 
    max_line = 0
    min_row = 4096 
    max_row = 0 
    content_traverse_index = 0
    content = ReadContent(path + "双城记.txt")
    draw = ImageDraw.Draw(im)

    for i in range(0, len(im_base_data)):
        if im_base_data[i] == 255:
            row_number = i % int(base_width/font_size)
            line_number = int(i / int(base_width/font_size))
            if line_number >= 6 and line_number <= 36 and row_number >= 7 and row_number <= 132:
                draw.text((row_number * (font_size + row_space) + 400, line_number * (font_size + line_space) - 100), content[content_traverse_index], font = font)
                content_traverse_index += 1
            '''
            min_line = min(min_line, line_number)
            max_line = max(max_line, line_number)
            min_row = min(min_row, row_number)
            max_row = max(max_row, row_number)
            '''
    print content_traverse_index 
    print i - content_traverse_index
#    print (max_line - min_line) * (max_row - min_row)
#    print max_line,min_line,max_row,min_row
    del draw
    im.crop((0,0,1120,792)).save("/home/autstanding/letter1.jpg", "JPEG")
    im.crop((1121,0,2240,792)).save("/home/autstanding/letter2.jpg", "JPEG")
    im.crop((2241,0,3360,792)).save("/home/autstanding/letter3.jpg", "JPEG")
    im.crop((3361,0,4480,792)).save("/home/autstanding/letter4.jpg", "JPEG")
   
def ReadContent(content_text):
    content = ''
    with open(content_text , 'r') as content_file:
        content = content_file.read()
        content = content.decode(chardet.detect(content)['encoding'])
    content = re.sub(ur"([^\u4e00-\u9fa5])+",''  , content)
    return content

DrawText()

#-*- coding:UTF-8-*-
import Image
import ImageDraw
import ImageFont
import sys
import chardet

path = '/home/autstanding/Code/Python/resources/'
content_text = path + '双城记.txt'

def DrawText():
    im_base = Image.new("1", (1120, 792), "white")
    font_global = ImageFont.truetype(path + "truetypefont.ttf", 500)
    font_local = ImageFont.truetype(path + "truetypefont.ttf", 5)
    draw = ImageDraw.Draw(im_base)
    draw.text((0, 0), unicode('雪', 'UTF-8'), font = font_global)
    draw.text((500, 0), unicode('国', 'UTF-8'), font = font_global)
    draw = ImageDraw.Draw(im_top)
    im_base_data = list(im_base.getdata())
    line_space = 1
    line_number = 0
    row_number = 0
    content_traverse_index = 0
    content = ReadContent()

# there is cordinate transformation

    for i in range(0, int(len(im_base_data)/25)):
        if im_base_data[i -] != 255:
            draw.text((int(i / 1120) * 6, int(i / 5) * 5), content[content_traverse_index++], font = font_local)
    del draw
    im.save(path + "test.jpg", "JPEG")

def ReadContent(content_text):
    content = ''
    with open(content_text, 'r') as content_file:
        content = content_file.read().decode(chardet.detect(content)['encoding'])
    content = re.sub(ur"([^\u4e00-\u9fa5])+",''  , content)
    return content

DrawText()

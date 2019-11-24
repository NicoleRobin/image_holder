#/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate_image(static_dir, image_type, width, height, color):
    print(static_dir, image_type, width, height, color)
    image_dir = os.path.join(static_dir, 'image')
    mode = 'RGBA'
    if image_type == 'jpg':
        mode = 'YCbCr'
    
    width = int(width)
    height = int(height)
    image_name = '%sx%s_%s.%s' % (width, height, int(time.time()), image_type)
    image_path = os.path.join(image_dir, image_name)

    text = '%sx%s' % (width, height)
    image = Image.new(mode, (width, height), color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('font/fontawesome-webfont.ttf', 14)
    textwidth, textheight = draw.textsize(text, font)

    margin = 5
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, font=font)

    image.save(image_path)
    return image_path

if __name__ == '__main__':
    image_path = generate_image('/data/static/', 'jpg', 500, 500, '#FFFFFF')
    print(image_path)

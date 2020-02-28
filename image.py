#/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time
import random


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor


def rndColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def generate_image(static_dir, image_type, width, height, color):
    print(static_dir, image_type, width, height, color)

    mode = 'RGB'
    width = int(width)
    height = int(height)
    color_tuple = ImageColor.getcolor(color, mode)

    image = Image.new(mode, (width, height), color_tuple)

    image_dir = os.path.join(static_dir, 'image')
    image_name = '%sx%s_%s.%s' % (width, height, int(time.time()), image_type)
    image_path = os.path.join(image_dir, image_name)

    font = ImageFont.truetype('./font/consola.ttf', 36)
    draw = ImageDraw.Draw(image)
    mark_content = "nicojwzhang"
    for i, ch in enumerate(mark_content):
        draw.text((20*i + 10, 10), ch, font=font, fill=rndColor())

    image.save(image_path)

    print('image_path:%s' % (image_path))
    return image_path

if __name__ == '__main__':
    image_path = generate_image('/data/static/', 'jpg', 500, 500, '#FFFFFF')
    print(image_path)

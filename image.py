#/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from PIL import Image

def generate_image(image_type, width, height, color):
    print(image_type, width, height)
    mode = 'RGBA'
    if image_type == 'jpg':
        mode = 'YCbCr'
    
    width = int(width)
    height = int(height)
    image = Image.new(mode, (width, height), color)
    image_name = 'image/%sx%s_%s.%s' % (width, height, int(time.time()), image_type)
    image_path = 'static/' + image_name
    image.save(image_path)
    return image_name

if __name__ == '__main__':
    image_path = generate_image('jpg', 500, 500)
    print(image_path)

#!/usr/bin/env python
# -*- coding:utf-8

import os
from flask import Flask
from flask import request
from flask import url_for
from image import generate_image

app = Flask(__name__)

server_url = 'https://nicolerobin.top/'
static_dir = '/data/static/'

@app.route('/cgi-bin/image_holder', methods=['POST'])
def image_holder():
    if request.method == 'POST':
        if not request.is_json:
            return 'Not json fomat'

        request_json = request.get_json()
        if not request_json:
            return 'Get json data failed'

        image_type = request_json['image_type']
        height = request_json['height']
        width = request_json['width']
        color = request_json['color']
        image_path = generate_image(static_dir, image_type, width, height, color)
        print('image_path:' + image_path)
        image_url = image_path.replace(static_dir, server_url)
        print('image_url:' + image_url)
        return {
            'image_url':image_url
        }
    else:
        return 'Unsupport method'

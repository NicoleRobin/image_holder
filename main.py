#!/usr/bin/env python
# -*- coding:utf-8

from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from image import generate_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/image_holder', methods=['POST'])
@app.route('/image_holder/<image_path>', methods=['GET'])
def image_holder():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        if not request.is_json:
            return 'Not json fomat'

        request_json = request.get_json()
        if not request_json:
            return 'Get json data failed'

        image_type = request_json['image_type']
        height = request_json['height']
        width = request_json['width']
        color = request_json['color']
        image_path = generate_image(image_type, height, width, color)
        return {
            'image_url':url_for('static', filename=image_path)
        }
    else:
        return 'No support method'

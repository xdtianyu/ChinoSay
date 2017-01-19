#!/usr/bin/env python3

import textwrap

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os


W, H = (561, 450)
path = os.path.dirname(os.path.realpath(__file__))
cache_dir = 'data/'


def say(msg):
    img = Image.open(path + '/chino.jpg').convert("RGB")

    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype(path + "/wqy-microhei.ttc", size=48)
    w, h = draw.textsize(msg, font=fnt)
    lines = textwrap.wrap(msg, width=10)
    y_text = H - h - 10
    for line in reversed(lines):
        width, height = draw.textsize(line, font=fnt)
        draw.text(((W - width) / 2, y_text), line, (255, 255, 255), font=fnt)
        y_text -= height

    # img.show()
    import hashlib
    import time

    sha1 = hashlib.sha1()
    sha1.update(str(time.time()).encode('utf-8'))
    name = cache_dir + sha1.hexdigest() + '.jpg'

    if not os.path.exists(path + '/' + cache_dir):
        os.makedirs(path + '/' + cache_dir)

    img.save(path + '/' + name)
    return name
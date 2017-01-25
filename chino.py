#!/usr/bin/env python3

import textwrap

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os

path = os.path.dirname(os.path.realpath(__file__))
cache_dir = 'data/'
font = '/DroidSansFallbackFull.ttf'

images = [
    ('/chino.jpg', (255, 255, 255), 561, 450, 48, (256, 256)),
    ('/chino2.jpg', (0, 0, 0), 544, 545, 48, (256, 256))
]


def say(msg):
    results = list()
    for image in images:
        results.append(gen(image, msg))
    return results


def gen(image, msg):
    src, color, i_width, i_height, size, thumb_size = image

    import hashlib

    sha1 = hashlib.sha1()
    sha1.update((msg + str(image)).encode('utf-8'))
    name = cache_dir + sha1.hexdigest() + '.jpg'
    thumb = cache_dir + sha1.hexdigest() + '_thumb.jpg'

    if not os.path.exists(path + '/' + cache_dir):
        os.makedirs(path + '/' + cache_dir)

    if not os.path.exists(path + '/' + name):
        img = Image.open(path + src).convert("RGB")
        draw = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(path + font, size=size)
        w, h = draw.textsize(msg, font=fnt)
        lines = textwrap.wrap(msg, width=10)
        y_text = i_height - h - 10
        for line in reversed(lines):
            width, height = draw.textsize(line, font=fnt)
            draw.text(((i_width - width) / 2, y_text), line, color, font=fnt)
            y_text -= height
        # img.show()
        img.save(path + '/' + name)
        img.thumbnail(thumb_size)
        img.save(path + '/' + thumb)

    return thumb, name, i_width, i_height

gen(images[0], "哦哦哦")
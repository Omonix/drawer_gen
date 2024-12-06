from PIL import Image
import urllib.request
import time
import math
from tkinter import *

def lb_new_img(res, name):
    new_img = Image.new('RGB', (res[0], res[1]), (0, 0, 0))
    new_img.save(name)
    return new_img
def lb_draw_img(img):
    origin_img = Image.open(img)
    before = time.time()
    (old_width, old_height) = origin_img.size
    if new_resolution['delta'] == (0, 0):
         new_resolution['delta'] = (old_width, old_height)
    new_img = lb_new_img((new_resolution['delta'][0], new_resolution['delta'][1]), 'after.jpg')
    (new_width, new_height) = new_img.size
    for i in range(new_width):
        for j in range(new_height):
            pix = origin_img.getpixel((i * (old_width / new_width), j * (old_height / new_height)))
            mini = {'dif': 255, 'id': 0}
            for k in range(len(listColor)):
                difference = abs(pix[0] - listColor[k][0]) + abs(pix[1] - listColor[k][1]) + abs(pix[2] - listColor[k][2])
                if difference < mini['dif']:
                    mini['id'] = k
                    mini['dif'] = difference
            new_img.putpixel((i, j), listColor[mini['id']])
    new_img.save('after.' + img.split('.')[-1])
    new_img.close()
    after = time.time() - before
    minu = after / 60
    origin_img.close()
    return [math.floor(minu), math.floor(minu % 1 * 60), math.floor(after % 1 * 1000)]

listColor = [(0, 0, 0), (102, 102, 102), (0, 80, 205), (255, 255, 255), (170, 170 ,170), (36, 201, 255), (2, 116, 31), (152, 0, 0), (149, 65, 19), (15, 176, 60), (255, 0, 21), (255, 120, 39), (176, 112, 24), (155, 0, 80), (203, 89, 86), (254, 193, 40), (255, 1, 142), (254, 175, 167)]
new_resolution = {'a': (), 'b': (), 'delta': ()}
old_color = (0, 0)
urllib.request.urlretrieve(input('\033[36mURl : '), 'before.jpg')
time_draw = lb_draw_img('./before.jpg')
print(f'\033[33m{time_draw[0]}min', f'{time_draw[1]}sec', f'{time_draw[2]}ms\033[0m')

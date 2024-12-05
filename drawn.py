from PIL import Image
import urllib.request
import time
import math
from pynput import mouse


def lb_mouse_event(x, y, button, pressed):
    global new_resolution
    if button == mouse.Button.left and pressed:
        new_resolution = (x, y)
    elif button == mouse.Button.left and not pressed:
        new_resolution = (abs(new_resolution[0] - x), abs(new_resolution[1] - y))
        listener.stop()
def lb_new_img(res, name):
    new_img = Image.new('RGB', (res[0], res[1]), (0, 0, 0))
    new_img.save(name)
    return new_img
def lb_draw_img(img, f):
    origin = Image.open(img)
    before = time.time()
    (width, height) = origin.size
    new_img = lb_new_img((width // f, height // f), 'after.jpg')
    for i in range(width):
        for j in range(height):
            if j % f == 0 and i % f == 0:
                pix = origin.getpixel((i, j))
                mini = {'color': (255, 255, 255), 'dif': 255}
                for k in listColor['color']:
                    difference = abs(pix[0] - k[0]) + abs(pix[1] - k[1]) + abs(pix[2] - k[2])
                    if difference < mini['dif']: 
                        mini['color'] = k
                        mini['dif'] = difference
                new_img.putpixel((i // f - 1, j // f - 1), mini['color'])
    new_img.save('after.' + img.split('.')[-1])
    new_img.close()
    after = time.time() - before
    minu = after / 60
    origin.close()
    return [math.floor(minu), math.floor(minu % 1 * 60), math.floor(after % 1 * 1000)]

listColor = {'color': [(0, 0, 0), (102, 102, 102), (0, 80, 205), (255, 255, 255), (170, 170 ,170), (36, 201, 255), (2, 116, 31), (152, 0, 0), (149, 65, 19), (15, 176, 60), (255, 0, 21), (255, 120, 39), (176, 112, 24), (155, 0, 80), (203, 89, 86), (254, 193, 40), (255, 1, 142), (254, 175, 167)], 'xy': [(462, 456), (504, 452), (546, 452), (461, 496), (501, 500), (546, 497), (455, 544), (496, 543), (555, 542), (456, 596), (507, 594), (556, 590), (459, 640), (508, 639), (554, 641), (469, 692), (507, 692), (554, 691)]}
new_resolution = (0, 0)
urllib.request.urlretrieve(input('URl : '), 'before.jpg')
time_draw = lb_draw_img('./before.jpg', int(input('Divided by : ')))
print(f'\033[33m{time_draw[0]}min', f'{time_draw[1]}sec', f'{time_draw[2]}ms\033[0m')

#listener = mouse.Listener(on_click=lb_mouse_event)
#listener.start()
#listener.join()
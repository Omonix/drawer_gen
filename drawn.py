from PIL import Image
import time
import math

listColor = [(0, 0, 0), (102, 102, 102), (0, 80, 205), (255, 255, 255), (170, 170 ,170), (36, 201, 255), (2, 116, 31), (152, 0, 0), (149, 65, 19), (15, 176, 60), (255, 0, 21), (255, 120, 39), (176, 112, 24), (155, 0, 80), (203, 89, 86), (254, 193, 40), (255, 1, 142), (254, 175, 167)]

url_origin = input('File path : ')
origin = Image.open(url_origin)
before = time.time()
(width, height) = origin.size
for i in range(width // 1):
    for j in range(height // 1):
        pix = origin.getpixel((i, j))
        mini = {'color': (255, 255, 255), 'dif': 255}
        for k in listColor:
            difference = abs(pix[0] - k[0]) + abs(pix[1] - k[1]) + abs(pix[2] - k[2])
            if difference < mini['dif']: 
                mini['color'] = k
                mini['dif'] = difference
                #print(mini['dif'], mini['color'], pix)
        origin.putpixel((i, j), mini['color'])
origin.save(url_origin.split('/')[-1].split('.')[0] + '_copied.' + url_origin.split('.')[-1])
after = time.time() - before
minu = after / 60
print(f'{math.floor(minu)}min', f'{math.floor(minu % 1 * 60)}sec', f'{math.floor(after % 1 * 1000)}ms')
origin.close()
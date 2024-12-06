from tkinter import *
import time
from PIL import Image
import urllib.request
import math

def lb_preshot_img():
    if urler.get() != '':
        urllib.request.urlretrieve(urler.get(), './temp/before.jpg')
        imag = Image.open('./temp//before.jpg')
        old_resolution.set(f'{imag.size[0]}x{imag.size[1]}')
        imag.close()
        urler.set('')
        print('\033[32mImage load succefully !\033[0m')
    else:
        print('\033[31mNo URL !\033[0m')
def lb_new_img(res, name):
    new_img = Image.new('RGB', (int(res[0]), int(res[1])), (0, 0, 0))
    new_img.save(f'./archive/{name}.jpg')
    return new_img
def lb_get_res():
    if new_resolution.get() == '':
        return old_resolution.get().split('x')
    else:
        return new_resolution.get().split('x')
def lb_draw_img():
    new_res = lb_get_res()
    name = name_file.get()
    origin_img = Image.open('./temp/before.jpg')
    before = time.time()
    (old_width, old_height) = origin_img.size
    new_img = lb_new_img(new_res, name)
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
    new_img.save(f'./archive/{name}.jpg')
    new_img.close()
    after = time.time() - before
    minu = after / 60
    origin_img.close()
    timing.set(f'{math.floor(minu)}min {math.floor(minu % 1 * 60)}sec {math.floor(after % 1 * 1000)}ms')
    print(f'\033[33m{math.floor(minu)}min', f'{math.floor(minu % 1 * 60)}sec', f'{math.floor(after % 1 * 1000)}ms\033[0m')
def lb_submit():
    global bg_color
    if old_resolution.get() != '' and name_file.get() != '':
        lb_draw_img()
        old_resolution.set('')
        new_resolution.set('')
        name_file.set('')
    else:
        print('\033[31mError : missing arg !\033[0m')

screen = Tk()
screen.geometry('400x400')
screen.iconbitmap('./icon.ico')
screen.title('Redrawer')
screen['bg'] = '#191919'
screen.resizable(height=False, width=False)

listColor = [(0, 0, 0), (102, 102, 102), (0, 80, 205), (255, 255, 255), (170, 170 ,170), (36, 201, 255), (2, 116, 31), (152, 0, 0), (149, 65, 19), (15, 176, 60), (255, 0, 21), (255, 120, 39), (176, 112, 24), (155, 0, 80), (203, 89, 86), (254, 193, 40), (255, 1, 142), (254, 175, 167)]
urler = StringVar()
new_resolution = StringVar()
old_resolution = StringVar()
name_file = StringVar()
timing = StringVar()

url_txt = Label(screen, text='URL :', font=(20), fg='white', bg='#191919').place(x='10', y='10')
url_put = Entry(screen, textvariable=urler).place(x='70', y='15', width='250')
load = Button(screen, text='Load image', fg='white', bg='#191919', command=lb_preshot_img).place(x='325', y='12.5')
res_txt = Label(screen, text='RES :', font=(20), fg='white', bg='#191919').place(x='10', y='40')
resolution_origin = Label(screen, textvariable=old_resolution, font=(20), fg='white', bg='#191919').place(x='70', y='40')
arrow = Label(screen, text='>', font=(20), fg='white', bg='#191919').place(x='150', y='40')
resolution_new = Entry(screen, textvariable=new_resolution).place(x='180', y='45', width='70')
name_txt = Label(screen, text='NAME :', font=(20), fg='white', bg='#191919').place(x='10', y='70')
name_put = Entry(screen, textvariable=name_file).place(x='90', y='75')
finished = Label(screen, text='Finished in : ', font=(20), fg='white', bg='#191919').place(x='10', y='100')
timer = Label(screen, textvariable=timing, font=(20), fg='yellow', bg='#191919').place(x='130', y='100')

button = Button(screen, text='Submit', font=(10), fg='white', bg='#191919', command=lb_submit).place(relx='0.5', rely='0.9', anchor=CENTER)

screen.mainloop()
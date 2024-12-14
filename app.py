from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo, showwarning
import time
from PIL import Image
import urllib.request
import math
import webbrowser

def lb_upper(text):
    return text[0].upper() + text[1:].lower()
def lb_preshot_img(have_filer):
    global have_file
    if urler.get() != '':
        if have_filer == False:
            urllib.request.urlretrieve(urler.get(), './temp/before.jpg')
            imag = Image.open('./temp/before.jpg')
            old_resolution.set(f'{imag.size[0]}x{imag.size[1]}')
            imag.close()
            urler.set('')
        else:
            imag = Image.open(urler.get())
            old_resolution.set(f'{imag.size[0]}x{imag.size[1]}')
            imag.close()
        have_file = False
        showinfo(title='Successfully !', message='Image load successfully !')
        print('\033[32mImage load successfully !\033[0m')
    else:
        showwarning(title='Error', message='No URL !')
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
def lb_draw_img(url):
    new_res = lb_get_res()
    name = name_file.get()
    origin_img = Image.open(url)
    before = time.time()
    (old_width, old_height) = origin_img.size
    new_img = lb_new_img(new_res, name)
    (new_width, new_height) = new_img.size
    for i in range(new_width):
        for j in range(new_height):
            pix = origin_img.getpixel((i * (old_width / new_width), j * (old_height / new_height)))
            mini = {'dif': 255, 'id': 0}
            for k in range(len(palette)):
                difference = abs(pix[0] - palette[k][0]) + abs(pix[1] - palette[k][1]) + abs(pix[2] - palette[k][2])
                if difference < mini['dif']:
                    mini['id'] = k
                    mini['dif'] = difference
            new_img.putpixel((i, j), palette[mini['id']])
    new_img.save(f'./archive/{name}.jpg')
    new_img.close()
    after = time.time() - before
    minu = after / 60
    origin_img.close()
    showinfo(title='Successfully !', message=f'Finished in {math.floor(minu)}min {math.floor(minu % 1 * 60)}sec {math.floor(after % 1 * 1000)}ms')
    print(f'\033[33m{math.floor(minu)}min', f'{math.floor(minu % 1 * 60)}sec', f'{math.floor(after % 1 * 1000)}ms\033[0m')
def lb_submit(url):
    global bg_color
    if old_resolution.get() != '' and name_file.get() != '':
        lb_draw_img(url)
        old_resolution.set('')
        new_resolution.set('')
        name_file.set('')
    else:
        showwarning(title='Error', message='Missing argument(s) !')
        print('\033[31mError : missing arg !\033[0m')
def lb_change_palette():
    global palette
    palette = listColor[int(choose_palette.get())]['colors']
def lb_open_file():
    global have_file
    global have_url
    file_url = fd.askopenfilename(filetypes=[('JPEG (*.jpg)', '*.jpg'), ('PNG (*.png)', '*.png'), ('ICO (*.ico)', '*.ico'), ('All files', '*.*')])
    urler.set(file_url)
    have_file = True
    have_url = file_url
def lb_quit():
    screen.destroy()
    screen.quit()
def lb_contact(contact):
    tab_contact = ['https://github.com/Omonix', 'https://www.instagram.com/omonyx_sama/']
    webbrowser.open(tab_contact[contact])
def lb_shortcut(key):
    if key.keysym == 'o':
        lb_open_file()
    elif key.keysym == 'ampersand':
        print(1)
    elif key.keysym == 'eacute':
        print(2)
    elif key.keysym == 'quotedbl':
        print(3)
    elif key.keysym == 'apostrophe':
        print(4)
    elif key.keysym == 'parenleft':
        print(5)
    elif key.keysym == 'minus':
        print(6)
    elif key.keysym == 'egrave':
        print(7)
    elif key.keysym == 'underscore':
        print(8)
    elif key.keysym == 'ccedilla':
        print(9)
    elif key.keysym == 'agrave':
        print(10)
def lb_create_childScreen(name, xy, parent):
    child = Toplevel(screen)
    child.geometry(xy)
    child.iconbitmap('./icon.ico')
    child.title(name)
    child['bg'] = '#191919'
    child.resizable(height=False, width=False)
    child.transient(parent)
    child.grab_set()
    return child
def lb_palette_handler():
    global listColor
    manager = lb_create_childScreen('Manage palette', '850x400', screen)
    manager.resizable(height=True, width=True)
    Button(manager, text='Add palette', fg='white', bg='#191919', command=lambda: lb_new_palette(manager, len(listColor))).place(x='10', y='10')
    screen.wait_window(manager)
def lb_new_palette(fen, num):
    name = lb_create_childScreen('Palette name', '200x150', fen)
    tset = StringVar()
    Label(name, text='New palette : ', fg='white', bg='#191919').place(x='75', y='50')
    Entry(name, textvariable=tset).place(x='50', y='75')
    Button(name, text='Create', fg='white', bg='#191919', command=lambda: name.destroy()).place(x='75', y='100')
    fen.wait_window(name)
    Label(fen, text=lb_upper(tset.get()), fg='white', bg='#191919').place(x=num * 75 - 130, y='10')
    listColor.append({'name': lb_upper(tset.get()), 'colors': []})
    Button(fen, text='Add color', fg='white', bg='#191919', command=lambda: lb_new_color(fen, num)).place(x=num * 75 - 130, y='30', width='70')
def lb_new_color(fen, num):
    test = StringVar()
    Entry(fen, textvariable=test).place(x=num * 75 - 130, y=len(listColor[num]['colors']) * 20 + 60, width='70')
    listColor[num]['colors'].append('re')

screen = Tk()
screen.geometry('400x400')
screen.iconbitmap('./icon.ico')
screen.title('Redrawer')
screen['bg'] = '#191919'
screen.resizable(height=False, width=False)
screen.bind('<Control-Key-o>', lb_shortcut)
screen.bind('<Control-Key-ampersand>', lb_shortcut)
screen.bind('<Control-Key-eacute>', lb_shortcut)
screen.bind('<Control-Key><">', lb_shortcut)
screen.bind("<Control-Key><'>", lb_shortcut)
screen.bind('<Control-Key-parenleft>', lb_shortcut)
screen.bind('<Control-Key-minus>', lb_shortcut)
screen.bind('<Control-Key-egrave>', lb_shortcut)
screen.bind('<Control-Key-underscore>', lb_shortcut)
screen.bind('<Control-Key-ccedilla>', lb_shortcut)
screen.bind('<Control-Key-agrave>', lb_shortcut)
menu_bar = Menu(screen)
menu_file = Menu(menu_bar, tearoff=0, bg='#ffffff', fg='#191919', activebackground='#191919', activeforeground='#ffffff')
menu_palette = Menu(menu_bar, tearoff=0, bg='#ffffff', fg='#191919', activebackground='#191919', activeforeground='#ffffff')
menu_contact = Menu(menu_bar, tearoff=0, bg='#ffffff', fg='#191919', activebackground='#191919', activeforeground='#ffffff')
menu_bar.add_cascade(label='File', menu=menu_file)
menu_bar.add_cascade(label='Palette', menu=menu_palette)
menu_bar.add_cascade(label='Contact', menu=menu_contact)

listColor = [{'name' : 'Gartic phone', 'colors' : [(0, 0, 0), (255, 255, 255), (102, 102, 102), (0, 80, 205), (255, 255, 255), (170, 170 ,170), (36, 201, 255), (2, 116, 31), (152, 0, 0), (149, 65, 19), (15, 176, 60), (255, 0, 21), (255, 120, 39), (176, 112, 24), (155, 0, 80), (203, 89, 86), (254, 193, 40), (255, 1, 142), (254, 175, 167)]}, {'name' : 'Basic', 'colors' : [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 0, 125), (255, 125, 0), (125, 255, 0), (0, 255, 125), (0, 125, 255), (125, 0, 255)]}, {'name' : 'Paint', 'colors' : [(0, 0, 0), (255, 255, 255), (127, 127, 127), (136, 0, 21), (237, 28, 36), (255, 127, 39), (255, 242, 0), (34, 177, 76), (0, 162, 232), (63, 72, 204), (163, 73, 164), (195, 195, 195), (185, 122, 87), (255, 174, 201), (255, 201, 14), (239, 228, 176), (181, 230, 29), (153, 217, 234), (112, 146, 190), (200, 191, 231)]}]
urler = StringVar()
new_resolution = StringVar()
old_resolution = StringVar()
name_file = StringVar()
have_file = False
have_url = './temp/before.jpg'
palette = listColor[0]
choose_palette = StringVar()
menu_file.add_command(label='Open file', command=lb_open_file)
menu_file.add_separator()
menu_file.add_command(label='Manage palettes', command=lb_palette_handler)
menu_file.add_separator()
menu_file.add_command(label='Exit', command=lb_quit)
menu_palette.add_radiobutton(label=listColor[0]['name'], value=0, variable=choose_palette, command=lb_change_palette)
menu_palette.add_radiobutton(label=listColor[1]['name'], value=1, variable=choose_palette, command=lb_change_palette)
menu_palette.add_radiobutton(label=listColor[2]['name'], value=2, variable=choose_palette, command=lb_change_palette)
menu_contact.add_command(label='Github', command=lambda: lb_contact(0))
menu_contact.add_command(label='Instagram', command=lambda: lb_contact(1))

url_txt = Label(screen, text='URL :', font=(20), fg='white', bg='#191919').place(x='10', y='10')
url_put = Entry(screen, textvariable=urler).place(x='70', y='15', width='250')
load = Button(screen, text='Load image', fg='white', bg='#191919', command=lambda: lb_preshot_img(have_file)).place(x='325', y='12.5')
res_txt = Label(screen, text='RES :', font=(20), fg='white', bg='#191919').place(x='10', y='40')
resolution_origin = Label(screen, textvariable=old_resolution, font=(20), fg='white', bg='#191919').place(x='70', y='40')
arrow = Label(screen, text='>', font=(20), fg='white', bg='#191919').place(x='170', y='40')
resolution_new = Entry(screen, textvariable=new_resolution).place(x='210', y='45', width='70')
name_txt = Label(screen, text='NAME :', font=(20), fg='white', bg='#191919').place(x='10', y='70')
name_put = Entry(screen, textvariable=name_file).place(x='90', y='75')

button = Button(screen, text='Submit', font=(10), fg='white', bg='#191919', command=lambda: lb_submit(have_url)).place(relx='0.5', rely='0.9', anchor=CENTER)

screen.config(menu=menu_bar)
screen.mainloop()

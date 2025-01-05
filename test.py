def lb_rgb_to_hexa(rgb):
    color = ''
    for i in range(3):
        print(hex(rgb[i])[2:])
        if rgb[i] == '0' or len(hex(rgb[i])[2:]) == 1:
            color += '0'
        color += hex(rgb[i])[2:]
    return '#' + color

print(lb_rgb_to_hexa((2, 116, 31)))
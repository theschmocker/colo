#!/usr/bin/python3
#from rgb import RGB
import rgb

class HSL(object):
    def __init__(self, h, s, l):
        if all(rgb.is_number(i) for i in (h, s, l)):
            self.h, self.s, self.l = (h, s, l)
        else:
            raise TypeError("Arguments must be of type int or float")

    def to_RGB(self):
        #C
        chroma = (1 - abs(2 * self.l - 1)) * self.s

        #H'
        hue = self.h / 60

        x = chroma * (1 - abs((hue % 2) - 1))
        intermediate_RGB = {}

        # There's gotta be a better way to do this...
        if 0 <= hue and hue <= 1:
            intermediate_RGB = {'r': chroma, 'g': x, 'b': 0}
        elif 1 <= hue and hue <= 2:
            intermediate_RGB = {'r': x, 'g': chroma, 'b': 0}
        elif 2 <= hue and hue <= 3:
            intermediate_RGB = {'r': 0, 'g': chroma, 'b': x}
        elif 3 <= hue and hue <= 4:
            intermediate_RGB = {'r': 0, 'g': x, 'b': chroma}
        elif 4 <= hue and hue <= 5:
            intermediate_RGB = {'r': x, 'g': 0, 'b': chroma}
        elif 5 <= hue and hue <= 6:
            intermediate_RGB = {'r': chroma, 'g': 0, 'b': x}
        else:
            print('Something went very, very wrong')
            print('value of "hue": ' + hue)
            exit(1)

        m = self.l - 0.5 * chroma

        R = 255 * (intermediate_RGB['r'] + m)
        G = 255 * (intermediate_RGB['g'] + m)
        B = 255 * (intermediate_RGB['b'] + m)

        return rgb.RGB(R, G, B)



    def __str__(self):
        h = round(self.h)
        s = round(self.s * 100)
        l = round(self.l * 100)
        return 'hsl({0}, {1}%, {2}%)'.format(h, s, l)

def from_string(string):
    if not string.startswith('hsl'):
        raise ValueError('You must provide an HSL string, such as "hsl(74, 64%, 59%)"')
    


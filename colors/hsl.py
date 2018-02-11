#!/usr/bin/python3

class HSL(object):
    def __init__(self, h, s, l):
        self.h, self.s, self.l = (h, s, l)
    def __str__(self):
        h = round(self.h)
        s = round(self.s * 100)
        l = round(self.l * 100)
        return 'hsl({0}, {1}%, {2}%)'.format(h, s, l)

#!/usr/bin/python3

base16 = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

def convertToDecimal(hex):
    digits = hex.lower()
    if len(digits) == 1:
        digits += digits
    digitSequence = reversed(list(digits))
    decimal = 0
    for index, value in enumerate(digitSequence):
        number = 0
        if value in base16:
            number = base16[value]
        else:
            try:
                number = int(value)
            except ValueError:
                print('Your hex value seems to have a value out of the range 0-f.')
        decimal += number * (16 ** index)
    return decimal

class RGB(object):
    def __init__(self, color="#000000"):
        if 'HSL' not in str(type(color)):
            #Deal with hex string
            if color[0] == '#':
                color = color[1:]
            if len(color) == 3:
                self.r = convertToDecimal(color[0])
                self.g = convertToDecimal(color[1])
                self.b = convertToDecimal(color[2])
            elif len(color) == 6:
                self.r = convertToDecimal(color[0:2])
                self.g = convertToDecimal(color[2:4])
                self.b = convertToDecimal(color[4:6])
            else:
                raise Exception('Malformed color.')
        #else:
            #Deal with HSL object

    def __str__(self):
        return 'rgb({0}, {1}, {2})'.format(self.r, self.g, self.b)

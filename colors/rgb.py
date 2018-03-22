#!/usr/bin/python3
import hsl

base16 = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

def convert_to_decimal(hex):
    digits = hex.lower()
    if len(digits) == 1:
        digits += digits
    digit_sequence = reversed(list(digits))
    decimal = 0
    for index, value in enumerate(digit_sequence):
        number = 0
        if value in base16:
            number = base16[value]
        else:
            try:
                number = int(value)
            except ValueError:
                raise ValueError('Your hex value seems to have a value out of the range 0-f.')
        decimal += number * (16 ** index)
    return decimal

# Only works for base ten numbers < 255. Should probably make this a bit more general purpose
# WARNING: Dirty hackery ahead...
# Returns a two digit hex value as a string
def convert_to_hex(decimal):
    sixteens = int(decimal) // 16
    ones = int(decimal) % 16
    if sixteens >= 10:
        sixteens = list(base16.keys())[list(base16.values()).index(sixteens)]
    if ones >= 10:
        ones = list(base16.keys())[list(base16.values()).index(ones)]
    return str(sixteens) + str(ones)
    
def is_number(number):
    return type(number) is int or type(number) is float

def calculate_luminance(min, max):
    return (min + max) / 2

def calculate_saturation(R, G, B):
    minimum = min(R, G, B)
    maximum = max(R, G, B)
    luminance = calculate_luminance(minimum, maximum)

    if luminance < 0.5:
        saturation = (maximum - minimum) / (maximum + minimum)
    elif luminance > 0.5:
        saturation = (maximum - minimum) / (2.0 - maximum - minimum)
    elif luminance == 0.5 and minimum != maximum:
        saturation = 1.0
    else:
        saturation = 0

    return saturation

def calculate_hue(R, G, B):
    minimum = min(R, G, B)
    maximum = max(R, G, B)

    if R == maximum:
        hue = (G - B) / (maximum - minimum)
    elif G == maximum:
        hue = 2.0 + ((B - R) / (maximum - minimum))
    elif B == maximum:
        hue = 4.0 + ((R - G) / (maximum - minimum))
    # Convert to degrees 
    hue *= 60

    if hue < 0:
        hue += 360

    return hue


def RGB_to_HSL(R, G, B):
    R /= 255.0
    G /= 255.0
    B /= 255.0
    minimum = min(R, G, B)
    maximum = max(R, G, B)
    if minimum != maximum:
        hue = calculate_hue(R, G, B)
        saturation = calculate_saturation(R, G, B) 
    else:
        hue = 0
        saturation = 0

    return hsl.HSL(hue, saturation, calculate_luminance(minimum, maximum))

class RGB(object):
    def __init__(self, r=None, g=None, b=None):
        if r is None or (is_number(r) and b is None):
            raise ValueError('RGB accepts these formats of arguments. RGB(hex_string), RGB(number_r, number_g, number_b')

        elif type(r) is hsl.HSL:
            raise ValueError('RGB(hsl_object) is not supported. Use HSL.to_RGB() instead')

        # Usage: RGB(255, 255, 255)
        elif None not in (r, g, b):
            if all(is_number(i) for i in (r, g, b)):
                self.r, self.g, self.b = (r, g, b)
            else:
                raise TypeError("Arguments must be of type int or float")

        # Usage: RGB('#bada55')
        elif type(r) is str: 
            color = r
            #Deal with hex string
            if color[0] == '#':
                color = color[1:]
            if len(color) == 3:
                self.r = convert_to_decimal(color[0])
                self.g = convert_to_decimal(color[1])
                self.b = convert_to_decimal(color[2])
            elif len(color) == 6:
                self.r = convert_to_decimal(color[0:2])
                self.g = convert_to_decimal(color[2:4])
                self.b = convert_to_decimal(color[4:6])
            else:
                raise ValueError('Malformed color.')

    def to_HSL(self):
        return RGB_to_HSL(self.r, self.g, self.b)

    def to_hex(self):
        return '#' + ''.join(convert_to_hex(num) for num in (self.r, self.g, self.b))

    def __str__(self):
        return 'rgb({0}, {1}, {2})'.format(round(self.r), round(self.g), round(self.b))

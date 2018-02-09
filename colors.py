#!/usr/bin/python3
import sys


def calculateLuminance(min, max):
    return (min + max) / 2

def calculateSaturation(R, G, B):
    minimum = min(R, G, B)
    maximum = max(R, G, B)
    luminance = calculateLuminance(minimum, maximum)

    if luminance < 0.5:
        saturation = (maximum - minimum) / (maximum + minimum)
    elif luminance > 0.5:
        saturation = (maximum - minimum) / (2.0 - maximum - minimum)
    elif luminance == 0.5 and minimum != maximum:
        saturation = 1.0
    else:
        saturation = 0

    return saturation



def calculateHue(R, G, B):
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

def RGBtoHSL(rgb):
    hsl = {}
    R = rgb['r'] / 255.0
    G = rgb['g'] / 255.0
    B = rgb['b'] / 255.0
    minimum = min(R, G, B)
    maximum = max(R, G, B)
    if minimum != maximum:
        hue = calculateHue(R, G, B)
        saturation = calculateSaturation(R, G, B) 
    else:
        hue = 0
        saturation = 0

    hsl['h'] = hue
    hsl['s'] = saturation
    hsl['l'] = calculateLuminance(minimum, maximum)

    return hsl

# Adapted from https://en.wikipedia.org/wiki/HSL_and_HSV#Converting_to_RGB
def HSLtoRGB(hsl):
    #C
    chroma = (1 - abs(2 * hsl['l'] - 1)) * hsl['s']

    #H'
    hue = hsl['h'] / 60

    x = chroma * (1 - abs((hue % 2) - 1))
    intermediateRGB = {}

    # There's gotta be a better way to do this...
    if 0 <= hue and hue <= 1:
        intermediateRGB = {'r': chroma, 'g': x, 'b': 0}
    elif 1 <= hue and hue <= 2:
        intermediateRGB = {'r': x, 'g': chroma, 'b': 0}
    elif 2 <= hue and hue <= 3:
        intermediateRGB = {'r': 0, 'g': chroma, 'b': x}
    elif 3 <= hue and hue <= 4:
        intermediateRGB = {'r': 0, 'g': x, 'b': chroma}
    elif 4 <= hue and hue <= 5:
        intermediateRGB = {'r': x, 'g': 0, 'b': chroma}
    elif 5 <= hue and hue <= 6:
        intermediateRGB = {'r': chroma, 'g': 0, 'b': x}
    else:
        print('Something went very, very wrong')
        print('value of "hue": ' + hue)
        exit(1)

    m = hsl['l'] - 0.5 * chroma
    
    rgb = {}

    rgb['r'] = 255 * (intermediateRGB['r'] + m)
    rgb['g'] = 255 * (intermediateRGB['g'] + m)
    rgb['b'] = 255 * (intermediateRGB['b'] + m)

    return rgb

try:
    hex_color = sys.argv[1]

except:
    # TODO: adapt this to accept other color formats 
    print('Please provide a hex color as an argument. If you did, and are seeing this message, try removing the "#".')
    exit()

if len(hex_color) != 3 and len(hex_color) != 6:
    print('Error: Malformed color.')
    exit()
rgb = hexToRGB(hex_color)

# TODO: Build a pretty printing system. In this format, this data is only useful for calculations
# TODO: Get rid of this nonsense. It's only for testing
print("Hex Color: #%s" % hex_color)
print("RGB representation: %s" % rgb)
print("HSL representation: %s" % RGBtoHSL(rgb))
print("RGB as converted from HSL: %s" % HSLtoRGB(RGBtoHSL(rgb)))


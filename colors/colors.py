#!/usr/bin/python3
import sys



# Adapted from https://en.wikipedia.org/wiki/HSL_and_HSV#Converting_to_RGB
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


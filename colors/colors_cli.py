from .rgb import RGB
from .hsl import HSL

def convert_to_all(hex):
    rgb = RGB(hex)
    hsl = rgb.to_HSL()

    output = f"""

Input:  #{hex}
To RGB: {rgb}
To HSL: {hsl}

    """

    return output

from functions import *


## Generate Complementary pallete
def complementary_pallete(colors):
    complementary = []
    for color in colors:
        # Remove the '#' symbol
        color = color.lstrip('#')
        # Convert hexadecimal colors to integers
        color_int = int(color, 16)
        comp_color = 0xFFFFFF ^ color_int
        result = "#%06X" % comp_color

        complementary.append(result)

    return complementary

comp_color = complementary_pallete(color)

print(color)
print(comp_color)
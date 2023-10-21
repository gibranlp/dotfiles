from colors import *

def hex_to_rgb(hex_color):
    # Remove the '#' if it exists in the input
    hex_color = hex_color.lstrip('#')
    # Convert the hex color to RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return r, g, b

def rgb_to_hex(rgb_color):
    # Convert RGB values to a hex color code
    hex_color = "#{:02X}{:02X}{:02X}".format(*rgb_color)
    return hex_color

def darken_color(hex_color, factor=0.5):
    # Convert hex color to RGB
    r, g, b = hex_to_rgb(hex_color)
    
    # Darken the color by reducing each RGB component
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    
    # Ensure values are within the valid RGB range (0-255)
    r = max(0, r)
    g = max(0, g)
    b = max(0, b)
    
    # Convert the darkened RGB color back to hex
    darkened_hex_color = rgb_to_hex((r, g, b))
    
    return darkened_hex_color

def lighten_color(hex_color, factor=1.5):
    # Convert hex color to RGB
    r, g, b = hex_to_rgb(hex_color)
    
    # Lighten the color by increasing each RGB component
    r = min(255, int(r * factor))
    g = min(255, int(g * factor))
    b = min(255, int(b * factor))
    
    # Convert the lightened RGB color back to hex
    lightened_hex_color = rgb_to_hex((r, g, b))
    
    return lightened_hex_color

def generate_palettes(hex_color_list):
    # Darken and lighten the colors in the input list
    darkened_colors = [darken_color(color) for color in hex_color_list]
    brighter_colors = [lighten_color(color) for color in hex_color_list]
    
    return darkened_colors, brighter_colors

try:
    # Generate darker and brighter palettes based on the input colors
    third_colors, secondary_colors = generate_palettes(color)
    
    print("Original colors:")
    for hex_color in color:
        print(hex_color)
    
    print("\nThird Palette (Darker Colors):")
    for darkened_color in third_colors:
        print(darkened_color)
    
    print("\nSecondary Palette (Brighter Colors):")
    for brighter_color in secondary_colors:
        print(brighter_color)
except ValueError:
    print("Invalid hex color format. Please use the format #RRGGBB.")



# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
## 
import json
import os

#Home Path
home = os.path.expanduser('~') # Path for use in folders

#Color Variables
## Import Colors from Pywal
with open(home + '/.cache/wal/colors.json') as wal_import:
  data = json.load(wal_import)
  wallpaper = data['wallpaper']
  colors = data['colors']
  val_colors = list(colors.values())
  def getList(val_colors):
    return [*val_colors]
    
  def init_colors():
    return [*val_colors]

color = init_colors()

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

def darken_color(hex_color, factor=0.3):
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

def lighten_color(hex_color, factor=1.2):
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
    
    return brighter_colors, darkened_colors

secondary_color, third_color = generate_palettes(color)

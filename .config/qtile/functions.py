# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence
#
#
import random
import socket
import subprocess
from os.path import expanduser
from pathlib import Path
import requests
from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import ScratchPad, DropDown, Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.popup.toolkit import (PopupRelativeLayout, PopupWidget)
from qtile_extras.widget.decorations import (BorderDecoration,PowerLineDecoration,RectDecoration)
from rofi import Rofi
from colors import  *

#### Variables ####
# Modifiers
mod = "mod4"
alt = "mod1"

## Import config
file = open(home + '/.config/qtile/variables', 'r')
variables=file.readlines()

## Get update if available
file = open(home + '/.config/qtile/update', 'r')
update_available=file.readlines()

## Read picom.conf for blur in the bar
file = open(home + '/.config/picom/picom.conf', 'r')
bar_blur=file.readlines()
current_blur = bar_blur[275].strip()

if current_blur == '"QTILE_INTERNAL:32c = 0"':
  new_blur = '"QTILE_INTERNAL:32c = 1"' + "\n"
  bar_blur[275] = new_blur
  blur_icon=''
else:
  new_blur = '"QTILE_INTERNAL:32c = 0"' + "\n"
  bar_blur[275] = new_blur
  blur_icon=''

## Get Terminal Fontsize
file = open(home + '/.config/alacritty/alacritty.toml', 'r')
term_size=file.readlines()
terminal_font_size = term_size[21].strip()

# SpectrumOS version
remote_version=update_available[0].strip()
version=variables[0].strip()

if version == remote_version:
  update_spectrumos= ' SpectrumOS is up to date!'
  
  update_available=0
else:
  update_spectrumos= f' Update Available {version} -> {remote_version}',
  update_available=1

## Fonts
main_font = str(variables[11].strip()) # Font in use for the entire system
awesome_font = "Font Awesome 6 Pro" # Font for the icons
font_size=int(variables[12].strip()) # Font Size
bar_size=30

# Terminal 
terminal = "alacritty"

# Format of the prompt
prompt = "$".format(os.environ["USER"], socket.gethostname()) 

# Wallpapers / Theming
wallpaper_dir= home + '/Pictures/Wallpapers/' # Wallpapers folders
light=str(variables[4].strip()) # Option for light themes

#Initialize Groups
groups = []
group_names = ["Escape","1","2","3","4","5","6","7","8","9"]
hide_unused_groups=bool(str(variables[8].strip()))

# Theme
current_theme=str(variables[1].strip())
themes_dir = home + str(variables[5].strip())
theme_dest = (home + "/.config/qtile/theme.py")
theme_file = themes_dir + "/" + current_theme
theme=['Spectrum', 'Miasma', 'Minimal', 'Monochrome',  'Monochrome2kends Options: Wal, Colorz, Colorthief, Haishoku
def_backend=str(variables[2].strip()) # Default Color Scheme for random wallpaper
backend=['wal', 'colorz', 'colorthief','haishoku']  

## Margins
layout_margin=10 # Layout margins
single_layout_margin=10 # Single window margin 
## Borders
layout_border_width=5 # Layout border width
single_border_width=5 # Single border width

# Bar Position
bar_position=str(variables[6].strip())

#Widgets
widget_width=200 #Width of widgets varies depending the resolution

# Get current screen resolution
resolution = os.popen('xdpyinfo | awk "/dimensions/{print $2}"').read()
xres = resolution[17:21]
yres = resolution[22:26]

# Set Bar and font sizes for different resolutions
if xres >= "3840" and yres >= "2160": #4k
  layout_margin=20
  single_layout_margin=15  
  layout_border_width=5
  single_border_width=5
  bar_size=30
  widget_width=450
  max_ratio=0.85
  ratio=0.65
  terminal_font_size=12
  if bar_position == "bottom":
    bar_margin=[0,15,10,15]
  else:
    bar_margin=[10,15,0,15]
  weather_x=0.78
  weather_y=0.90
  weather_width=0.075
  weather_height=0.09
elif xres == "1920" and yres == "1080": #FullHD
  layout_margin=10
  single_layout_margin=5  
  layout_border_width=4 
  single_border_width=4
  bar_size=25
  widget_width=150
  max_ratio=0.85
  ratio=0.65
  font_size=font_size-4
  terminal_font_size=9
  if bar_position == "bottom":
    bar_margin=[0,10,5,10]
  else:
    bar_margin=[5,10,0,10]
  weather_x=0.60
  weather_y=0.76
  weather_width=0.14
  weather_height=0.23
else: # 1366 x 768 Macbook air 11"
  layout_margin=2
  single_layout_margin=2  
  layout_border_width=2
  single_border_width=2
  font_size=font_size-7
  bar_size=20
  widget_width=100
  max_ratio=0.50
  ratio=0.50
  terminal_font_size=7
  bar_margin=[0,0,0,0]

# Set the right Terminal Font size
term_size[21] = "  size= " + str(terminal_font_size) + "\n"
with open(home + '/.config/alacritty/alacritty.toml', 'w') as file:
    file.writelines(term_size)

# Make font smaller for cetain groups icons
if int(variables[10]) in [7,8,9,10,11,12,13]:
   groups_font = font_size - 8
else:
   groups_font = font_size 

# Rofi Configuration files
rofi_right = Rofi(rofi_args=['-theme', '~/.config/rofi/right.rasi'])
rofi_network= Rofi(rofi_args=['-theme', '~/.config/rofi/network.rasi'])
rofi_left= Rofi(rofi_args=['-theme', '~/.config/rofi/left.rasi'])
rofi_session= Rofi(rofi_args=['-theme', '~/.config/rofi/session.rasi'])

### Weather
w_appkey = str(variables[3].strip()) # Get a key here https://home.openweathermap.org/users/sign_up 
w_cityid ="3995402" # "3514783" Veracruz, "3995402" Morelia, "3521342" Playa del Carmen https://openweathermap.org/city/

## Sticky Windows

sticky_windows=[]

## Move Window to current Group
@lazy.function
def toggle_sticky_windows(qtile, window=None):
    if window is None:
        window = qtile.current_screen.group.current_window
    if window in sticky_windows:
        sticky_windows.remove(window)
    else:
        sticky_windows.append(window)
    return window

#Hooks
@hook.subscribe.setgroup
def move_sticky_windows():
    for window in sticky_windows:
        window.togroup()
    return

@hook.subscribe.client_killed
def remove_sticky_windows(window):
    if window in sticky_windows:
        sticky_windows.remove(window)

@hook.subscribe.startup # This file gets executed everytime qtile restarts
def start():
  subprocess.call(home + '/.local/bin/alwaystart')
  subprocess.run(["openrgb", "-d", "0", "-c", "%s" %color[1].lstrip('#'), "-b", "50"])
      
@hook.subscribe.startup_once # Ths file gets executed once at the start1
def start_once():
  subprocess.call(home + '/.local/bin/autostart')

@hook.subscribe.client_new
def follow_window(client):
  for group in groups:
    match = next((m for m in group.matches if m.compare(client)), None)
    if match:
      targetgroup = qtile.groups_map[group.name]
      targetgroup.toscreen(toggle=False)
      break

@hook.subscribe.client_name_updated
def follow_window_name(client):
  for group in groups:
    match = next((m for m in group.matches if m.compare(client)), None)
    if match:
      targetgroup = qtile.groups_map[group.name]
      targetgroup.toscreen(toggle=False)
      break

##Specific Apps/Groups
def app_or_group(group, app):
  def f(qtile):
    if qtile.groups_map[group].windows:
       qtile.groups_map[group].toscreen(toggle=False)
       qtile.spawn(app)
    else:
      qtile.groups_map[group].cdtoscreen(toggle=False)
      qtile.spawn(app)
    return f

# Run i3-lock with Colors

def i3lock_colors(qtile):
  subprocess.run(['i3lock', 
    '--image=%s' % wallpaper,
    '--fill',          
    '--ring-color={}'.format(secondary_color[0]+"aa"),
    '--inside-color={}'.format(secondary_color[0]+"aa"),
    '--line-color={}'.format(color[2]),
    '--separator-color={}'.format(color[4]),
    '--time-color={}'.format(color[2]),           
    '--date-color={}'.format(color[4]),
    '--insidever-color={}'.format(secondary_color[0]+"aa"),
    '--ringver-color={}'.format(color[0]),
    '--verif-color={}'.format(color[5]),          
    '--verif-text=Validating',
    '--insidewrong-color={}'.format(secondary_color[0]+"aa"),
    '--ringwrong-color={}'.format(secondary_color[0]+"aa"),
    '--wrong-color={}'.format(secondary_color[0]+"aa"),
    '--wrong-text=Wrong!',
    '--keyhl-color={}'.format(color[1]),         
    '--bshl-color={}'.format(color[6]),            
    '--clock',
    '--indicator',       
    '--time-str=%H:%M:%S',
  ])

# Toggle Bar Blur
def toggle_bar_blur(qtile):
  with open(home + '/.config/picom/picom.conf', 'w') as file:
    file.writelines(bar_blur)
  
  qtile.reload_config()

# Transparent for bars and widgets
transparent="00000000"

# Set Random Wallpaper
def change_wallpaper(qtile):
  selection = random.choice(os.listdir(wallpaper_dir))
  selected_wallpaper = os.path.join(wallpaper_dir, selection)
  i=0
  while i<5:
    if selected_wallpaper != wallpaper:
      subprocess.run(["wpg", light, "-s", str(selected_wallpaper), "--backend", def_backend.lower()])
      subprocess.run(["cp", str(selected_wallpaper), "/usr/local/backgrounds/background.png"])
      subprocess.run(["cp", "-r", str(Path.home() / ".local/share/themes/FlatColor"), "/usr/local/themes/"])
      break
    else:
      selection = random.choice(os.listdir(wallpaper_dir))
      selected_wallpaper = os.path.join(wallpaper_dir, selection)
  
  qtile.reload_config()
  #subprocess.run(["notify-send","-a", " SpectrumOS", "Wallpaper Set to: ", "%s" %selection])

## Get network device in use
def get_net_dev():
  get_dev = "echo $(ip route get 8.8.8.8 | awk -- '{printf $5}')"
  ps = subprocess.Popen(get_dev,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0].decode('ascii').strip()
  return(output)

wifi = get_net_dev()

# Set Ethernet or Wifi icon according
if wifi.startswith('e'):
  wifi_icon=''
else:
  wifi_icon=''

## Get local IP Address
def get_private_ip():
  ip = socket.gethostbyname(socket.gethostname())
  return ip

private_ip = get_private_ip()

## Get Public IP Address
def get_public_ip(timeout=1):
    try:
        raw = requests.get('https://api.duckduckgo.com/?q=ip&format=json', timeout=timeout)
        raw.raise_for_status() 
        answer = raw.json()["Answer"].split()[4]
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return "0.0.0.0"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "0.0.0.0"
    else:
        return answer
        
public_ip = get_public_ip()


# Call Calendar Notification

def calendar_notification(qtile):{
  subprocess.call(home + '/.local/bin/calendar')
}

def calendar_notification_prev(qtile):{
  subprocess.call([home + '/.local/bin/calendar', 'prev'])
}

def calendar_notification_next(qtile):{
  subprocess.call([home + '/.local/bin/calendar', 'next'])
}

## Rofi Widgets

## Set default backend
def set_default_backend(qtile):
  options = backend
  index, key = rofi_session.select(' Backend -> ' + def_backend.capitalize() , options)
  if key == -1 or index == 4:
    rofi_left.close()
  else:
    subprocess.run(["wal", light.lower(), "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["wpg", light, "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %backend[index].lower()])
    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    variables[2]=backend[index] + "\n"
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " SpectrumOS", "Color Theme: ", " %s" %backend[index]])

# Display Shortcuts widget
def shortcuts(qtile):
  subprocess.run("cat ~/.shortcuts | rofi -theme '~/.config/rofi/shortcuts.rasi' -i -dmenu -p ' Shortcuts:'",shell=True)

# Display Emojis
def emojis(qtile):
  subprocess.run("rofi -modi emoji -show emoji -theme '~/.config/rofi/emojis.rasi' -emoji-format {emoji}",shell=True)

# NightLight widget
def nightLight_widget(qtile):
  options = [' Night Time(3500k)', ' Neutral (6500k)', ' Cool (7500k)']
  index, key = rofi_session.select('  Night Light', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      os.system('redshift -O 3500k -r -P')
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Night Time"])
    elif index == 1:
      os.system('redshift -x')
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Neutral"])
    else:
      os.system('redshift -O 7500k -r -P')
      subprocess.run(["notify-send","-a", " SpectrumOS", "Temperature Set to Cool"])

# Farge Widget
def fargewidget(qtile):
  options = [' Hex',' RGB']
  index, key = rofi_session.select('  Color Picker', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("farge --notify --expire-time 20000",shell=True)
    else:
      subprocess.run("farge --notify --rgb --expire-time 20000",shell=True)

# Draw Widget
def draw_widget(qtile):
  options = [' Draw', ' Exit']
  index, key = rofi_session.select('  Screen Draw', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("gromit-mpx -a &",shell=True)
      subprocess.run(["notify-send", "-a", " SpectrumOS", "You can Draw Now"])
    else:
      subprocess.run("gromit-mpx -q",shell=True)

# Logout widget
def session_widget(qtile):
  options = ['','', '','']
  index, key = rofi_session.select('  Session', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      qtile.function(i3lock_colors)
    elif index == 1:
      qtile.shutdown()
    elif index == 2:
      os.system('systemctl reboot')
    else:
      os.system('systemctl poweroff')

# Network Widget
def network_widget(qtile):
  options = [' Wlan Manager','  Bandwith Monitor (CLI)', ' Network Manager (CLI)']
  index, key = rofi_network.select(" " + private_ip + " -" + "  " + public_ip, options)
  if key == -1:
    rofi_network.close()
  else:
    if index == 0:
      qtile.spawn(home + '/.local/bin/wifi2')
    elif index==1:
      qtile.spawn("alacritty -e bash -c '. ~/.zshrc; bmon'")
    else:
      qtile.spawn("alacritty -e bash -c '. ~/.zshrc; nmtui'")

## Show / Hide all Groups
def show_groups(qtile):
  if hide_unused_groups == True:
    variables[8]=" " + "\n"
    variables[9]="" + "\n"
  else:
    variables[8]="True" + "\n"
    variables[9]="" + "\n"
      
  with open(home + '/.config/qtile/variables', 'w') as file:
    file.writelines(variables)
  qtile.reload_config()
   
## groups_icon_select
def group_icon(qtile):
  options = [
    '         ', 
    '零 一 二 三 四 五 六 七 八 九', 
    '         ',
    '         ',
    '         ',
    '0 1 2 3 4 5 6 7 8 9',
    ': ( ) { : | : & } ;',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    'TERM DEV WWW SYS DOC VIRT MSG MUS VID GFX'
    ]
  index, key = rofi_session.select(' Group Icons ', options)
  if key == -1:
    rofi_left.close()
  else:
    variables[10]=str(index) + "\n"
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()

## Select Dark or Light Theming
def dark_white(qtile):
  options = [' Dark', ' Light']
  index, key = rofi_session.select(' Theme -> ' + str(variables[7].strip()), options)
  if key == -1 or index == 2:
    rofi_left.close()
  else:
    if index == 0:
      variables[4]="-c" + "\n"
      variables[7]="Dark" + "\n"
      variables[5]="/.config/qtile/themes/dark" + "\n"
      subprocess.run(['cp', home + '/.config/qtile/themes/dark/' + current_theme + ".py", home + '/.config/qtile/theme.py'])
      subprocess.run(["wal", "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
      subprocess.run(["wpg", "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
    else:
      variables[4]="-L" + "\n"
      variables[7]="Light" + "\n"
      variables[5]="/.config/qtile/themes/light" + "\n"
      subprocess.run(['cp', home + '/.config/qtile/themes/light/' + current_theme + ".py", home + '/.config/qtile/theme.py'])
      subprocess.run(["wal", "-l", "-i", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])
      subprocess.run(["wpg", "-L", "-A", "-s", "/usr/local/backgrounds/background.png", "--backend", "%s" %def_backend])

    subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " SpectrumOS", "Theme changed to: ", "%s" %options[index]])


## Select Bar Position Top or Bottom
def bar_pos(qtile):
  options = ['Top', 'Bottom', 'Toggle Bar']
  index, key = rofi_session.select(' Bar -> ' + bar_position , options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      variables[6]="top" + "\n"
      subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
      with open(home + '/.config/qtile/variables', 'w') as file:
        file.writelines(variables)
      qtile.reload_config()
    elif index == 1:
      variables[6]="bottom" + "\n"
      subprocess.run(["cp", "-r", home + "/.local/share/themes/FlatColor",  "/usr/local/themes/"])
      with open(home + '/.config/qtile/variables', 'w') as file:
        file.writelines(variables)
      qtile.reload_config()
    else:
      qtile.hide_show_bar()

# Change Theme widget
def change_theme(qtile):
  options = theme
  index, key = rofi_session.select('  Theme -> ' + current_theme , options)
  if key == -1:
    rofi_left.close()
    subprocess.run(["notify-send","-a", " SpectrumOS", "No Theme Selected!"])
  else:
    subprocess.run('rm -rf ~/.config/qtile/theme.py', shell=True)
    variables[1]=theme[index] + "\n"
    new_theme=theme[index] + ".py"
    subprocess.run(['cp', themes_dir + "/" + new_theme, home + '/.config/qtile/theme.py'])
    with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
    qtile.reload_config()
    subprocess.run(["notify-send","-a", " SpectrumOS", " Theme: ", "%s" %theme[index]])
    
# Set random colors to theme
def random_colors(qtile):
  subprocess.run(["wpg", light, "-z", "%s" % wallpaper])
  subprocess.run(["wpg", "-s", "%s" % wallpaper])
  subprocess.run(["rm", "-rf", "%s" %wallpaper + "_wal_sample.png"])
  qtile.reload_config()

# Screenshot widget
def screenshot(qtile):
  options = [' Area', ' Screen', ' Window',  ' 5s Screen']
  index, key = rofi_session.select('  Screenshot', options)
  if key == -1:
    rofi_left.close()
  else:
    if index ==0:
      subprocess.run("flameshot gui --path ~/Pictures/area_screenshot.png --delay 400",shell=True)
    elif index==1:
      subprocess.run("flameshot full --path ~/Pictures/Screenshot.png --delay 500",shell=True)
    elif index==2:
      subprocess.run("scrot -u 'window_screenshot.png' -e 'mv $f ~/Pictures/ #; feh -F ~/Pictures/$f' && notify-send -a 'flameshot' 'Window Picture Taken!'",shell=True)
    else:
      subprocess.run("flameshot full --path ~/Pictures/Screenshot.png --delay 5000",shell=True)

# Popup Widgets
def show_keyboard_layout(qtile):
    controls = [
        PopupWidget(
            widget=widget.KeyboardLayout(
              configured_keyboards=['us intl', 'latam'],
              foreground=color[1],
            ),
            width=1,
            height=1,
        )
    ]

    layout = PopupRelativeLayout(
        qtile,
        pos_x=0.8,
        pos_y=0.8,
        width=100,
        height=50,
        controls=controls,
        background=color[0],
        initial_focus=None,
        close_on_click=False,
        hide_on_mouse_leave=True,
        keyboard_navigation=True,
    )
    layout.show(centered=True)

## Support SpectrumOS
def support_spectrumos(qtile):
  options = [' Become a Patreon', ' Buy me a Coffee']
  index, key = rofi_session.select(' Support SpectrumOS', options)
  if key == -1 or index == 2:
    rofi_left.close()
  else:
    if index == 0:
      subprocess.run(["xdg-open", "https://www.patreon.com/user?u=48005915"])
    else:
      subprocess.run(["xdg-open", "https://www.buymeacoffee.com/gibranlp"])
    
    subprocess.run(["notify-send","-a", " SpectrumOS", "Thanks for supporting SpectrumOS"])

## Update SpectrumOS
### Pacman
def pacman_packages(qtile):
    packets = [
        ''
    ]
    for packet in packets:
        subprocess.run(["notify-send","-a", " SpectrumOS", "Installing -> %s" % packet])
        subprocess.run(["sudo", "pacman", "-Syu", packet, "--noconfirm", "--needed"])

## Update SpectrumOS


# Logout widget
def turntable(qtile):
  options = [' On', ' Off']
  index, key = rofi_session.select(' Listen Turntable', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 0:
      os.system('pactl load-module module-loopback source=48')
    else:
      os.system('pactl unload-module module-loopback')

### AUR
def aur_packages(qtile):
    packets = [
      'sndio'
    ]
    
    for packet in packets:
        subprocess.run([f"notify-send","-a", " SpectrumOS", "Installing -> %s" % packet])
        subprocess.run(["paru", "-Syu", packet, "--noconfirm", "--needed"])

## Update SpectrumOS verssion
def update_ver(qtile):
  variables[0] = remote_version + "\n"
  with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
  qtile.reload_config()
  subprocess.run(["notify-send","-a", " SpectrumOS", "Updated to the version", "%s" % remote_version])


# Control Panel Widget
def control_panel(qtile):
  options = [
    ' Wallpaper Options',#0
    '     Set Random Wallpaper (⎇ + R)',
    '     Select Wallpaper (❖ +  + E)',
    ' Theme Options',#3
    '     Set Color Scheme (⎇ +  + W)',
    '     Dark/Light Theme (❖ + D)',
    ' Bar Options',#6
    '     Bar Position (❖ +  + W)',
    '     Change Bar Theme (⎇ + W)',
    '    %s Toggle Bar Blur' %blur_icon,
    '    %s Toggle Groups' %str(variables[9].strip()),
    '     Change Groups Icons',
    ' Tools',#12
    '     Find / Open Files (❖ + F)',
    '     Todo List (⎇ + L)',
    '     Notes (❖ + N)',
    '     Apps as Sudo (⎇ +  + )',
    '     Calculator (❖ + C)',
    '     Network Manager (❖ + B)',
    '     Screenshot (prtnsc)',
    '     Monitor Temperature (❖ +  + O)',
    '     Monitor Layout (❖ +  + X)',
    '     Bluetooth Manager (❖ + T)',
    '     Screen Recorder ( +  + R)',
    ' Miscelaneous',#24
    '     Screen Draw (❖ +  + P)',
    '     Pick Color (❖ + P)',
    '     View Shortcuts (❖ + S)',
    '     Emojis ( +  + )',
    '     System Cleaner',
    ' Session Menu (❖ + X)',
    ' Support SpectrumOS',
    '%s' %update_spectrumos
    
    ]
    
  index, key = rofi_left.select('  Control Panel', options)
  if key == -1:
    rofi_left.close()
  else:
    if index == 1:
      qtile.function(change_wallpaper)
    elif index == 2:
      qtile.spawn(home + '/.local/bin/selectwal')
    elif index == 4:
      qtile.function(set_default_backend)
    elif index == 5:
      qtile.function(dark_white)
    elif index == 7:
      qtile.function(bar_pos)
    elif index == 8:
      qtile.function(change_theme)
    elif index == 9:
      qtile.function(toggle_bar_blur) 
    elif index == 10:
      qtile.function(show_groups)
    elif index == 11:
      qtile.function(group_icon)
    elif index == 13:
      subprocess.run(home + '/.local/bin/opener')
    elif index == 14:
      qtile.spawn('rofi -modi TODO:~/.local/bin/todo -show TODO -theme ~/.config/rofi/left.rasi')
    elif index == 15:
      subprocess.Popen(home + '/.local/bin/notesfi', shell=True)
    elif index == 16:
      qtile.spawn('sudo rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')
    elif index == 17:
      subprocess.run(home + '/.local/bin/calculator')
    elif index == 18:
      qtile.function(network_widget)
    elif index == 19:
      qtile.function(screenshot)
    elif index == 20:
      qtile.function(nightLight_widget)
    elif index == 21:
      subprocess.run(home + '/.local/bin/change_display')
    elif index == 22:
      subprocess.run(home + '/.local/bin/bluet')
    elif index == 24:
      subprocess.run(home + '/.local/bin/recorder')
    elif index == 25:
      qtile.function(draw_widget)
    elif index == 26:
      qtile.function(fargewidget)
    elif index == 27:
      qtile.function(shortcuts)
    elif index == 28:
      qtile.function(emojis)
    elif index == 29:
      qtile.spawn(home + '/.local/bin/cleansys')
    elif index == 30:
      qtile.function(session_widget)
    elif index == 31:
      qtile.function(support_spectrumos)
    elif index == 32:
      if update_available == 1:
        subprocess.run(home + '/.local/bin/updater') 
        qtile.function(pacman_packages)
        qtile.function(aur_packages)
        qtile.function(update_ver)
      else:
        subprocess.run(["notify-send","-a", " SpectrumOS", "You are on the latest version!"])
        


 
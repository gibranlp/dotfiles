from theme import *
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
rofi_launcher = 'rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"'

keys = [
    # Qtile System Actions
    Key([mod], "t", lazy.layout.spawn_split(terminal, "x")),
    Key([mod, "shift"], "t", lazy.layout.spawn_split(terminal, "y")),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod, "shift"], "r",lazy.restart()),
    Key([mod, "shift"], "q",lazy.shutdown()),
    Key([mod], "q",lazy.window.kill()), # Close Window
    Key([mod], "r", lazy.spawncmd()), # Launch Prompt
    Key([mod], "y", toggle_sticky_windows()),

    # SpectrumOS
    Key([mod], "Return", lazy.layout.spawn_split(rofi_launcher, "x")), # Open Rofi launcher on X split
    Key([mod, "shift"], "Return", lazy.layout.spawn_split(rofi_launcher, "y")), # Open Rofi launcher on Y split

    Key([mod], "z",lazy.function(change_wallpaper)), # Set random wallpaper

    # Rofi Widgets
    Key([mod],"b",lazy.function(network_widget)), # Network Settings
    Key([mod],"c",lazy.spawn(home + '/.local/bin/calculator')), # Calculator Widget
    Key([mod],"f",lazy.function(dark_white)), # Select Dark or Light Theme
    Key([mod, "shift"], "e",lazy.spawn(home + '/.local/bin/selectwal')), # Select Wallpaper
    Key([mod],"f",lazy.spawn(home + '/.local/bin/opener')),# Find Files

     Key([mod], "n", lazy.spawn(home + '/.local/bin/notesfi')), # Notes Widget


    Key([alt],"l",lazy.spawn('rofi -modi TODO:~/.local/bin/todo -show TODO -theme ~/.config/rofi/left.rasi')),# Todo Manager
    Key(["control", "shift"], "Return", lazy.function(emojis)), # Open Rofi Emojis
    
    Key([mod, "Shift"],"z",lazy.function(shortcuts)), # Shortcuts widget
        
    Key([mod, "shift"],"w",lazy.function(bar_pos)), # Set bar position
    Key([mod, "shift"],"o",lazy.function(nightLight_widget)), # Set night light
    Key([mod],"p",lazy.function(fargewidget)), # Color Picker Widget
    Key(["control", "shift"], "r", lazy.spawn(home + '/.local/bin/recorder')), # Recorder Widget
    Key([mod, "shift"],"p",lazy.function(draw_widget)), # Desktop draw widget
    Key([alt], "Return", lazy.function(control_panel)), # Search for files and folders
    Key([mod], "m", lazy.spawn(home + '/.local/bin/bluet')), # Bluetooth widget
    Key([mod],"x",lazy.function(session_widget)), # Log out
    
    Key([alt, "shift"],"w",lazy.function(set_default_backend)), # Set Default Color Scheme
    Key([alt],"w",lazy.function(change_theme)), # Change Theme
    Key([mod, "shift"],"x",lazy.spawn(home + '/.local/bin/change_display')),# Monitor modes Widget
    
    #Sudo
    Key([alt, "shift"], "Return", lazy.spawn('sudo rofi -show drun -show-icons -theme "~/.config/rofi/launcher.rasi"')), # Open Rofi launcher as Sudo

    # Toggle Sticky Windows
    # Apps
    Key([mod],"e",lazy.spawn('thunar')),# Thunar

    # Layout Focus
    Key([mod], "w", 
        lazy.layout.up()
    ),
    Key([mod], "a", 
        lazy.layout.left()
    ),
    Key([mod], "s", 
        lazy.layout.down()
    ),
    Key([mod], "d", 
        lazy.layout.right()
    ),

    # Layout Resize
    Key([mod, "shift"], "w", 
        lazy.layout.resize("up", 30)
    ),
    Key([mod, "shift"], "a", 
        lazy.layout.resize("left", 30)
    ),
    Key([mod, "shift"], "s", 
        lazy.layout.resize("down", 30)
    ),
    Key([mod, "shift"], "d", 
        lazy.layout.resize("right", 30)
    ),

    # Layout swap
    Key([alt], "w", 
        lazy.layout.swap("up")
    ),
    Key([alt], "a", 
        lazy.layout.swap("left")
    ),
    Key([alt], "s", 
        lazy.layout.swap("down")
    ),
    Key([alt], "d", 
        lazy.layout.swap("right")
    ),

    # Layout Push
    Key([alt, "shift"], "w", 
        lazy.layout.push_in("up")
    ),
    Key([alt, "shift"], "a", 
        lazy.layout.push_in("left")
    ),
    Key([alt, "shift"], "s", 
        lazy.layout.push_in("down")
    ),
    Key([alt, "shift"], "d", 
        lazy.layout.push_in("right")
    ),

    # Layout merge tabs
    Key([mod], "Tab", 
        lazy.layout.next_tab()
    ),
    Key([mod, "shift"], "Tab", 
        lazy.layout.merge_tabs("previous")
    ),
    
    # Pull out to tab
    Key([alt], "Tab",
        lazy.layout.pull_out_to_tab(),
    ),
    
    Key([alt, "shift"], "Tab", 
        lazy.layout.shuffle_down(),
        lazy.layout.swap_right()
        ), # Swap Right Up
    
    Key([mod], 'period', lazy.next_screen()), # Send Cursor to next screen

    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    Key([mod], "i", 
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        ),
    
    Key([mod, "shift"], "i", lazy.layout.grow_main()),
    Key([mod], "m", 
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        ),
    
    Key([mod, "shift"], "m", lazy.layout.shrink_main()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    Key(["control", alt], "Return", lazy.layout.toggle_split()), # Toggle Split

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("sudo xbacklight -inc 5")), # Aument Brightness
    Key(["control", alt], "p", lazy.spawn("sudo xbacklight -inc 5")), # Aument Brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("sudo xbacklight -dec 5")), # Lower Brightness
    Key(["control", alt], "o", lazy.spawn("sudo xbacklight -dec 5")),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")), # Mute
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 2%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 2%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)), # Raise Volume

    # Media Control
    Key([], "XF86AudioPlay", lazy.spawn("playerctl --player=%any play-pause")), # Play Pause
    Key([], "XF86AudioNext", lazy.spawn("playerctl --player=%any next")), # Next song
    Key([], "XF86AudioPrev", lazy.spawn("playerctl --player=%any previous")), # Previous Song

    # Window hotkeys
    Key([alt], "g", lazy.window.toggle_fullscreen()), # Toggle Current window ;n
    Key([alt, "shift"], "f", lazy.window.toggle_floating()), # Toggle current window floating
    Key([mod], "space", lazy.next_layout()), # Cycle layouts

    # Keyboard
    Key([alt], "space", lazy.widget["keyboardlayout"].next_keyboard()), # Change Keyboard Layout

    # Screenshots
    Key([], "Print", lazy.function(screenshot)),

    # Lock Screen
    Key(["control", alt],"l",lazy.function(i3lock_colors)), # Run i3lock 

    # Dunst Shortuts
    Key(["control"], "space",  lazy.spawn("dunstctl close")), # Clear Last Notification
    Key(["control", "shift"], "space",  lazy.spawn("dunstctl close-all")), # Clear All Notifications
    Key(["control", "shift"], "n",  lazy.spawn("dunstctl  history-pop")), # Show Notificaction history

    # Kill window            
    Key([alt], "Escape", lazy.spawn('xkill')), # Click window to close

    # Scratchpads
    Key(["shift"], 'F12', lazy.group['scratchpad'].dropdown_toggle("music")),
    Key(["control","shift"], 'F12', lazy.group['scratchpad'].dropdown_toggle("lyrics")),
    Key([alt], 'F12', lazy.group['scratchpad'].dropdown_toggle("htop")),
    Key([alt], 'F11', lazy.group['scratchpad'].dropdown_toggle("weather")),

    # Show Keyboard Layouts
    Key([mod],"g",lazy.function(show_keyboard_layout)), # Run i3lock 

]

#https://www.patreon.com/rss/creepyenespanol?auth=w79EFzfpTCwuvNbZ0LSsSlRuh4M1IEwJ
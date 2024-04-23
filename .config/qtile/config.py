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
from keys import *

## Groups

#### Groups Labels
if int(variables[10]) == 0:
   group_labels=["","","","","","","","","",""] # SpectrumOS
elif int(variables[10]) == 1:
   group_labels=["零","一","二","三","四","五","六","七","八","九"] # Kanji Numbers
elif int(variables[10]) == 2:
   group_labels=["","","","","","","","","",""] # Custom
elif int(variables[10]) == 3:
   group_labels=["","","","","","","","","",""] # Star Wars
elif int(variables[10]) == 4:
   group_labels=["","","","","","","","","",""] # Chess
elif int(variables[10]) == 5:
   group_labels=["0","1","2","3","4","5","6","7","8","9"] # Numbers:
elif int(variables[10]) == 6:
   group_labels=[":","(",")","{",":","|",":","&","}",";"] # Fork Bomb
elif int(variables[10]) == 7:
   group_labels=["","","","","","","","","",""] # Circles
elif int(variables[10]) == 8:
   group_labels=["","","","","","","","","",""] # Squares
elif int(variables[10]) == 9:
   group_labels=["","","","","","","","","",""] # Triangles
elif int(variables[10]) == 10:
   group_labels=["","","","","","","","","",""] # Hexagons
elif int(variables[10]) == 11:
   group_labels=["","","","","","","","","",""] # Rectangles 
elif int(variables[10]) == 12:
   group_labels=["","","","","","","","","",""] # Square Ring
elif int(variables[10]) == 13:
   group_labels=["TERM","DEV","WWW","SYS","DOC","VIRT","MSG","MUS","VID","GFX"]

group_layouts=["monadtall", "monadtall", "monadtall", "spiral","monadtall", "monadtall", "monadtall","monadwide", "monadtall", "monadtall"]
for i in range(len(group_names)):
  groups.append(
    Group(
      name=group_names[i],
      layout=group_layouts[i].lower(),
      label=group_labels[i],
  ))
for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
    keys.append(Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)))

# Scratchpads

groups.append(ScratchPad("scratchpad", [
   DropDown("lyrics", "alacritty -e bash -c '. ~/.zshrc; lyrics'",
      x=0.75, y=0.05, width=0.20, height=0.9, opacity=0.9,
      on_focus_lost_hide=False),

   DropDown("music", "alacritty -e bash -c '. ~/.zshrc; ncspot'",
      x=0.05, y=0.0, width=0.9, height=0.7, opacity=0.9,
      on_focus_lost_hide=False),
               
   DropDown("htop", "alacritty -e bash -c '. ~/.zshrc; htop'",
      x=0.05, y=0.0, width=0.9, height=0.7, opacity=0.9,
      on_focus_lost_hide=False),            
               
                      ]),
          )

## Layouts
def init_layout_theme():
  return {"font":main_font,
    "fontsize":font_size,
    "margin":layout_margin,
    "border_on_single":False,
    "border_width":layout_border_width,
    "border_normal":color[0],
    "border_focus":color[2],
    "single_margin":single_layout_margin,
    "single_border_width":single_border_width,
    "change_ratio":0.01,
    "new_client_position":'bottom',
    }

layout_theme = init_layout_theme()

def init_layouts():
  return [
   layout.MonadTall(
     max_ratio=max_ratio,
     ratio=ratio,
     **layout_theme),
   layout.MonadWide(
     max_ratio=0.90,
     ratio=0.90,
     **layout_theme),
   layout.Spiral(
     ratio=0.5,
     ratio_increment=0.02,
     main_pane="left",
     clockwise=True,
     **layout_theme),
   layout.Spiral(
     ratio=0.5,
     ratio_increment=0.02,
     main_pane="top",
     clockwise=False,
     **layout_theme),
   layout.MonadWide(
     max_ratio=0.85,
     ratio=0.50,
     **layout_theme),
 ]
layouts = init_layouts()

floating_layout = layout.Floating(
   border_width=layout_border_width,
    border_normal=color[0],
    border_focus=color[2],
)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = 'floating_only'
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'focus'
reconfigure_screens = True
floats_kept_above = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
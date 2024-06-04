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
labels = {
    0: ["","","","","","","","","",""], # SpectrumOS
    1: ["零","一","二","三","四","五","六","七","八","九"], # Kanji Numbers
    2: ["","","","","","","","","",""], # Custom
    3: ["","","","","","","","","",""], # Star Wars
    4: ["","","","","","","","","",""], # Chess
    5: ["0","1","2","3","4","5","6","7","8","9"], # Numbers
    6: [":","(",")","{",":","|",":","&","}",";"], # Fork Bomb
    7: ["","","","","","","","","",""], # Circles
    8: ["","","","","","","","","",""], # Squares
    9: ["","","","","","","","","",""], # Triangles
    10: ["","","","","","","","","",""], # Hexagons
    11: ["","","","","","","","","",""], # Rectangles
    12: ["","","","","","","","","",""], # Square Ring
    13: ["TERM","DEV","WWW","SYS","DOC","VIRT","MSG","MUS","VID","GFX"] # Custom Labels
}

selected_label = int(variables[10])
group_labels = labels.get(selected_label, [])


group_layouts=["bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai", "bonsai"]
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
  return {
    "font":main_font,
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
   Bonsai(
      **{
         "window.border_size": layout_border_width,
         "window.margin":layout_margin,
         "window.border_color": color[0],
         "window.active.border_color": color[1],
         "window.default_add_mode": "match_previous",
         "auto_cwd_for_terminals": False,
         "tab_bar.height": 10,
         "tab_bar.bg_color": color[0],
         "tab_bar.tab.padding": 0,
         "tab_bar.tab.bg_color": color[3],
         "tab_bar.tab.fg_color": color[3],
         "tab_bar.tab.font_family": main_font,
         "tab_bar.tab.font_size": font_size,
         "tab_bar.tab.active.bg_color": color[1],
         "tab_bar.tab.active.fg_color": color[1],
         "tab_bar.margin": [2,5,0,5],
      }),
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
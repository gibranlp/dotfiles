# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
from functions import *
widget_defaults = dict(
    font=main_font,
    fontsize=font_size,
    padding=4,
)
# Theme

## Screens

def init_widgets_list():
    widgets_list = [
        widget.TextBox(
          foreground=color[0],
          text="",
          fontsize=font_size ,
          mouse_callbacks={'Button1': lambda: qtile.function(session_widget)},
          background=color[7]+"22",
        ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        widget.GroupBox(
          fontsize=groups_font,
          font=awesome_font,
          disable_drag=True,
          hide_unused=hide_unused_groups,
          borderwidth=0,
          active=color[5], #Program opened in that group
          inactive=color[8], # Empty Group
          rounded=False,
          highlight_method="text",
          this_current_screen_border=secondary_color[2],
          center_aligned = True,
          other_curren_screen_border=secondary_color[2],
          block_highlight_text_color=secondary_color[2],    
          urgent_border="fc0000",
          decorations=[RectDecoration(colour=color[0], radius=9, padding_y=1, filled=True)],
          background=color[7]+"22",
        ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        widget.Prompt(
          prompt=prompt,
          fontsize=font_size ,
          foreground=color[0],
          cursor_color=color[0],
          visual_bell_color=[0],
          visual_bell_time=0.2,
          background=color[7]+"22",
        ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        widget.Mpris2(
          background=color[7]+"22",
          mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
          objname=None,
          fontsize=font_size ,
          foreground=color[0],
          width=widget_width,
          format='{xesam:artist}  {xesam:title}',
          stopped_text="Stop",
          paused_text='  ',
          scroll=True,
          scroll_repeat=True,
          scroll_delay=0.1,
        ),
        widget.Spacer(
          background=color[7]+"22",
        ),
        widget.TextBox(
          foreground=color[2],
          text="",
          fontsize=font_size-2,
          mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
          decorations=[RectDecoration(colour=color[0], radius=[9,0,0,9], padding_y=1, filled=True)],
          background=color[7]+"22",
        ),
        widget.Clock(
          foreground=secondary_color[7],
          fontsize=font_size -2,
          format="%H:%M",
          update_interval=1,
          mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
          decorations=[RectDecoration(colour=color[0], radius=[0,9,9,0], padding_y=1, filled=True)],
          background=color[7]+"22",              
        ),
        widget.Spacer(
          length=bar.STRETCH,
          background=color[7]+"22",
        ),
        widget.TextBox(
          decorations=[RectDecoration(colour=color[0], radius=[9,0,0,9], padding_y=1, filled=True)],
          background=color[7]+"22",
          foreground=color[3],
          text=" ",
          fontsize=font_size-2,
        ),  
        widget.CPU(
          decorations=[RectDecoration(colour=color[0], radius=[0,9,9,0], padding_y=1, filled=True)],
          background=color[7]+"22",
          foreground=secondary_color[7],
          format='{load_percent}% ',
          fontsize=font_size ,
        ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        widget.TextBox(
          decorations=[RectDecoration(colour=color[0], radius=[9,0,0,9], padding_y=1, filled=True)],
          background=color[7]+"22",
          fontsize=font_size-2,
          foreground=color[4],
          text=" ",
        ),
        widget.Memory(
          decorations=[RectDecoration(colour=color[0], radius=[0,9,9,0], padding_y=1, filled=True)],
          background=color[7]+"22",
          foreground=secondary_color[7],
          format='{MemUsed:.0f}{mm} ',
          measure_mem='M',
          fontsize=font_size ,
        ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        widget.TextBox(
          decorations=[RectDecoration(colour=color[0], radius=[9,0,0,9], padding_y=1, filled=True)],
          background=color[7]+"22",
          text="",
          foreground=color[5],
          mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)}, 
          fontsize=font_size-2
        ),
        widget.ALSAWidget(
          background=color[0],
          device='Master',
          bar_colour_high=color[5],
          bar_colour_loud=color[5],
          bar_colour_normal=color[5],
          bar_colour_mute=color[5],
          hide_interval=5,
          update_interval=0.1,
          bar_width=80,
          mode='bar',
          text_format=' ',
        ),
        widget.TextBox(
          decorations=[RectDecoration(colour=color[0], radius=[0,9,9,0], padding_y=1, filled=True)],
          background=color[7]+"22",
          text=" ",
          foreground=color[5],
          mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
          fontsize=font_size-2
        ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        ## Network
        widget.WidgetBox(
          decorations=[RectDecoration(colour=color[0], radius=[9,0,0,9], padding_y=1, filled=True)],
          background=color[7]+"22",
          fontsize=font_size-2,
          text_closed=' ' + wifi_icon + ' ',
          text_open='  ',
          foreground=color[3],
          widgets=[
            widget.TextBox(
              background=color[0],
              fontsize=font_size-2,
              text='  ',
              foreground=color[4],
              mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
            widget.TextBox(
              background=color[0],
              fontsize=font_size ,
              text=private_ip,
              foreground=secondary_color[7],
              mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
            widget.TextBox(
              background=color[0],
              fontsize=font_size-2,
              text='  ',
              foreground=color[4],
              mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
            widget.TextBox(
              background=color[0],
              fontsize=font_size ,
              text=public_ip,
              foreground=secondary_color[7],
              mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
            widget.TextBox(
              background=color[0],
              fontsize=font_size-2,
              text=wifi_icon,
              foreground=color[4],
              mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
          ]
        ),
        widget.Wlan(
          decorations=[RectDecoration(use_widget_background=True, radius=0, padding_y=1, filled=True)],
          background=color[0],
          fontsize=font_size ,
          interface=wifi,
          format='{essid}',
          disconnected_message='',
          foreground=color[3],
          width=widget_width,
          scroll=True,
          scroll_repeat=True,
          scroll_interval=0.1,
          scroll_step=1,
          update_interval=1,
          mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}),
        widget.Wlan(
          background=color[0],
          fontsize=font_size,
          interface=wifi,
          format='{percent:2.0%}',
          disconnected_message='',
          foreground=color[3],
          mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
        ),
        widget.Net(
          decorations=[RectDecoration(colour=color[0], radius=[0,9,9,0], padding_y=1, filled=True)],
          background=color[7]+"22",
          fontsize=font_size ,
          prefix='M',
          interface=wifi,
          format='{down:1.1f}M',
          foreground=secondary_color[7],
          use_bits=True,
          mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
        ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        widget.UPowerWidget(
          decorations=[RectDecoration(colour=color[0], radius=9, padding_y=1, filled=True)],
          background=color[7]+"22",
          padding_y=1,
          fontsize=font_size,
          border_charge_colour=color[3],
          border_colour=secondary_color[0],
          border_critical_colour='#cc0000',
          fill_critical='#cc0000',
          fill_low='#FF5511',
          fill_normal=color[3],
          foreground=color[3],
          percentage_critical=0.2,
          percentage_low=0.4,
          text_charging=' ({percentage:.0f}%) {ttf} to ',
          text_discharging=' ({percentage:.0f}%) {tte} Left',
        ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        widget.WidgetBox(
              decorations=[RectDecoration(colour=color[0], radius=5, filled=True)],
              background=color[7]+"22",
              text_closed='',
              text_open='',
              foreground=color[7],
              widgets=[
                  widget.Systray(),
                  ]
            ),
        widget.Spacer(
          length=5,
          background=color[7]+"22",
        ),
        widget.KeyboardLayout(
          configured_keyboards=['us intl', 'latam'],
          fontsize=font_size ,
          foreground=secondary_color[7],
          decorations=[RectDecoration(colour=color[0], radius=9, filled=True)],
          background=color[7]+"22",
        ),]
    return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1


def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=bar_margin))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=bar_margin))]

if bar_position == "top":
  screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()
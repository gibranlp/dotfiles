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
              foreground=color[1],
              background=transparent,
              padding=-1,
              fontsize=font_size+0,
              text="░▒▓",
            ),
            widget.CurrentLayout(
              decorations=[BorderDecoration(colour=color[0], border_width=2)],
              padding=5,
              background=color[1],
              foreground=color[0],
              scale=0.8,
            ),
            widget.TextBox(
              foreground=color[2],
              background=color[1],
              padding=-1,
              fontsize=font_size+3,
              text="░",
            ),
            widget.CPU(
              foreground=color[0],
              background=color[2],
              format='{load_percent}%',
              decorations=[BorderDecoration(colour=color[0], border_width=2)],
              padding=5,
            ),
            widget.TextBox(
              foreground=color[4],
              background=color[2],
              padding=-1,
              fontsize=font_size+3,
              text="░",
            ),
            widget.WindowName(
              background=color[4],
              foreground=color[0],
              width=widget_width,
              format='{state} {name}',
              scroll=True,
              scroll_delay=2,
              scroll_repeat=True,
              scroll_step=1,
              decorations=[BorderDecoration(colour=color[0], border_width=2)],
              padding=5,
            ),
            widget.TextBox(
              foreground=color[6],
              background=color[4],
              padding=-1,
              fontsize=font_size+3,
              text="░",
            ),
            widget.Mpris2(
              background=color[6],
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
              objname=None,
              foreground=color[0],
              width=widget_width,
              format='{xesam:artist}  {xesam:title}',
              stopped_text="Stop",
              paused_text='  ',
              scroll=True,
              scroll_repeat=True,
              scroll_delay=0.1,
              decorations=[BorderDecoration(colour=color[0], border_width=2)],
              padding=5,
            ),
            widget.TextBox(
              foreground=color[3],
              background=color[6],
              padding=-1,
              fontsize=font_size+3,
              text="░",
            ),
            widget.Pomodoro(
              background=color[3],
              foreground=color[0],
              color_active=color[0],
              color_break=color[0],
              color_inactive=color[0],
              length_long_break=30,
              length_pomodori=45,
              length_short_break=15,
              notification_on=True,
              num_pomodori=3,
              prefix_active=' ',
              prefix_inactive='',
              prefix_break=' ',
              prefix_long_break=' ',
              prefix_paused=' ',
              decorations=[BorderDecoration(colour=color[0], border_width=2)],
              padding=5,
            ),
            widget.TextBox(
              foreground=color[4],
              background=color[3],
              padding=-1,
              fontsize=font_size+3,
              text="░",
            ),
            widget.Prompt(
              background=color[4],
              prompt=prompt,
              foreground=color[0],
              cursor_color=color[0],
              visual_bell_color=[0],
              visual_bell_time=0.2,
              decorations=[BorderDecoration(colour=color[0], border_width=2)],
              padding=5,
            ),
            widget.TextBox(
              foreground=color[4],
              background=transparent,
              padding=-1,
              fontsize=font_size+0,
              text="▓▒░",
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=transparent,
            ),
            widget.TextBox(
              foreground=color[0],
              background=transparent,
              padding=-1,
              fontsize=font_size+0,
              text="░▒▓",
            ),
            widget.GroupBox(
              background=color[0],
              fontsize=groups_font,
              font=awesome_font,
              disable_drag=True,
              hide_unused=hide_unused_groups,
              borderwidth=0,
              active=secondary_color[0], #Program opened in that group
              inactive=color[6], # Empty Group
              rounded=False,
              highlight_method="text",
              this_current_screen_border=color[1],
              center_aligned = True,
              other_curren_screen_border=color[1],
              block_highlight_text_color=color[1],    
              urgent_border="fc0000",
              decorations=[BorderDecoration(colour=color[1], border_width=2)],
              #visible_groups=['Escape','1','2','3','4'],
            ),
            widget.TextBox(
              foreground=color[0],
              background=transparent,
              padding=-1,
              fontsize=font_size+0,
              text="▓▒░",
            ),
            widget.Spacer(
              length=bar.STRETCH,
              background=transparent,
            ),
            widget.WidgetBox(
              background=transparent,
              text_closed='',
              text_open='',
              foreground=color[1],
              widgets=[
                  widget.Spacer(
                  length=5,
                  background=transparent,
            ),
                  widget.Systray(),]
            ),
            widget.TextBox(
              foreground=secondary_color[5],
              background=transparent,
              padding=-1,
              fontsize=font_size+0,
              text="░▒▓",
            ),
            widget.OpenWeather(
              background=secondary_color[5],
              foreground=color[0],
              app_key=w_appkey,
              cityid=w_cityid,
              weather_symbols={
                "Unknown": "",
                "01d": "",
                "01n": "",
                "02d": "",
                "02n": "",
                "03d": "",
                "03n": "",
                "04d": "",
                "04n": "",
                "09d": "⛆",
                "09n": "⛆",
                "10d": "",
                "10n": "",
                "11d": "🌩",
                "11n": "🌩",
                "13d": "❄",
                "13n": "❄",
                "50d": "🌫",
                "50n": "🌫",
                },
                format='{icon} {temp}°{units_temperature}',
                scroll=True,
                width=widget_width -50,
                metric=True,
                update_interval=600,
                decorations=[BorderDecoration(colour=color[0], border_width=2)],
                padding=5,
                mouse_callbacks={'Button1':lazy.group['scratchpad'].dropdown_toggle("weather"),}
            ),
            widget.TextBox(
              foreground=secondary_color[3],
              background=secondary_color[5],
              padding=-1,
              fontsize=font_size+3,
              text="░",
            ),
            ## Network
            widget.TextBox(
              background=secondary_color[3],
              text=wifi_icon,
              foreground=color[0],
              decorations=[BorderDecoration(colour=color[0], border_width=[2,0,2,2])],
              padding=5,
            ),
            widget.Wlan(
              background=secondary_color[3],
              interface=wifi,
              format='{essid} {percent:2.0%}',
              disconnected_message='',
              foreground=color[0],
              width=widget_width -50,
              scroll=True,
              scroll_repeat=True,
              scroll_interval=0.1,
              scroll_step=1,
              update_interval=1,
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              decorations=[BorderDecoration(colour=color[0], border_width=[2,0,2,0])],
              padding=5,
            ),
            widget.Net(
              prefix='M',
              interface=wifi,
              format='{down:1.1f}M',
              foreground=color[0],
              use_bits=True,
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              background=secondary_color[3],
              decorations=[BorderDecoration(colour=color[0], border_width=[2,2,2,0])],
              padding=5,
            ),
            widget.TextBox(
              foreground=secondary_color[4],
              background=secondary_color[3],
              padding=-1,
              fontsize=font_size+3,
              text="░",
            ),
            widget.KeyboardLayout(
              background=secondary_color[4],
              configured_keyboards=['us intl', 'latam'],
              foreground=color[0],
              decorations=[BorderDecoration(colour=color[0], border_width=2)],
              padding=5,
            ),
            widget.TextBox(
              foreground=color[2],
              background=secondary_color[4],
              padding=-1,
              fontsize=font_size+3,
              text="░",
            ),
            widget.Clock(
              foreground=color[0],
              format="%a %d %H:%M",
              update_interval=1,
              background=color[2],
              mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
              decorations=[BorderDecoration(colour=color[0], border_width=2)],
              padding=5,
            ),
            # widget.Battery(
            #   background=color[2],
            #   foreground=color[0],
            #   full_char='',
            #   charge_char='',
            #   discharge_char='',
            #   empty_char='',
            #   format='{char} {percent:2.0%}',
            #   low_percentage=0.3,
            #   notify_below=0.4,
            #   unknown_char='',
            #   ),
            widget.TextBox(
              foreground=color[2],
              background=transparent,
              padding=-1,
              fontsize=font_size,
              text="▓▒░",
            ),
            ]
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
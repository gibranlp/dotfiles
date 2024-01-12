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
    padding=6,
)

# Theme
## Screens
def init_widgets_list():
  widgets_list = [
    widget.GroupBox(
      decorations=[BorderDecoration(colour=color[0], border_width=4)],
      background=color[0],
      fontsize=groups_font,
      font=awesome_font,
      disable_drag=True,
      hide_unused=hide_unused_groups,
      borderwidth=0,
      active=secondary_color[1], #Program opened in that group
      inactive=third_color[0], # Empty Group
      rounded=False,
      highlight_method="text",
      this_current_screen_border=color[7],
      center_aligned = True,
      other_curren_screen_border=color[7],
      block_highlight_text_color=color[7],    
      urgent_border="fc0000",
    ),
    widget.CurrentLayoutIcon(
      use_mask=True,
      background=color[6],
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      foreground=color[0],
      scale=0.6,
    ),
    widget.Prompt(
      background=color[6],
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      prompt=prompt,
      foreground=color[0],
      cursor_color=color[0],
      visual_bell_color=[0],
      visual_bell_time=0.2,
    ),
    widget.WidgetBox(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[0],
      text_closed='',
      text_open='',
      foreground=color[7],
      widgets=[
        widget.Visualiser(
          decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
          background=color[0],
          bar_colour=color[2],
          width=200,
          bars=32,
          channels='stereo',
          framerate=60,
          hide=True,
          mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
        ),
        ]
    ),
    widget.Mpris2(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[7],
      mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle("music")},
      objname=None,
      foreground=color[0],
      width=widget_width,
      format='{xesam:artist} - {xesam:title}',
      stopped_text="Stop",
      paused_text='  ',
      scroll=True,
      scroll_repeat=True,
      scroll_delay=0.1,
    ),
    widget.Pomodoro(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[0],
      foreground=color[7],
      color_active=color[7],
      color_break=color[1],
      color_inactive=color[7],
      length_long_break=30,
      length_pomodori=45,
      length_short_break=15,
      notification_on=True,
      num_pomodori=3,
      prefix_active='',
      prefix_inactive='',
      prefix_break='',
      prefix_long_break='',
      prefix_paused=' ',
    ),
    widget.Spacer(
      length=bar.STRETCH,
      decorations=[BorderDecoration(colour=color[0], border_width=[4,4,4,0])],
      background=color[0],
    ),
    widget.WindowName(
      background=color[7],
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      foreground=color[0],
      width=widget_width,
      format='{name}',
      scroll=True,
      scroll_delay=2,
      scroll_repeat=True,
      scroll_step=1,
    ),
    widget.Spacer(
      length=bar.STRETCH,
      decorations=[BorderDecoration(colour=color[0], border_width=[4,4,4,0])],
      background=color[0],
    ),
    widget.TextBox(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[0],
      foreground=color[7],
      text="",
    ),
    widget.KeyboardLayout(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[0],
      foreground=color[7],
      configured_keyboards=['us intl', 'latam'],
    ),
    widget.OpenWeather(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[1],
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
        format='{icon}',
        foreground=color[0],
        metric=True,
        update_interval=600,
        mouse_callbacks={'Button1':lazy.group['scratchpad'].dropdown_toggle("weather"),}
    ),
    widget.OpenWeather(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,4,4,0])],
      background=color[1],
      app_key=w_appkey,
      scroll=True,
      width=widget_width -60,
      cityid=w_cityid,
      foreground=color[0],
      format='{temp}°{units_temperature}',
      metric=True,
      update_interval=600,
      mouse_callbacks={'Button1':lazy.group['scratchpad'].dropdown_toggle("weather"),}
    ),
    widget.TextBox(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,4,4,0])],
      background=color[0],
      text="",
      foreground=color[2],
      mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
    ),
    widget.ALSAWidget(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,4,4,0])],
      background=color[0],
      device='Master',
      bar_colour_high=color[2],
      bar_colour_normal=color[2],
      bar_colour_mute=color[2],
      hide_interval=5,
      update_interval=0.1,
      bar_width=50,
      mode='bar',
      text_format=' ',
    ),
    ## Network
    widget.WidgetBox(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[3],
      foreground=color[0],
      text_closed=wifi_icon,
      text_open='',
      widgets=[
        widget.TextBox(
        decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
        text='',
        background=color[0],
        foreground=color[3],
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
      widget.TextBox(
        decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
        background=color[3],
        foreground=color[0],
        text=private_ip,
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
      widget.TextBox(
        decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
        background=color[0],
        foreground=color[3],
        text='',
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
      widget.TextBox(
        decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
        background=color[3],
        foreground=color[0],
        text=public_ip,
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
      widget.TextBox(
        decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
        background=color[0],
        foreground=color[3],
        text=wifi_icon,
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}),
      ]
    ),
    widget.Wlan(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[3],
      foreground=color[0],
      interface=wifi,
      format='{essid} {percent:2.0%}',
      disconnected_message='',
      width=widget_width -20,
      scroll=True,
      scroll_repeat=True,
      scroll_interval=0.1,
      scroll_step=1,
      update_interval=1,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
    ),
    widget.Net(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,4,4,0])],
      background=color[3],
      foreground=color[0],
      prefix='M',
      interface=wifi,
      format='{down:1.1f}M',
      use_bits=True,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
    ),
    widget.Clock(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[0],
      foreground=color[4],
      format="%a",
      update_interval=1,
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
    ),
    widget.Clock(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[4],
      foreground=color[0],
      format="%d",
      update_interval=1,
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
    ),
    widget.Clock(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,4,4,0])],
      background=color[0],
      foreground=color[4],
      format="%H:%M",
      update_interval=1,
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},              
    ),      
    widget.UPowerWidget(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
      background=color[5],
      foreground=color[0],
      border_charge_colour=color[0],
      border_colour=secondary_color[0],
      border_critical_colour='#cc0000',
      fill_critical='#cc0000',
      fill_low='#FF5511',
      fill_normal=color[3],
      percentage_critical=0.2,
      percentage_low=0.4,
      text_charging=' ({percentage:.0f}%) {ttf} to ',
      text_discharging=' ({percentage:.0f}%) {tte} Left',
    ),
    widget.Systray(
      decorations=[BorderDecoration(colour=color[0], border_width=[4,0,4,0])],
    )]
  return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1

def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=color[0],margin=bar_margin))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=color[0],margin=bar_margin))]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()
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
        foreground=secondary_color[6],
        text="",
      ),
      widget.ThermalSensor(
        background=color[6],
        foreground=secondary_color[0],
        format='{temp:.1f}{unit}',
      ),
      widget.TextBox( 
        foreground=secondary_color[5],
        text="",
      ),
      widget.CPU(
        background=color[5],
        foreground=secondary_color[0],
        format='{load_percent}%'
      ),
      widget.TextBox(
      foreground=secondary_color[1],
      text="",
      ),
      widget.Memory(
        background=color[1],
        foreground=secondary_color[0],
        format='{MemUsed:.0f}{mm}',
        measure_mem='M',
      ),
      widget.TextBox(
        foreground=secondary_color[2],
        text="",
      ),
      widget.WindowName(
        background=color[2],
        foreground=secondary_color[0],
        width=widget_width,
        format='{name}',
        scroll=True,
        scroll_delay=2,
        scroll_repeat=True,
        scroll_step=1,
      ),
      widget.WidgetBox(
        text_closed='',
        text_open='',
        foreground=secondary_color[6],
        widgets=[
            widget.Visualiser(
              background=secondary_color[6],
              bar_colour=secondary_color[0],
              width=widget_width - 50,
              bars=16,
              channels='stereo',
              framerate=30,
              hide=True,
              mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
            ),
            ]
      ),
      widget.Mpris2(
        background=color[6],
        mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle("music")},
        objname=None,
        foreground=secondary_color[0],
        width=widget_width,
        format='{xesam:artist} - {xesam:title}',
        stopped_text="Stop",
        paused_text='',
        scroll=True,
        scroll_repeat=True,
        scroll_delay=0.1,
      ),
      widget.TextBox(
        text="",
        foreground=secondary_color[6],
      ),
      widget.WidgetBox(
        background=color[5],
        text_closed='',
        text_open='',
        foreground=secondary_color[0],
        widgets=[
            widget.Systray(),]
      ),
      widget.Prompt(
        prompt=prompt,
        foreground=secondary_color[4],
        cursor_color=secondary_color[4],
        visual_bell_color=[4],
        visual_bell_time=0.2,
      ),
      widget.Spacer(
        length=bar.STRETCH,
      ),
      widget.GroupBox(
        fontsize=groups_font,
        font=awesome_font,
        disable_drag=True,
        hide_unused=hide_unused_groups,
        borderwidth=0,
        active=secondary_color[1], #Program opened in that group
        inactive=secondary_color[5], # Empty Group
        rounded=False,
        highlight_method="text",
        this_current_screen_border=secondary_color[2],
        center_aligned = True,
        other_curren_screen_border=secondary_color[2],
        block_highlight_text_color=secondary_color[2],    
        urgent_border="fc0000"
      ),
      widget.Spacer(
        length=bar.STRETCH,
      ),
      widget.OpenWeather(
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
          foreground=secondary_color[5],
          metric=True,
          update_interval=600,
          mouse_callbacks={'Button1':lazy.group['scratchpad'].dropdown_toggle("weather"),}
      ),
      widget.OpenWeather(
        background=color[6],
        app_key=w_appkey,
        scroll=True,
        width=widget_width -60,
        cityid=w_cityid,
        foreground=secondary_color[0],
        format='{temp}°{units_temperature}',
        metric=True,
        update_interval=600,
        mouse_callbacks={'Button1':lazy.group['scratchpad'].dropdown_toggle("weather"),}
      ), 
      ## Network
      widget.TextBox(
        text=wifi_icon,
        foreground=secondary_color[3],
      ),
      widget.Wlan(
        background=secondary_color[3],
        interface=wifi,
        format='{essid}',
        disconnected_message='',
        foreground=secondary_color[0],
        width=widget_width -20,
        scroll=True,
        scroll_repeat=True,
        scroll_interval=0.1,
        scroll_step=1,
        update_interval=1,
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
      ),
      widget.Wlan(
        background=secondary_color[3],
        interface=wifi,
        format='{percent:2.0%}',
        disconnected_message='',
        foreground=secondary_color[0],
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
      ),
      widget.Net(
        prefix='M',
        interface=wifi,
        format='{down:1.1f}M',
        foreground=secondary_color[0],
        use_bits=True,
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
        background=secondary_color[3],
      ),
      
      widget.TextBox(
        text="",
        foreground=secondary_color[4],
        mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
      ),
      widget.ALSAWidget(
        device='Master',
        bar_colour_high=secondary_color[4],
        bar_colour_normal=secondary_color[4],
        bar_colour_mute=secondary_color[1],
        hide_interval=5,
        update_interval=0.1,
        bar_width=50,
        mode='bar',
        text_format=' ',
      ),
      widget.Clock(
        foreground=secondary_color[0],
        format="%a",
        update_interval=1,
        background=secondary_color[1],
        mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
      ),
      widget.Clock(
        foreground=secondary_color[1],
        format="%d",
        update_interval=1,
        mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
      ),
      widget.Clock(
        foreground=secondary_color[0],
        format="%H:%M",
        update_interval=1,
        background=secondary_color[1],
        mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},              
      ),
      widget.TextBox( 
        text="",
        foreground=secondary_color[4],
      ),
      widget.KeyboardLayout(
        background=secondary_color[4],
        configured_keyboards=['us intl', 'latam'],
        foreground=secondary_color[0],
      ),
      widget.UPowerWidget(
          border_charge_colour=secondary_color[3],
          border_colour=secondary_color[0],
          border_critical_colour='#cc0000',
          fill_critical='#cc0000',
          fill_low='#FF5511',
          fill_normal=secondary_color[3],
          foreground=secondary_color[3],
          percentage_critical=0.2,
          percentage_low=0.4,
          text_charging=' ({percentage:.0f}%) {ttf} to ',
          text_discharging=' ({percentage:.0f}%) {tte} Left',
      )
      ]
    return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1


def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=secondary_color[0],margin=bar_margin))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=secondary_color[0],margin=bar_margin))]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()
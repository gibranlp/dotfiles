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
# Theme 

widget_defaults = dict(
    font=main_font,
    fontsize=font_size,
    padding=4,
)
## Decorations

powerline = {
    "decorations":[RectDecoration(use_widget_background=True, radius=0, filled=True), PowerLineDecoration(path="forward_slash")],
}

## Screens

def init_widgets_list():
    widgets_list = [
        widget.TextBox(
          background=color[1],
          foreground=color[0],
          text="",
          mouse_callbacks={'Button1': lambda: qtile.function(control_panel)},
        ),
        widget.CurrentLayout(
          foreground=color[0],
          background=color[1],
          **powerline,
        ),
        widget.GroupBox(
          background=color[0],
          fontsize=groups_font,
              font=awesome_font,
          disable_drag=True,
          hide_unused=hide_unused_groups,
          borderwidth=0,
          active=color[3], #Program opened in that group
          inactive=color[6], # Empty Group
          rounded=False,
          highlight_method="text",
          this_current_screen_border=color[2],
          center_aligned = True,
          other_curren_screen_border=color[2],
          block_highlight_text_color=color[2],    
          urgent_border="fc0000",
        ),
        widget.WindowName(
          background=color[0],
          foreground=color[3],
          width=widget_width,
          format='{name}',
          scroll=True,
          scroll_delay=2,
          scroll_repeat=True,
          scroll_step=1,  
          **powerline,  
        ),
        widget.Prompt(
          background=color[3],
          prompt=prompt,
          foreground=color[0],
          cursor_color=color[0],
          visual_bell_color=[0],
          visual_bell_time=0.2,
          **powerline,
        ),
        widget.WidgetBox(
              background=color[3],
              text_closed='',
              text_open='',
              foreground=color[0],
              **powerline,
              widgets=[
                  widget.Spacer(
                  length=5,
                  background=transparent,
            ),
                  widget.Systray(),]
            ),
        widget.Spacer(
          length=bar.STRETCH,
          background=transparent,
          **powerline,
        ),
        widget.OpenWeather(
          background=color[3],
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
            "50d": "",
            "50n": "",
            },
            format='{icon}',
            foreground=color[0],
            metric=True,
            update_interval=600,
            **powerline,
            mouse_callbacks={'Button1':lazy.group['scratchpad'].dropdown_toggle("weather"),}
        ),
        widget.Mpris2(
          background=color[0],
          mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
          objname=None,
          foreground=color[3],
          width=widget_width,
          format='{xesam:artist}  {xesam:title}',
          paused_text='  ',
          scroll=True,
          scroll_repeat=True,
          scroll_delay=0.1,
          **powerline,
        ),
        ## Network
        widget.WidgetBox(
          background=color[0],
          text_closed=wifi_icon,
          text_open='',
          foreground=color[3],
          **powerline,
          widgets=[
              widget.TextBox(
              background=color[0],
              text='',
              foreground=color[3],
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              **powerline,
            ),
            widget.TextBox(
              background=color[2],
              text=private_ip,
              foreground=color[0],
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              **powerline,
            ),
            widget.TextBox(
              background=color[0],
              text='',
              foreground=color[3],
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              **powerline,
            ),
            widget.TextBox(
              background=color[4],
              text=public_ip,
              foreground=color[0],
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              **powerline,
            ),
            widget.TextBox(
              background=color[0],
              text=wifi_icon,
              foreground=color[3],
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              **powerline,
            ),
          ]
        ),
        widget.Wlan(
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
              mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
              background=color[0],
            ),
        widget.Wlan(
                background=color[0],
                interface=wifi,
                format='{percent:2.0%}',
                disconnected_message='',
                foreground=color[3],
                mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
                **powerline,
        ),
        widget.TextBox(
          background=color[0],
          text="",
          foreground=color[3],
          mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
          **powerline,
        ),
        widget.ALSAWidget(
          background=color[0],
          device='Master',
          bar_colour_high=color[3],
          bar_colour_loud=color[3],
          bar_colour_normal=color[3],
          bar_colour_mute=color[3],
          hide_interval=5,
          update_interval=0.1,
          bar_width=80,
          mode='bar',
          foreground=color[3],
          text_format=' ',
          **powerline,
        ),
        widget.UPowerWidget(
            border_charge_colour=color[3],
            border_colour=secondary_color[0],
            border_critical_colour='#cc0000',
            fill_critical='#cc0000',
            fill_low='#FF5511',
            fill_normal=color[3],
            foreground=color[3],
            background=color[0],
            percentage_critical=0.2,
            percentage_low=0.4,
            text_charging=' ({percentage:.0f}%) {ttf} to ',
            text_discharging=' ({percentage:.0f}%) {tte} Left',
            **powerline,
        ),
        widget.Clock(
          foreground=color[0],
          format="%a %d %H:%M",
          update_interval=1,
          background=color[1],
          mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)}, 
          **powerline,
        ),
        ## Lock, Logout, Poweroff
        widget.TextBox(
          background=color[1],
          foreground=color[0],
          text="",
          mouse_callbacks={'Button1': lambda: qtile.function(session_widget)},
        )]
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
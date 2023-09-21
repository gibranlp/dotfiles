from functions import *
def i3lock_colors(qtile):
  subprocess.run(['i3lock', 
    '--image=%s' % wallpaper,
    '--fill',          
    '--ring-color={}'.format(color[0]),
    '--inside-color={}'.format(color[0]),
    '--line-color={}'.format(color[2]),
    '--separator-color={}'.format(color[4]),
    '--time-color={}'.format(color[2]),           
    '--date-color={}'.format(color[4]),
    '--insidever-color={}'.format(color[0]),
    '--ringver-color={}'.format(color[0]),
    '--verif-color={}'.format(color[5]),          
    '--verif-text=Validating',
    '--insidewrong-color={}'.format(color[0]),
    '--ringwrong-color={}'.format(color[0]),
    '--wrong-color={}'.format(color[1]),
    '--wrong-text=Wrong!',
    '--keyhl-color={}'.format(color[1]),         
    '--bshl-color={}'.format(color[6]),            
    '--clock',
    '--indicator',       
    '--time-str=%H:%M:%S',
  ])

i3lock_colors(qtile)
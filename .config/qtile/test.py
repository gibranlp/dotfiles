from functions import *

## Update SpectrumOS verssion
def update_ver(qtile):
  variables[0] = remote_version + "\n"
  with open(home + '/.config/qtile/variables', 'w') as file:
      file.writelines(variables)
  subprocess.run(["notify-send","-a", " SpectrumOS", "Updated to the version", "%s" % remote_version])

update_ver(qtile)
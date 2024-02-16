from functions import *

#subprocess.run(["openrgb", "-d", "0", "-c", color[1].lstrip('#')])
#subprocess.Popen(openrgb -d 0 -c %s, %color[1].lstrip('#'), shell=True)
#subprocess.run(["openrgb","-d","0","-c",color[1].lstrip('#')])
#subprocess.run(["openrgb","-d","0","-c",rgb1])
#subprocess.run([f"openrgb","-d","0","-c",[rgb1]])

subprocess.run(["sudo", "openrgb", "-d", "0", "-c", "%s" %color[1].lstrip('#')])
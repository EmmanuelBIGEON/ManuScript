import pystray
import commands 
from app import app
import PIL;
import util;

# Le donut !
image = PIL.Image.open(util.getPathTo("favicon.ico"))

def generate_pystray():
  menu = pystray.Menu()
  
  menuItems = []
  menuItems.append(pystray.MenuItem("Open", showWindow))
  for command in commands.commands:
    menuItems.append(pystray.MenuItem(command.name, command.execute))
  menuItems.append(pystray.MenuItem("Exit", exit))
  menu = pystray.Menu(*menuItems)
  icon = pystray.Icon("ManuScript", image, "ManuScript", menu=menu)
  return icon

# define interactions between system tray icon and window
# When display the window, destroy the system tray icon.
def showWindow():
    icon.stop()
    app.deiconify()
    
# When hide the window, create the system tray icon.
def withdrawWindow():
    global icon 
    app.withdraw()
    icon = generate_pystray()
    icon.run()

# On Exit Destroy both window and system tray.
def exit():
    icon.stop()
    app.destroy()

# define the action on click (launch the command)
def on_clickedicon(icon, item):
    print("clicked" + item)

# setup icon.
icon = generate_pystray()

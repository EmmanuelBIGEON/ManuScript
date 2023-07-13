from tendo import singleton
import sys 


# Make sure only one instance is open at a time.
try:
  me = singleton.SingleInstance() 
except:
  # Bad catch for except. But it works. since program will exit without printing an error anyway.
  print("Another instance of this program is already running.")
  sys.exit(1)
  

import commands
import basic


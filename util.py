import os
import sys

# Not working properly, because files aren't shipped with the executable by PyInstaller (TODO)
def getPathTo(filename):
  return os.path.join(os.getcwd(), filename)

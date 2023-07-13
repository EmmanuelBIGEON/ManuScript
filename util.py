import os
import sys

# Because Pyinstaller needs to have an absolute path to the ico.
def getPathTo(filename):
  return os.path.join(os.getcwd(), filename)

# print(getPathTo("favicon.ico"))
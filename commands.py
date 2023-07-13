import json
import os
import subprocess

commands = [] # list of commands
maxid=0;

class Command:
  
  def __init__(self, id, name, command, open_terminal=False, persistent_terminal=False):
    self.id = id
    self.name = name
    self.cmd = command
    self.open_terminal = open_terminal
    self.persistent_terminal = persistent_terminal
    
  def to_json(self):
    return {'id': self.id, 'name': self.name, 'cmd': self.cmd, 'open_terminal': self.open_terminal, 'persistent_terminal': self.persistent_terminal}
  
  def SetTerminalDisplayed(self, bool):
    if bool:
      self.open_terminal = True;
    else:
      self.open_terminal = False;
    save_commands(commands)
    
  def SetPersistentTerminal(self, bool):
    """
    Set the terminal to be persistent or not
    Auto set the open_terminal to True if parameter is true
    """
    if bool:
      self.open_terminal = True
      self.persistent_terminal = True 
    else:
      self.persistent_terminal = False
    save_commands(commands)
  
  def execute(self):
    """
    Only works on window for now. Maybe a linux implementation will be added later
    """
    print("executing : " + self.cmd)
    if self.open_terminal:
      if self.persistent_terminal:
        subprocess.Popen(["start", "cmd", "/k", self.cmd], shell=True)
      else:
        subprocess.Popen(["start", "cmd", "/c", self.cmd], shell=True)
    else:
      subprocess.call(self.cmd, shell=True)

# -- End of class Command --

def retrieve_commands():
  """
  Retrieve the commands from the commands.json file
  :return: list of commands
  """
  if(not os.path.exists("commands.json") or os.path.getsize("commands.json") == 0):
    with open("commands.json", "w") as f:
      json.dump({'commands' : []}, f, indent=4) 
  with open("commands.json", "r") as f:
    data = json.load(f)
    retrieved_commands = []
    for d in data['commands']:
      cmd = Command(d['id'], d['name'], d['cmd'], d['open_terminal'], d['persistent_terminal'])
      retrieved_commands.append(cmd)
  return retrieved_commands
      
def save_commands(commands):
  """
  Save the commands to the commands.json file, overwrite the current content of the file
  """
  with open("commands.json", "w") as f:
    jsondata = {'commands' : []}
    for cmd in commands:
      jsondata['commands'].append(cmd.to_json())
    json.dump(jsondata, f, indent=4)
        
def command_create(name, command):
  global commands
  id = get_available_id()
  command = Command(id, name, command)
  commands.append(command)
  save_commands(commands)
  return command
  
def clear_commands():
  global commands
  """
  Clear all commands from file and variable : commands
  """
  # delete file
  if(os.path.exists("commands.json")):
    os.remove("commands.json")
  
  # clear variable
  commands.clear()
  
def get_available_id(): 
  global commands, maxid
  availableId = maxid;
  if(len(commands) != 0):
    availableId = max(commands, key=lambda x: x.id).id + 1
    
  maxid = availableId + 1;
  return availableId
    

commands = retrieve_commands()
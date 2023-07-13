import customtkinter
import tkinter as tk
from app import app
from commands import commands as commands_list, Command, get_available_id, command_create, save_commands

import systray


def on_enter_pressed(event):
    print("no line return, keep the command on a single line.")
    return 'break'

def on_changed_name(event,id):
    for command in commands_list:
      if(command.id == id):
        command.name = event.widget.get("1.0", tk.END).strip()
        save_commands(commands_list)
        
def on_changed_cmd(event,id):
    for command in commands_list:
      if(command.id == id):
        command.cmd = event.widget.get("1.0", tk.END).strip()
        save_commands(commands_list)
  
  
class ScrollableCommands(customtkinter.CTkScrollableFrame):
  def __init__(self, master, command=None, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(2, weight=1)
    self.button_list = []
    self.label_list = []
    self.runbutton_list = []
    self.commandinput_list = []
    self.checkbox_externalconsole_list = []
    self.checkbox_persistent_list = []
    self.idList = []

  def add_item(self, pcommand):
    
    runbutton = customtkinter.CTkButton(self, text="Run", width=100, height=24, command=lambda: pcommand.execute())
    label = customtkinter.CTkTextbox(self, width=200, height=25, activate_scrollbars=False)
    label.insert("0.0", pcommand.name)
    label.bind('<KeyRelease>', lambda event, id=pcommand.id: on_changed_name(event, id))
    label.bind('<Return>', on_enter_pressed)
    commandinput = customtkinter.CTkTextbox(self, height=25, activate_scrollbars=False)
    commandinput.insert("0.0", pcommand.cmd)
    commandinput.bind('<KeyRelease>', lambda event, id=pcommand.id: on_changed_cmd(event, id))
    commandinput.bind('<Return>', on_enter_pressed)
    button = customtkinter.CTkButton(self, text="Delete", width=100, height=24, command= lambda: self.remove_item(pcommand.id))
    checkbox_externalconsole = customtkinter.CTkCheckBox(self, command= lambda: pcommand.SetTerminalDisplayed(checkbox_externalconsole.get()), text="ExternalConsole")
    checkbox_persistent = customtkinter.CTkCheckBox(self,command= lambda: pcommand.SetPersistentTerminal(checkbox_persistent.get()), text="Persistent")
    
    if(pcommand.open_terminal):
      checkbox_externalconsole.select()
    else:
      checkbox_externalconsole.deselect()
      
    if(pcommand.persistent_terminal):
      checkbox_persistent.select()
    else:
      checkbox_persistent.deselect()
    
    
    currentindex = len(self.runbutton_list)
    runbutton.grid(row=currentindex, column=0)
    label.grid(row=currentindex, column=1)
    commandinput.grid(row=currentindex, column=2, sticky="nsew")
    button.grid(row=currentindex, column=3)
    checkbox_externalconsole.grid(row=currentindex, column=4, padx=5)
    checkbox_persistent.grid(row=currentindex, column=5, padx=5)
    
    self.button_list.append(button)
    self.label_list.append(label)
    self.runbutton_list.append(runbutton)
    self.commandinput_list.append(commandinput)
    self.checkbox_externalconsole_list.append(checkbox_externalconsole)
    self.checkbox_persistent_list.append(checkbox_persistent)
    self.idList.append(pcommand.id)
    
  def remove_item(self, idCommand):
    global commands_list
    for command in commands_list:
      if(command.id == idCommand):
        commands_list.remove(command)
        save_commands(commands_list)
        break
      
    currentindex = 0
    for id in self.idList:
      if(id == idCommand):
        break
      currentindex += 1
    
    self.button_list[currentindex].destroy()
    self.button_list.pop(currentindex)
    self.label_list[currentindex].destroy()
    self.label_list.pop(currentindex)
    self.runbutton_list[currentindex].destroy()
    self.runbutton_list.pop(currentindex)
    self.commandinput_list[currentindex].destroy()
    self.commandinput_list.pop(currentindex)
    self.checkbox_externalconsole_list[currentindex].destroy()
    self.checkbox_externalconsole_list.pop(currentindex)
    self.checkbox_persistent_list[currentindex].destroy()
    self.checkbox_persistent_list.pop(currentindex)
    self.idList.pop(currentindex)
    
    for i in range(0, len(self.button_list)):
      self.button_list[i].grid(row=i, column=3)
      self.label_list[i].grid(row=i, column=1)
      self.runbutton_list[i].grid(row=i, column=0)
      self.commandinput_list[i].grid(row=i, column=2, sticky="nsew")
      self.checkbox_externalconsole_list[i].grid(row=i, column=4)
      self.checkbox_persistent_list[i].grid(row=i, column=5)

def createcommand_and_addtolist(scrollablelist, commandname, commandvalue):
  d = command_create(commandname, commandvalue)
  scrollablelist.add_item(d)
  
    
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.scrollablelist = ScrollableCommands(master=app, width=300, height=200, corner_radius=0)
app.scrollablelist.grid(row=0, column=0, sticky="nsew")

for command in commands_list:
  app.scrollablelist.add_item(command)

app.addnewcommand = customtkinter.CTkButton(app, text="New command", width=100, height=50, command= lambda: createcommand_and_addtolist(app.scrollablelist, "NewCommand", "echo \"command value\""))
app.addnewcommand.grid(row=1, column=0, pady=10, padx=10, sticky="ns")
app.protocol("WM_DELETE_WINDOW", systray.withdrawWindow) # Set the withdrawWindow function to be called when the window is closed to keep the application on system tray.
app.mainloop()
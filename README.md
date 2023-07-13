# ManuScript
SystemTray Application for quick launch operations and commands on Windows.
Use CustomTkinter : https://github.com/TomSchimansky/CustomTkinter

You can create commands (name, value)
For now there are only two options : 
- ExternalConsole : Open the terminal and execute the command in it.
- Persistent : Make the terminal persistent after the command ended (if checked, ExternalConsole is automatically true)

![Preview ParticleSandbox](preview.png)

When you close the windows, it put the application in the System Tray icons. From here you can still Open the window and execute any command you created.

![Preview ParticleSandbox](preview2.png)

The commands are saved in a file named commands.json auto-generated.

## Quick Install

There's an installer in the release. Just download it and start the application.

## Run

```
Install the dependencies : customtkinter, pystray, tendo

$ python main.py
```

## Create an executable 

I use PyInstaller, you can install it using : 

```
$ pip install -U pyinstaller
```

Open a terminal in the repository location and run this command.

```
$ pyinstaller -n "ManuScript" -i "favicon.ico" -w main.py
```

Once you're done, copy the "favicon.ico" in the dist/main folder because the executable requires it.
Now you can run the executable "ManuScript.exe" and create a shortcut.
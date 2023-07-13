import customtkinter
import tkinter as tk
import util

windowHeight = 500
windowWidth = 1000

# Create app here for systray access and configuration. Prevent a circular import.
app = customtkinter.CTk();
app.iconbitmap(util.getPathTo("favicon.ico"))
app.title("ManuScript")
app.geometry(f"{windowWidth}x{windowHeight}")
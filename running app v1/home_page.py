import tkinter
import customtkinter
import subprocess
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

# destroy current window exiting the loop so it creates a new one
window = customtkinter.CTk()
window.geometry("495x595")
window.title('Welcome')


def button_function():
    # destroy current window exiting the loop so it creates a new one
    window.destroy()
    subprocess.Popen(["python", r"log_in_page.py"])


button = customtkinter.CTkButton(
    master=window, width=220, text="home page", command=button_function, corner_radius=6)
button.place(x=100, y=220)

window.mainloop()

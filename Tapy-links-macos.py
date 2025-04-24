import tkinter as tk
from tkinter import ttk
from os import system
import subprocess

def app_1():
    system('open -a https://github.com') # opens Github webpage

def app_2():
    system('open -a https://www.youtube.com') #opens Youtube

def app_3():
    system('open -a https://teams.microsoft.com') # opens Teams

def app_4():
    system('open -a https://scratch.mit.edu') # opens scratch

def app_5():
    system('open -a https://www.photopea.com') # open photopea

def app_6():
    system('open -a https://www.google.com') # open google

def app_7():
    system('open -a https://chatgpt.com') #opens Chat gpt

def app_8():
    system('open -a https://duckduckgo.com') # opens DuckDuckGo

def app_9():
    system('open -a https://open.spotify.com') # opens the link to spotify (if you downloded frome the microsoft store you can use that).

def app_10():
    system('open -a https://mail.google.com') # opens the link to google mail

root = tk.Tk()
root.config(width=200, height=350) # Window size
root.title("Links") # Change the title of the window
#root.config(bg="blue") # change the color of the window

buton_1 = ttk.Button(text="Github", command=app_1)
buton_1.place(x=60, y=40)

buton_2 = ttk.Button(text="Youtube", command=app_2)
buton_2.place(x=60, y=65)

buton_3 = ttk.Button(text="Teams", command=app_3)
buton_3.place(x=60, y=90)

buton_4 = ttk.Button(text="Scratch", command=app_4)
buton_4.place(x=60, y=115)

buton_5 = ttk.Button(text="Photopea", command=app_5)
buton_5.place(x=60, y=140)

buton_6 = ttk.Button(text="Goolge", command=app_6)
buton_6.place(x=60, y=165)

buton_7 = ttk.Button(text="Chat GPT", command=app_7)
buton_7.place(x=60, y=190)

buton_8 = ttk.Button(text="DuckDuckGo", command=app_8)
buton_8.place(x=60, y=215)

buton_9 = ttk.Button(text="Spotify", command=app_9)
buton_9.place(x=60, y=240)

buton_10 = ttk.Button(text="Gmail", command=app_10)
buton_10.place(x=60, y=265)

root.mainloop()
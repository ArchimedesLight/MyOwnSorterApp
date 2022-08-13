
from tkinter import *
import os
import datetime as dt


root = Tk()
root.geometry("350x200")

tkinter = Tk


def Spotify():
    os.chdir(r"C:\Users\stuart\AppData\Roaming\Spotify")
    os.startfile(r"C:\Users\stuart\AppData\Roaming\Spotify\Spotify.exe")
    os.system(r"C:\Users\stuart\AppData\Roaming\Spotify/Spotify.exe")    

def Steam():
    os.chdir(r"C:\Program Files (x86)\Steam")
    os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
    os.system(r"C:\Program Files (x86)\Steam/steam.exe")

def Firefox():
    os.chdir(r"C:\Program Files\Mozilla Firefox")
    os.startfile(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    os.system(r"C:\Program Files\Mozilla Firefox/firefox.exe")

def Discord():
    os.chdir(r"C:\Users\stuart\AppData\Local\Discord\app-1.0.9006")
    os.startfile(r"C:\Users\stuart\AppData\Local\Discord\app-1.0.9006\Discord.exe")
    os.system(r"C:\Users\stuart\AppData\Local\Discord\app-1.0.9006z/Discord.exe")

def GOG():
    os.chdir(r"C:\Program Files (x86)\GalaxyClient")
    os.startfile(r"C:\Program Files (x86)\GalaxyClient\GalaxyClient.exe")
    os.system(r"C:\Program Files (x86)\GalaxyClient/GalaxyClient.exe")

def EGS():
    os.chdir(r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32")
    os.startfile(r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")
    os.system(r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32/EpicGamesLauncher.exe")


spotLabel = Label(root, text="Press Here For Spotify", fg="green")
spotLabel.grid(row = 0, column = 1)
spotify = Button(root, text="Spotify",command = Spotify, fg="green", bg="black", width=25, height=1)
spotify.grid(row = 0, column = 0)

steamLabel = Label(root, text="Press Here For Steam", fg="blue")
steamLabel.grid(row = 1, column = 1)
steam = Button(root, text="Steam",command = Steam, fg="blue", bg="black", width=25, height=1)
steam.grid(row = 1, column = 0)

firefoxLabel = Label(root, text="Press Here For Firefox", fg="orange")
firefoxLabel.grid(row = 2, column = 1)
firefox = Button(root, text="Firefox",command = Firefox, fg="orange", bg="black", width=25, height=1)
firefox.grid(row = 2, column = 0)

discordLabel = Label(root, text="Press Here For Discord", fg="purple")
discordLabel.grid(row = 3, column = 1)
discord = Button(root, text="Discord", command = Discord, fg="purple", bg="black", width=25, height=1)
discord.grid(row = 3, column = 0)

GOGLabel = Label(root, text="Press Here For GOG", fg="pink")
GOGLabel.grid(row = 4, column = 1)
gog = Button(root, text="GOG", command = GOG, fg="pink", bg="black", width=25, height=1)
gog.grid(row = 4, column = 0)

EGSLabel = Label(root, text="Press Here For EGS", fg="white", bg="black")
EGSLabel.grid(row = 5, column = 1)
egs = Button(root, text="EGS", command = EGS, fg="white", bg="black", width=25, height=1)
egs.grid(row = 5, column = 0)

date = dt.datetime.now()
TiMe = Label(root, text=f"{date:%I:%M, %A, %B %d, %Y}")
TiMe.grid(row = 7, column = 0)
 
root.mainloop()





from tkinter import *
import os
import datetime as dt

root = Tk()
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

def WarThunder():
    os.chdir(r"F:\Steam Library\steamapps\common\War Thunder\win64")
    os.startfile(r"F:\Steam Library\steamapps\common\War Thunder\win64\aces.exe")
    os.system(r"F:\Steam Library\steamapps\common\War Thunder/win64/aces.exe")
    
spotLabel = Label(root, text="Press Here For Spotify", fg="green", bg="black")
spotLabel.grid(row = 0, column = 1)
spotify = Button(root, text="Spotify",command = Spotify, fg="green", bg="black")
spotify.grid(row = 0, column = 0)

steam = Button(root, text="Steam",command = Steam, fg="blue", bg="black")
steam.grid(row = 1, column = 0)
steamLabel = Label(root, text="Press Here For Steam", fg="blue", bg="black")
steamLabel.grid(row = 1, column = 1)

firefoxLabel = Label(root, text="Press Here For Firefox", fg="orange", bg="black")
firefoxLabel.grid(row = 2, column = 1)
firefox = Button(root, text="Firefox",command = Firefox, fg="orange", bg="black")
firefox.grid(row = 2, column = 0)

discordLabel = Label(root, text="Press Here For Discord", fg="purple", bg="black")
discordLabel.grid(row = 3, column = 1)
discord = Button(root, text="Discord", command = Discord, fg="purple", bg="black")
discord.grid(row = 3, column = 0)

GOGLabel = Label(root, text="Press Here For GOG", fg="pink", bg="black")
GOGLabel.grid(row = 4, column = 1)
discord = Button(root, text="Discord", command = Discord, fg="pink", bg="black")
discord.grid(row = 4, column = 0)

WTLabel = Label(root, text="Press Here For War Thunder", fg="red", bg="black")
WTLabel.grid(row = 5, column = 1)
wt = Button(root, text="War Thunder", command = Discord, fg="red", bg="black")
wt.grid(row = 5, column = 0)

date = dt.datetime.now()
TiMe = Label(root, text=f"{date:%I:%M, %A, %B %d, %Y}")
TiMe.grid(row = 6, column = 0)
 
root.mainloop()




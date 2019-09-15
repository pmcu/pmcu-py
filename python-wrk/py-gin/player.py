from pygame import *
import tkinter as tkinter

#create window

player = tkr.Tk()

#edit window
player.title('Audio Player')
player.geometry("205X340")

#get song
file ="lordRings.mp3"

#action event
def Player():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
def ExitPlayer():
    pygame.mixer.music.stop()


#Register buttons
button1 = tkr.Button(player,width=5,height=3, text="PLAY", command=play)
button1.pack(fill="x")
button2 = tkr.Button(player,width=5,height=3, text="PLAY", command=ExitPlayer)
button2.pack(fill="x")

#Song Name
label1 = tkr.LabelFrame(player, text = "Song Name")
label1.pack()

contents1 = tkr.Label(label1,text = file)
contents1.pack()


#Activate
player.mainloop()

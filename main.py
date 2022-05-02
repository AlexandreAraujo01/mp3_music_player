from turtle import heading
from playsound import playsound
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


class MusicPlayer():
    def __init__(self,win):
        win.geometry('200x200')
        win.title('Music Player')
        win.resizable(0,0)
        self.frame = Frame(win,bg='orange')
        self.frame.pack(fill= BOTH, expand= True)
        
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        # button and their positions
        load_button = Button(win,text='Load',width=10,font=('Arial',11),command=self.load)
        load_button.bind("<Enter>", func=lambda e: load_button.config(background='pink',pady=1))
        load_button.bind("<Leave>", func=lambda e: load_button.config(background='white',pady=0))
        load_button.place(x = 100,y=40,anchor='center')
        
        play_button = Button(win,textvariable=self.play_restart,width=10,font=('Arial',11),command=self.play)
        play_button.place(x = 100,y=80,anchor='center')
        
        pause_button = Button(win,textvariable=self.pause_resume,width=10,font=('Arial',11),command=self.pause)
        pause_button.place(x = 100,y=120,anchor='center')
        
        stop_button = Button(win,text='stop',width=10,font=('Arial',11),command=self.stop)
        stop_button.place(x = 100,y=160,anchor='center')
        
        self.music_file = False
        self.playing_state = False
          
    def load(self):
        self.music_file = filedialog.askopenfilename()
        print('Loaded', self.music_file)
        self.play_restart.set('Play')
        
    def play(self):
        if self.music_file != False:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')
    
    def stop(self):
        mixer.music.stop()
    
    def pause(self):
        if self.playing_state == False:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')
    
    def on_hover(btn):
        btn.config(background='pink')
        
    
root = Tk() 
MusicPlayer(root)
root.mainloop()
          
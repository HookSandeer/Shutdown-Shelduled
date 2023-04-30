#!/usr/bin/python3
# By HookSander

from datetime import datetime
import os
import time
import platform

from tkinter import Tk
from tkinter import *

def shutdown() :
    currentOs = platform.system()
    if currentOs == 'Linux' :
        os.system("shutdown now")
    if currentOs == 'Windows' :
        os.system("shutdown /s /t 0")
    else :
        pass #Message boxe erreur


class Script :
        
    def __init__(self):
        
        def getEntry(self):
            hours = self.hours.get("1.0", END)
            minutes = self.minutes.get("1.0", END)
            print(hours, minutes)
            """
            if hours >= 23 :
                self.hours.delete("1.0", END)
            if minutes >= 59 :
                self.minutes.delete("1.0", END)
            """
        
        self.gui = Tk()
        self.gui.geometry(("450x500"))
        self.gui.minsize(450, 500)
        self.gui.maxsize(450, 500)
        self.gui.title("Arrêt programmé")
        self.gui.configure(background='black')
        
        self.title = Label(self.gui, text="Programmation Arrêt", font=('Arial', 30), fg='white', bg='black')
        self.title.place(x=50, y=10)
        
        self.text1 = Label(self.gui, text="Heure actuelle => ", font=('Arial', 20), fg='white', bg='black')
        self.text1.place(x=50, y=80)
        
        self.clock = Label(self.gui, text="", font=('Arial', 20), fg='red', bg='black')
        self.clock.place(x=270, y=80)
        self.updateClock()
        
        self.text2 = Label(self.gui, text="Heure de l'arrêt => ", font=('Arial', 20), fg='white', bg='black')
        self.text2.place(x=50, y=150)
        
        self.hours = Text(self.gui, width=2, height=1)
        self.hours.place(x=300, y=160)
        
        self.split = Label(self.gui, text=":", font=('Arial', 20), fg='white', bg='black')
        self.split.place(x=330, y=150)
        
        self.minutes = Text(self.gui, width=2, height=1)
        self.minutes.place(x=350, y=160)
        
        self.valide = Button(self.gui, text='ok', command=getEntry(self))
        self.valide.place(x=380, y=155)
        
        self.gui.mainloop()
        
        
    
    def updateClock(self) :
        now = time.strftime("%H:%M:%S")
        self.clock.configure(text = now)
        self.gui.after(1000, self.updateClock)
    
    
            

        
program = Script()
"""
title = Label(gui, text="Programmation d'arrêt", font=('Arial', 20))
title.place(x=20, y=50)

text = Label(gui, text="Entrer l'heure a laquelle vous souhaitez que l'ordinateur s'arrête :", font=('Arial', 10))
text.place(x=20, y=150)

hoursEntry = Text(gui, height=1, width=2)
hoursEntry.place(x=150, y=200)

separation = Label(gui, text=" : ")
separation.place(x=170, y=200)

minutesEntry = Text(gui, height=1, width=2)
minutesEntry.place(x=185, y=200)


gui.mainloop()
"""


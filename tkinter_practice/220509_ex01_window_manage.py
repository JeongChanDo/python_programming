# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:05:22 2022

@author: jdo
"""

import tkinter
from tkinter import *
from tkinter import messagebox

global window

window = Tk()
window.title("window = Tk()")
window.geometry("300x300+100+100")
window.resizable(width=False, height = False)

def ask_quit():
    result = messagebox.askquestion("Msg", "quit?")
    if result == "yes":
        window.destroy()

label = Label(window, text="Buttons")
label.pack() # pack()윈도우에 배치
iconBtn = Button(window, text="iconify", command=window.iconify) #iconify 아이콘화
iconBtn.pack()
quitBtn = Button(window, text="quit", command=window.destroy)
quitBtn.pack()

window.protocol("WM_DELETE_WINDOW", ask_quit)
window.mainloop()

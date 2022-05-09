# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:01:20 2022

@author: jdo
"""

from tkinter import *

window =Tk()
window.title("testing pack layout")
window.geometry("400x300+100+200")



label1 = Label(window, text="label 1", bg="red", fg="white").pack(fill=X, padx=10, pady=10)
label2 = Label(window, text="label 2", bg="green", fg="black").pack(fill=X, padx=10, pady=10)
label3 = Label(window, text="label 3", bg="yellow", fg="white").pack(fill=X, padx=10, pady=10)

label4 = Label(window, text="label 4", bg="red", fg="black").pack(fill=X,padx=10, pady=10, side=LEFT)
label5 = Label(window, text="label 5", bg="green", fg="black").pack(fill=X, padx=10, pady=10, side=LEFT)
label6 = Label(window, text="label 6", bg="blue", fg="black").pack(fill=X, padx=10, pady=10, side=LEFT)

listbox = Listbox(window)
listbox.pack(fill=BOTH, expand=1)
L = [100, 200, 300, 400, 500]
for i in range(len(L)):
    listbox.insert(END, str(L[i]))

mainloop()
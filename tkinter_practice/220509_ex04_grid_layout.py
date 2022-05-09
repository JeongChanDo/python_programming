# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:15:51 2022

@author: jdo
"""

from tkinter import *

def fetch(cells):
    print("- input data -")
    for i, e in enumerate(cells):
        print("  {0}:{1}".format(fields[i], e.get()))

def make_form(fields):
    cells = []
    for r, field in enumerate(fields):
        label = Label(window, width=10, text= field)
        entry = Entry(window)
        label.grid(row=r, column=0, sticky=NSEW)
        entry.grid(row=r, column=1, sticky=NSEW)
        cells.append(entry)
    return cells

if __name__ == "__main__":
    window = Tk()
    window.title("Input Dialog with label and entry")
    fields = ("Name", "Age", "Address")
    cells = make_form(fields)
    window.bind("<Return>", (lambda event, e=cells: fetch(e)))
    #엔터키 눌릴떼 람다식 호출 바인드
    #cells를 e에 담고 fetch 호출
    # 주의 : bind 함수 호출시 lambda 식 앞단에 인수를 2개해야한다.
    Button(window, text="Fetch", bg="green",
           command=(lambda e=cells:fetch(e))).grid(row=3, column=0, sticky=NSEW)
    # 버튼 눌릴때도 fetch(e) 호
    Button(window, text="Quit", bg="Red", command=window.destroy).grid(row=3, column=1, sticky=NSEW)
    print("grid size : ", window.grid_size())
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.mainloop()
        
import tkinter
from tkinter import *

window = Tk()
window.title("window - tk()")
window.geometry("600x600+200+100")
window.resizable(width=False, height=False)



frame1 = Frame(window, bg="light green", cursor="heart", bd=5, padx=10, pady=10, relief=GROOVE) #relief 프레임 기본 스타일
#relief : flat(기본), raised(버튼올린모양), sunken(버튼눌린모양), groove, ridge 등(대문자)
frame1.grid(row=0,column=0)
frame2 = Frame(window, bg="yellow", cursor="man", bd=5, padx=10, pady=10, relief=GROOVE)
frame2.grid(row=1,column=0)
frame3 = Frame(window, bg="yellow", cursor="plus", bd=5, padx=10, pady=10, relief=GROOVE)
frame3.grid(row=2, column=0)


canvas_11 = Canvas(frame1, bg="lime", width=100, height=100)
canvas_11.grid(row=0, column=0, fill=None, padx=10, pady=10)
canvas_12 = Canvas(frame1, bg="orange", width=150, height=100)
canvas_12.grid(row=0, column=1, fill=None, padx=10, pady=10)
canvas_13 = Canvas(frame1, bg="grey", width=100, height=100)
canvas_13.grid(row=1, column=1, fill=None, padx=10, pady=10)


canvas_21 = Canvas(frame2, bg="magenta", width=200, height=50)
canvas_21.grid(row=0, column=0, fill=None, padx=10, pady=10)
canvas_22 = Canvas(frame2, bg="brown", width=200, height=50)
canvas_22.grid(row=0, column=1, fill=None, padx=10, pady=10)
canvas_23 = Canvas(frame2, bg="sky blue", width=200, height=50)
canvas_23.grid(row=1, column=0, fill=None, padx=10, pady=10)

canvas_31 = Canvas(frame3, bg="light green", width=400, height=50)
canvas_31.grid(row=0, column=0, fill=None, padx=10, pady=10)
window.mainloop()
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *

def onSize(event):
    if event.widget == frame: # 이벤트 호출된 위젯이 프레임인경우
        frame.update() # 라벨 변경전 갱신
        label_fr.configure(text="frame size: {}x{}".format(frame.winfo_width(), frame.winfo_height()))
        canvas.update()
        label_cnv.configure(text="canvas size: {}x{}".format(canvas.winfo_width(), canvas.winfo_height()))
    
    
if __name__ == "__main__":
    global label_Fr, label_cnv, frame, canvas
    window =Tk()
    window.title("finding frame and canvas size at resizing events")
    frame = Frame(window, bg="light green", bd=10, padx=50, pady=50, relief=GROOVE)
    frame.pack(expand=YES, fill=BOTH)
    canvas = Canvas(frame, bg="white", width=600, height=400)
    canvas.pack(expand=YES, fill=BOTH, padx=10, pady=10) #frame, canvas 양방향 조절 가능
    frame.update()
    label_fr = Label(canvas, text="frame size: {} x {}".format(frame.winfo_width(), frame.winfo_height()))
    label_fr.grid(row=0, column=0, sticky=N)
    canvas.update()
    label_cnv = Label(canvas, text="canvas size: {} x {}".format(canvas.winfo_width(), canvas.winfo_height()))
    label_cnv.grid(row=1, column=0, sticky=S)
    
    # <Configure> : 위젯모양변경시 이벤트 -> onSize() 호출
    # bind_all(컨피겨, func) -> 모든 위젯 크게 변경시 onsize() 호출 
    window.bind_all("<Configure>", onSize)
    window.mainloop()
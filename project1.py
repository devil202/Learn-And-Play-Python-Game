#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
def main():
    root=Tk()
    root.title("Hangman")
    root.resizable(0,0)

    frame=Frame(root,width=900,height=250)      
    frame.pack()
    frame.pack_propagate(False)

    b_frame=Frame(root,width=900,height=250)
    b_frame.pack(side=BOTTOM)
    frame.pack_propagate(False)
    
    command=lambda : play(root,frame)
    Button_1=Button(frame,text="PLAY",width=40,height=10,command=command,bg="#000000",fg="#ffffff"
    ,activebackground="#ffffff",activeforeground="#000000")
    Button_1.pack()

    command=lambda : root.destroy()
    Button_2=Button(b_frame,text="QUIT",width=40,height=10,command=command,bg="#000000",fg="#ffffff"
    ,activebackground="#ffffff",activeforeground="#000000")
    Button_2.pack()
    root.mainloop()
main()

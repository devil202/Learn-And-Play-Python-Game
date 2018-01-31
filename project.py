#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
x=1
root=Tk()
var1=IntVar()
def check(frame,b_frame):
    global var1
    if(var1.get()==2):
        tkMessageBox.showinfo("result","correct Ans")
    else:
         tkMessageBox.showinfo("result","Wrong Ans")
    global x
    x=x+1
    frame.destroy()
    b_frame.destroy()
    main()
def main():
    global root
    global var1
    frame=Frame(root)
    frame.pack()
    b_frame=Frame(root)
    b_frame.pack(side=BOTTOM)
    if(x==1):
        gifl=PhotoImage(master=frame,file="1814.gif")
        lable1=Label(frame,image=gifl)
        lable1.pack()
        lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
        lable.pack()
        R1=Radiobutton(b_frame,text="COW",variable=var1,value=1)
        R1.pack()
        R2=Radiobutton(b_frame,text="GOAT",variable=var1,value=2)
        R2.pack()
        R3=Radiobutton(b_frame,text="TIGER",variable=var1,value=3)
        R3.pack()
        R4=Radiobutton(b_frame,text="LEOPARD",variable=var1,value=4)
        R4.pack()
        R5=Radiobutton(b_frame,text="MONKEY",variable=var1,value=5)
        R5.pack()
        command=lambda:check(frame,b_frame)
        B=Button(b_frame,text="suubmit",command=command)
        B.pack()
        print x
    elif(x==2):
        print x
        var1=IntVar()
        gifl=PhotoImage(master=frame,file="li21.gif")
        lable1=Label(frame,image=gifl)
        lable1.pack()
        lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
        lable.pack()
        R1=Radiobutton(b_frame,text="COW",variable=var1,value=1)
        R1.pack()
        R2=Radiobutton(b_frame,text="GOAT",variable=var1,value=2)
        R2.pack()
        R3=Radiobutton(b_frame,text="TIGER",variable=var1,value=3)
        R3.pack()
        R4=Radiobutton(b_frame,text="LEOPARD",variable=var1,value=4)
        R4.pack()
        R5=Radiobutton(b_frame,text="MONKEY",variable=var1,value=5)
        R5.pack()
        command=lambda:check(frame,b_frame)
        B=Button(b_frame,text="suubmit",command=command)
        B.pack()
    elif(x==3):
        print x
        var1=IntVar()
        gifl=PhotoImage(master=frame,file="Bellis_perennis_white_(aka).gif")
        lable1=Label(frame,image=gifl)
        lable1.pack()
        lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
        lable.pack()
        R1=Radiobutton(b_frame,text="COW",variable=var1,value=1)
        R1.pack()
        R2=Radiobutton(b_frame,text="GOAT",variable=var1,value=2)
        R2.pack()
        R3=Radiobutton(b_frame,text="TIGER",variable=var1,value=3)
        R3.pack()
        R4=Radiobutton(b_frame,text="LEOPARD",variable=var1,value=4)
        R4.pack()
        R5=Radiobutton(b_frame,text="MONKEY",variable=var1,value=5)
        R5.pack()
        command=lambda:check(frame,b_frame)
        B=Button(b_frame,text="suubmit",command=command)
        B.pack()
    mainloop()
main()

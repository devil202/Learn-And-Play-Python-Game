#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
import sqlite3
x=1
root=Tk()
score=0
root.title("play And Fun") 
root.resizable(0,0)
var1=IntVar()
def check(frame,b_frame):
    conn=sqlite3.connect('game1.db')
    c=conn.cursor()
    c.execute('select * from database')
    value=c.fetchall()
    conn.close()
    global var1
    global score
    global x
    if(value[x-1]==(var1.get(),)):
        tkMessageBox.showinfo("result","correct Ans")
        score+=10
    else:
         tkMessageBox.showinfo("result","Wrong Ans")
         score-=1
    x=x+1
    frame.destroy()
    b_frame.destroy()
    main()
def buttons_FLOWERS(frame,b_frame):
    global var1
    global score
    lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
    lable.grid(row=1,column=1,padx=20,pady=20)
    lable.config(font=("Courier", 25))
    R1=Radiobutton(b_frame,text="LILY",variable=var1,value=1)
    R1.grid(row=2,column=1,padx=20,sticky=W)
    R1.config(font=("Courier", 15))
    R2=Radiobutton(b_frame,text="MARIGOLD",variable=var1,value=2)
    R2.grid(row=3,column=1,padx=20,sticky=W)
    R2.config(font=("Courier", 15))
    R3=Radiobutton(b_frame,text="SUNFLOWER",variable=var1,value=3)
    R3.grid(row=4,column=1,padx=20,sticky=W)
    R3.config(font=("Courier", 15))
    R4=Radiobutton(b_frame,text="LOTUS",variable=var1,value=4)
    R4.grid(row=5,column=1,padx=20,sticky=W)
    R4.config(font=("Courier", 15))
    R5=Radiobutton(b_frame,text="DAISY",variable=var1,value=5)
    R5.grid(row=6,column=1,padx=20 ,sticky=W)
    R5.config(font=("Courier", 15))
    R6=Radiobutton(b_frame,text="ROSE",variable=var1,value=6)
    R6.grid(row=7,column=1,padx=20 ,sticky=W)
    R6.config(font=("Courier", 15))
    B=Button(b_frame,text="suubmit",command=lambda:check(frame,b_frame))
    B.grid(row=8,column=1,padx=20,pady=10)
    B.config(font=("Courier", 15))
    lable2=Label(b_frame,text="total Score")
    lable2.grid(row=9,column=1,padx=10)
    lable2.config(font=("Courier", 30))
    s=str(score)
    lable3=Label(b_frame,text=s)
    lable3.grid(row=9,column=2)
    lable3.config(font=("Courier", 30))

def buttons_BIRDS(frame,b_frame):
    global var1
    global score
    lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
    lable.grid(row=1,column=1,padx=20,pady=20)
    lable.config(font=("Courier", 25))
    R1=Radiobutton(b_frame,text="PEACOCK",variable=var1,value=1)
    R1.grid(row=2,column=1,padx=20,sticky=W)
    R1.config(font=("Courier", 15))
    R2=Radiobutton(b_frame,text="OWL",variable=var1,value=2)
    R2.grid(row=3,column=1,padx=20,sticky=W)
    R2.config(font=("Courier", 15))
    R3=Radiobutton(b_frame,text="PEAGION",variable=var1,value=3)
    R3.grid(row=4,column=1,padx=20,sticky=W)
    R3.config(font=("Courier", 15))
    R4=Radiobutton(b_frame,text="SPARROW",variable=var1,value=4)
    R4.grid(row=5,column=1,padx=20,sticky=W)
    R4.config(font=("Courier", 15))
    R5=Radiobutton(b_frame,text="CROW",variable=var1,value=5)
    R5.grid(row=6,column=1,padx=20 ,sticky=W)
    R5.config(font=("Courier", 15))
    R6=Radiobutton(b_frame,text="KINGFISHER",variable=var1,value=6)
    R6.grid(row=7,column=1,padx=20 ,sticky=W)
    R6.config(font=("Courier", 15))
    B=Button(b_frame,text="suubmit",command=lambda:check(frame,b_frame))
    B.grid(row=8,column=1,padx=20,pady=10)
    B.config(font=("Courier", 15))
    lable2=Label(b_frame,text="total Score")
    lable2.grid(row=9,column=1,padx=10)
    lable2.config(font=("Courier", 30))
    s=str(score)
    lable3=Label(b_frame,text=s)
    lable3.grid(row=9,column=2)
    lable3.config(font=("Courier", 30))

def buttons_ANIMALS(frame,b_frame):
    global var1
    global score
    lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
    lable.grid(row=1,column=1,padx=20,pady=20)
    lable.config(font=("Courier", 25))
    R1=Radiobutton(b_frame,text="TIGER",variable=var1,value=1)
    R1.grid(row=2,column=1,padx=20,sticky=W)
    R1.config(font=("Courier", 15))
    R2=Radiobutton(b_frame,text="ELEPHANT",variable=var1,value=2)
    R2.grid(row=3,column=1,padx=20,sticky=W)
    R2.config(font=("Courier", 15))
    R3=Radiobutton(b_frame,text="RABBIT",variable=var1,value=3)
    R3.grid(row=4,column=1,padx=20,sticky=W)
    R3.config(font=("Courier", 15))
    R4=Radiobutton(b_frame,text="PUPPY",variable=var1,value=4)
    R4.grid(row=5,column=1,padx=20,sticky=W)
    R4.config(font=("Courier", 15))
    R5=Radiobutton(b_frame,text="LION",variable=var1,value=5)
    R5.grid(row=6,column=1,padx=20 ,sticky=W)
    R5.config(font=("Courier", 15))
    R6=Radiobutton(b_frame,text="WHITE PANDA",variable=var1,value=6)
    R6.grid(row=7,column=1,padx=20 ,sticky=W)
    R6.config(font=("Courier", 15))
    B=Button(b_frame,text="suubmit",command=lambda:check(frame,b_frame))
    B.grid(row=8,column=1,padx=20,pady=10)
    B.config(font=("Courier", 15))
    lable2=Label(b_frame,text="total Score")
    lable2.grid(row=9,column=1,padx=10)
    lable2.config(font=("Courier", 30))
    s=str(score)
    lable3=Label(b_frame,text=s)
    lable3.grid(row=9,column=2)
    lable3.config(font=("Courier", 30))
    
def main():
    global root
    global var1
    frame=Frame(root,height=400,width=500)
    frame.pack(side=LEFT,fill=BOTH)
    b_frame=Frame(root,height=400,width=500)
    b_frame.pack(side=RIGHT,fill=BOTH)
    if(x==1):
        gifl=PhotoImage(master=frame,file="1814.gif",height=400,width=500)
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=0,rowspan=8,padx=20,pady=20)
        buttons_FLOWERS(frame,b_frame)
    elif(x==2):
        gifl=PhotoImage(master=frame,file="li21.gif",height=400,width=500)
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_FLOWERS(frame,b_frame)
    elif(x==3):
        gifl=PhotoImage(master=frame,file="Bellis_perennis_white_(aka).gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_FLOWERS(frame,b_frame)
    elif(x==4):
        gifl=PhotoImage(master=frame,file="PF_15_R102_MINIMAL_NOGYP_NOFERN_VA0038_W2_SQ.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_FLOWERS(frame,b_frame)
    elif(x==5):
        gifl=PhotoImage(master=frame,file="what-does-the-lotus-flower-mean_c705d4c6-b686-47fd-ac8c-5cc85c7ee4bf.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_FLOWERS(frame,b_frame)
    elif(x==6):
        gifl=PhotoImage(master=frame,file="australia_satin_bower_bird_bird_221260.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_BIRDS(frame,b_frame)
    elif(x==7):
        gifl=PhotoImage(master=frame,file="birds.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_BIRDS(frame,b_frame)
    elif(x==8):
        gifl=PhotoImage(master=frame,file="pigeons-04.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_BIRDS(frame,b_frame)
    elif(x==9):
        gifl=PhotoImage(master=frame,file="owl-05.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_BIRDS(frame,b_frame)
    elif(x==10):
        gifl=PhotoImage(master=frame,file="Peacock_Walking_600.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_BIRDS(frame,b_frame)
    elif(x==11):
        gifl=PhotoImage(master=frame,file="animals-background-7.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_ANIMALS(frame,b_frame)
    elif(x==12):
        gifl=PhotoImage(master=frame,file="aplive-african-watering-hole-cam.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_ANIMALS(frame,b_frame)
    elif(x==13):
        gifl=PhotoImage(master=frame,file="babyanimal_open.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_ANIMALS(frame,b_frame)
    elif(x==14):
        gifl=PhotoImage(master=frame,file="animals-4.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_ANIMALS(frame,b_frame)
    elif(x==15):
        gifl=PhotoImage(master=frame,file="animals-01.gif")
        lable1=Label(frame,image=gifl)
        lable1.grid(row=0,column=5,columnspan=2,pady=20,padx=20)
        buttons_ANIMALS(frame,b_frame)
    else:
        global score
        global x
    
        lable2=Label(frame,text="GAME OVER")
        lable2.grid(row=0,column=2 ,padx=50,pady=50)
        lable2.config(font=("Courier", 50))
        lable3=Label(frame,text="your score:")
        lable3.grid(row=3,column=2)
        lable3.config(font=("Courier", 30))
        s=str(score)
        lable4=Label(frame,text=s)
        lable4.grid(row=3,column=5,pady=50,padx=50)
        score=0
        x=15
        lable4.config(font=("Courier", 30))
        B=Button(frame,text="RETRY",bg="BLACK",fg="WHITE",width=20,command=lambda:main())
        B.grid(row=5,column=0 ,padx=50,pady=15)
        B1=Button(frame,text="EXIT",bg="BLACK",fg="WHITE",width=20)
        B1.grid(row=5,column=2 ,padx=50,pady=15)
        
    mainloop()
main()

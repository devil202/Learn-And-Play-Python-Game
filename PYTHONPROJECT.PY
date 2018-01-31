# KIDS GAME
from  Tkinter import * 
import tkMessageBox
import sqlite3
#global variables
x=1
NAME=""
user=""
root=Tk()
Name=StringVar()
root.geometry("1050x500+200+100")
top=Tk()
top.geometry("900x500+200+100")
top.title("user")
top.withdraw()
score=0
#root.title("play And Fun") 
root.resizable(0,0)
var1=IntVar()
def Playx(frame,canvas,scrollbar):
    canvas.pack_forget()
    scrollbar.pack_forget()
    Play(frame)
def play1(frame):
    frame.pack_forget()
    play()
def get_name(entry,Name,frame):
    global NAME
    conn=sqlite3.connect('game1.db')
    c=conn.cursor()
    NAME=entry.get()
    c.execute('select * from user where name=?;',[NAME])
    if(c.fetchall()==[]):
        c.execute('insert into user values(?,?);',(NAME,0))
        conn.commit()
    conn.close()
    frame.pack_forget()
    play()
def Play(frame1):
    root.withdraw()
    top.deiconify()
    frame1.pack_forget()
    frame=Frame(top,width=500,height=400)
    frame.pack()
    frame.config(background='SLATE GRAY')
    top.config(background='SLATE GRAY')
    label=Label(frame,text="Enter Your Name:")
    label.grid(row=0,column=2,pady=40,padx=10)
    label.config(font=("Courier", 30),background='SLATE GRAY')
    entry=Entry(frame,width=100,textvariable=Name)
    entry.grid(row=2,column=1,columnspan=5,padx=50,pady=50)
    B5=Button(frame,text="Enter",bg="BLACK",fg="WHITE" ,command=lambda:get_name(entry,Name,frame),width=30,padx=10,height=2)
    B5.grid(row=3,column=2,pady=10)
def play():
    global root
    top.withdraw()
    root.deiconify()
    def keep_zero(frame,b_frame):
        global x
        x=16
        frame.pack_forget()
        b_frame.pack_forget()
        main()
    #fuction to check correct ans
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
            tkMessageBox.showinfo("Result","CORRECT ANS")
            tkMessageBox.showwarning
            score+=10
        else:
             tkMessageBox.showinfo("Result","WRONG ANS")
             score-=4
        x=x+1
        frame.destroy()
        b_frame.destroy()
        main()
    #function for flowers option
    def buttons_FLOWERS(frame,b_frame):
        global var1
        global score
        lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
        lable.grid(row=1,column=0,pady=20,sticky=W)
        lable.config(font=("Courier", 25),background='MOCCASIN') 
        R1=Radiobutton(b_frame,text="LILY",variable=var1,value=1)
        R1.grid(row=2,column=0,padx=20,sticky=W)
        R1.config(font=("Courier", 15),background='MOCCASIN')
        R2=Radiobutton(b_frame,text="MARIGOLD",variable=var1,value=2)
        R2.grid(row=3,column=0,padx=20,sticky=W)
        R2.config(font=("Courier", 15),background='MOCCASIN')
        R3=Radiobutton(b_frame,text="SUNFLOWER",variable=var1,value=3)
        R3.grid(row=4,column=0,padx=20,sticky=W)
        R3.config(font=("Courier", 15),background='MOCCASIN')
        R4=Radiobutton(b_frame,text="LOTUS",variable=var1,value=4)
        R4.grid(row=5,column=0,padx=20,sticky=W)
        R4.config(font=("Courier", 15),background='MOCCASIN')
        R5=Radiobutton(b_frame,text="DAISY",variable=var1,value=5)
        R5.grid(row=6,column=0,padx=20 ,sticky=W)
        R5.config(font=("Courier", 15),background='MOCCASIN')
        R6=Radiobutton(b_frame,text="ROSE",variable=var1,value=6)
        R6.grid(row=7,column=0,padx=20 ,sticky=W)
        R6.config(font=("Courier", 15),background='MOCCASIN')
        B=Button(b_frame,text="Submit",command=lambda:check(frame,b_frame))
        B.grid(row=8,column=0,pady=10,sticky=W)
        B.config(font=("Courier", 15),background='DEEPSKYBLUE2')
        lable2=Label(b_frame,text="Total Score")
        lable2.grid(row=11,column=0,sticky=W)
        lable2.config(font=("Courier", 30),background='MOCCASIN')
        s=str(score)
        lable3=Label(b_frame,text=s)
        lable3.grid(row=11,column=1,sticky=W)
        lable3.config(font=("Courier", 30),background='MOCCASIN')
        B1=Button(b_frame,text="END GAME",command=lambda:keep_zero(frame,b_frame))
        B1.grid(row=8,column=0,pady=10,sticky=E)
        B1.config(font=("Courier", 15),background='DEEPSKYBLUE2')

    def buttons_BIRDS(frame,b_frame):
        global var1
        global score
        lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
        lable.grid(row=1,column=0,pady=20,sticky=W)
        lable.config(font=("Courier", 25),background='MOCCASIN')
        R1=Radiobutton(b_frame,text="PEACOCK",variable=var1,value=1)
        R1.grid(row=2,column=0,padx=20,sticky=W)
        R1.config(font=("Courier", 15),background='MOCCASIN')
        R2=Radiobutton(b_frame,text="OWL",variable=var1,value=2)
        R2.grid(row=3,column=0,padx=20,sticky=W)
        R2.config(font=("Courier", 15),background='MOCCASIN')
        R3=Radiobutton(b_frame,text="PEGION",variable=var1,value=3)
        R3.grid(row=4,column=0,padx=20,sticky=W)
        R3.config(font=("Courier", 15),background='MOCCASIN')
        R4=Radiobutton(b_frame,text="SPARROW",variable=var1,value=4)
        R4.grid(row=5,column=0,padx=20,sticky=W)
        R4.config(font=("Courier", 15),background='MOCCASIN')
        R5=Radiobutton(b_frame,text="CROW",variable=var1,value=5)
        R5.grid(row=6,column=0,padx=20 ,sticky=W)
        R5.config(font=("Courier", 15),background='MOCCASIN')
        R6=Radiobutton(b_frame,text="KINGFISHER",variable=var1,value=6)
        R6.grid(row=7,column=0,padx=20 ,sticky=W)
        R6.config(font=("Courier", 15),background='MOCCASIN')
        B=Button(b_frame,text="Submit",command=lambda:check(frame,b_frame))
        B.grid(row=8,column=0,padx=20,pady=10,sticky=W)
        B.config(font=("Courier", 15),background='DEEPSKYBLUE2')
        lable2=Label(b_frame,text="Total Score")
        lable2.grid(row=11,column=0,sticky=W)
        lable2.config(font=("Courier", 30),background='MOCCASIN')
        s=str(score)
        lable3=Label(b_frame,text=s)
        lable3.grid(row=11,column=1,sticky=W)
        lable3.config(font=("Courier", 30),background='MOCCASIN')
        B1=Button(b_frame,text="END GAME",command=lambda:keep_zero(frame,b_frame))
        B1.grid(row=8,column=0,pady=10,sticky=E)
        B1.config(font=("Courier", 15),background='DEEPSKYBLUE2')

    def buttons_ANIMALS(frame,b_frame):
        global var1
        global score
        lable=Label(b_frame,text="CHOOSE THE CORRECT OPTION")
        lable.grid(row=1,column=0,pady=20,sticky=W)
        lable.config(font=("Courier", 25),background='MOCCASIN')
         
        R1=Radiobutton(b_frame,text="TIGER",variable=var1,value=1)
        R1.grid(row=2,column=0,sticky=W)
        R1.config(font=("Courier", 15),background='MOCCASIN')
        R2=Radiobutton(b_frame,text="ELEPHANT",variable=var1,value=2)
        R2.grid(row=3,column=0,sticky=W)
        R2.config(font=("Courier", 15),background='MOCCASIN')
        R3=Radiobutton(b_frame,text="RABBIT",variable=var1,value=3)
        R3.grid(row=4,column=0,sticky=W)
        R3.config(font=("Courier", 15),background='MOCCASIN')
        R4=Radiobutton(b_frame,text="PUPPY",variable=var1,value=4)
        R4.grid(row=5,column=0,sticky=W)
        R4.config(font=("Courier", 15),background='MOCCASIN')
        R5=Radiobutton(b_frame,text="LION",variable=var1,value=5)
        R5.grid(row=6,column=0 ,sticky=W)
        R5.config(font=("Courier", 15),background='MOCCASIN')
        R6=Radiobutton(b_frame,text="WHITE PANDA",variable=var1,value=6)
        R6.grid(row=7,column=0,sticky=W)
        R6.config(font=("Courier", 15),background='MOCCASIN')
        B=Button(b_frame,text="Submit",command=lambda:check(frame,b_frame))
        B.grid(row=8,column=0,pady=10,sticky=W)
        B.config(font=("Courier", 15),background='DEEPSKYBLUE2')
        lable2=Label(b_frame,text="Total Score")
        lable2.grid(row=13,column=0,sticky=W)
        lable2.config(font=("Courier", 30),background='MOCCASIN')
        s=str(score)
        lable3=Label(b_frame,text=s)
        lable3.grid(row=13,column=1,sticky=W)
        lable3.config(font=("Courier", 30),background='MOCCASIN')
        B1=Button(b_frame,text="END GAME",command=lambda:keep_zero(frame,b_frame))
        B1.grid(row=8,column=0,pady=10,sticky=E)
        B1.config(font=("Courier",15),background='DEEPSKYBLUE2')
     #main function for gui   
    def main():
        global root
        global var1
        global x
        frame=Frame(root,height=400,width=525)
        frame.pack(side=LEFT,fill=BOTH)
        frame.config(background='MOCCASIN')
        b_frame=Frame(root,height=400,width=525)
        b_frame.pack(side=RIGHT,fill=BOTH)
        b_frame.config(background='MOCCASIN')
        root.config(background='MOCCASIN')
        if(x==1):
            gifl=PhotoImage(master=frame,file="1814.gif")
            lable1=Label(frame,image=gifl)
            lable1.grid(row=0,column=0,rowspan=8,padx=20,pady=20)
            buttons_FLOWERS(frame,b_frame) 
        elif(x==2):
            gifl=PhotoImage(master=frame,file="li21.gif")
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
            high_score()
            frame.pack_forget()
            b_frame.pack_forget()
            root.withdraw()
            top.deiconify()
            top.title("Game Over!")
            frame=Frame(top)
            frame.pack()
            lable2=Label(frame,text="GAME OVER")
            lable2.grid(row=0,column=2 ,padx=30,pady=50)
            lable2.config(font=("Courier", 50))
            lable3=Label(frame,text="your score:")
            lable3.grid(row=3,column=2)
            lable3.config(font=("Courier", 30))
            s=str(score)
            lable4=Label(frame,text=s)
            lable4.grid(row=3,column=3,pady=50,padx=50)
            score=0
            x=1
            lable4.config(font=("Courier", 30))
            B=Button(frame,text="RETRY",bg="BLACK",fg="WHITE",width=20,command=lambda:play1(frame))
            B.grid(row=6,column=0 ,padx=50,pady=15)
            B1=Button(frame,text="EXIT",bg="BLACK",fg="WHITE",width=20,command=lambda:Quit())
            B1.grid(row=6,column=3 ,padx=50,pady=15)
            B2=Button(frame,text="High Scores",fg="white",bg="BLACK", width=20,command=lambda:High_score(frame))
            B2.grid(row=6,column=2)
        mainloop()
    
    main()

    
 #to display high scores   
def high_score():
    global score
    conn=sqlite3.connect('game1.db')
    c=conn.cursor()
    c.execute('select high_score from user where name=?',[NAME])
    x=c.fetchall()
    conn.close()
    conn=sqlite3.connect('game1.db')
    c=conn.cursor()
    if((score,)>x[0]):
        c.execute('update user set high_score=? where name=?',(score,NAME))
        conn.commit()
    conn.close()
    return
def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
def High_score(frame):
    top.withdraw()
    root.deiconify()
    frame.pack_forget()
    canvas = Canvas(root,borderwidth=0)
    frame=Frame(canvas,width=900,height=500)
    scrollbar=Scrollbar(root,orient="vertical")
    canvas.configure(yscrollcommand=scrollbar.set)
    #text_area=Text(frame,width=900,height=500,yscrollcommand=scrollbar.set)
    scrollbar.config(command=canvas.yview)
    scrollbar.pack(side="right",fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0,0), window=frame, anchor="nw",tags="frame")
    #canvas.configure(scrollregion=canvas.bbox("all"))
    #text_area.pack(side="left",fill="both",expand=True)
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    root.resizable(1,1)
    canvas.config(background="BLACK")
    frame.config(background="BLACK")
    root.config(background="BLACK")
    conn=sqlite3.connect('game1.db')
    c=conn.cursor()
    c.execute('select * from user')
    name=Label(frame,text="NAME",fg="WHITE")
    name.grid(row=0,column=0,padx=150,pady=10,sticky=W)
    name.config(background="BLACK",font=("Courier",20))
    high=Label(frame,text="High Score",fg="WHITE")
    high.grid(row=0,column=4,pady=10,sticky=W)
    high.config(background="BLACK",font=("Courier",20))
    i=1
    p=c.fetchone()
    while(p):
        name=Label(frame,text=p[0],fg="WHITE")
        name.grid(row=i,column=0,padx=150,pady=10,sticky=W)
        name.config(background="BLACK",font=("Courier",20))
        high=Label(frame,text=str(p[1]),fg="WHITE")
        high.grid(row=i,column=4,pady=10,sticky=W)
        high.config(background="BLACK",font=("Courier",20))
        p=c.fetchone()
        i+=1
    conn.close()
    B2=Button(frame,text="P L A Y",fg="BLACK",bg="green", height="2", width=15,command=lambda:Playx(frame,canvas,scrollbar))
    B2.grid(row=2000,column=0,pady=5)
    B2.config(font=("Courier",10)) 
    command=lambda:Quit()
    B3=Button(frame,text="Q u i t",fg="BLACK",bg="green", height="2", width="15",command=command)
    B3.grid(row=2000,column=4,pady=5,sticky=W)
    B3.config(font=("Courier",10))
    conn.close()
#for quit option()
def Quit():
   root.destroy()
   top.destroy()
#for the first page
def welcome():
    root.title("LEARN AND PLAY")
    root.resizable(0,0)
    frame1=Frame(root,height=500,width=1000)
    frame1.pack()
    frame1.pack_propagate(False)
    frame1.config(background='DARK SLATE GRAY')
    command=lambda:Play(frame1)
    B1=Button(frame1,text="P L A Y" ,fg="white",bg="BLACK", height="10", width="100",command=command)
    B1.pack(anchor=CENTER,pady=10)
    B1.config(font=("Courier",10))
    B2=Button(frame1,text="H i g h  S c o r e s",fg="white",bg="BLACK", height="10", width="100",command=lambda:High_score(frame1))
    B2.pack()
    B2.config(font=("Courier",10))
    command=lambda:Quit()
    B3=Button(frame1,text="Q u i t",fg="white",bg="BLACK", height="10", width="100",command=command)
    B3.pack(pady=10)
    B3.config(font=("Courier",10))
    mainloop()
welcome()

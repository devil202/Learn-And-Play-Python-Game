from Tkinter import*
root =Tk()
photo=PhotoImage(master=root,file="animals-4.gif")
label=Label(root,image=photo)
label.grid(row=0,column=0,padx=50,pady=50,rowspan=2)
mainloop()

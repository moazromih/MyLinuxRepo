from tkinter import * 

username = StringVar()
password = StringVar()

top = Tk()

L1 = Label(top,text= 'Username',font=('calibre',15,'bold')).grid(row=0,column=0)

E1 = Entry(top,bd = 5,font=('calibre',10,'normal')).grid(row=0,column=1,textvariable= username)

L2 = Label(top,text= 'Password',font=('calibre',15,'bold')).grid(row=1,column=0)

E2 = Entry(top,bd = 5,show='*',font=('calibre',10,'normal'),textvariable= password).grid(row=1,column=1)

top.mainloop()
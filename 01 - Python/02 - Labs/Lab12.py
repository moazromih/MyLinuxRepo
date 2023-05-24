from tkinter import *

def Masr():
    label_1 =Label(window_1, text= "تحيامصر!")
    label_1.pack(side= TOP)

window_1 = Tk()

window_1.title("Hello From Tkinter.")
window_1.geometry("1000x1000")
label_1 =Label(window_1, text= "Name: Moaz")
label_1.pack(side= TOP)

label_1 =Label(window_1, text= "Age: 24")
label_1.pack(side= TOP)

label_1 =Label(window_1, text= "Major: ECE")
label_1.pack(side= TOP)

photo_1 = PhotoImage(file= "syadet-elrys.png")
photo_1 = photo_1.subsample(2,2)

label_1 =Button(window_1, text= "Like!", command= Masr , bd = 5,image=photo_1)
label_1.pack(side= TOP)

label_1 =Button(window_1, text= "Like!",fg= 'white',bg='lightblue',bd = 5)
label_1.pack(side= LEFT)

label_1 =Button(window_1, text= "Like!",fg= 'white',bg='lightblue',bd = 5)
label_1.pack(side= RIGHT)

label_1 =Button(window_1, text= "Close",command= window_1.destroy, bd= 10)
label_1.pack(side= BOTTOM)


window_1,mainloop()
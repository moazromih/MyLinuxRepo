
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y




import tkinter as tk
root = tk.Tk()

entry = tk.Entry(root).grid(row =10,column=10)

# Disable the widget
entry.config(state='disabled')

Result = tk.Entry(root,text="ResultHere",width= 48).grid(row=0, column=0, columnspan= 4)
tk.Button(text="", bg="#DFFF00", fg="black", width=10).grid(row=2, column=0)
tk.Button(text="", bg="#EFFF00", fg="black", width=10).grid(row=2, column=1)
tk.Button(text="", bg="#EFFF00", fg="black", width=10).grid(row=2, column=2)
tk.Button(text="", bg="#EFFF00", fg="black", width=10).grid(row=2, column=3)
tk.Button(text="", bg="#00F000", fg="black", width=10).grid(row=3, column=0)
tk.Button(text="", bg="#FAEF00", fg="black", width=10).grid(row=3, column=1)
tk.Button(text="", bg="#FFFF00", fg="black", width=10).grid(row=4, column=0)
tk.Button(text="0", bg="#FFFF00", fg="black", width=10).grid(row=4, column=1)
tk.Button(text="1", bg="#AAAF00", fg="black", width=10).grid(row=5, column=0)
tk.Button(text="2", bg="#FFFF00", fg="black", width=10).grid(row=5, column=1)
tk.Button(text="3", bg="#CCCE00", fg="black", width=10).grid(row=6, column=0)
tk.Button(text="4", bg="#FFFF00", fg="black", width=10).grid(row=6, column=1)
tk.Button(text="5", bg="#FFFF00", fg="black", width=10).grid(row=7, column=0)
tk.Button(text="6", bg="#FFFF00", fg="black", width=10).grid(row=7, column=1)
tk.Button(text="7", bg="#FFFF00", fg="black", width=10).grid(row=8, column=0)
tk.Button(text="8", bg="#FFFF00", fg="black", width=10).grid(row=8, column=1)
tk.Button(text="9", bg="#FFFF00", fg="black", width=10).grid(row=9, column=0)
tk.Button(text="0", bg="#FFFF00", fg="black", width=10).grid(row=9, column=1)

root.mainloop()
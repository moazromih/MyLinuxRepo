
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y


pressedNum = 1
finalResult = 0
operator = ''
num1 = ''
num2 = ''

def resetCalc():
    global pressedNum
    global finalResult
    global operator
    global num1
    global num2
    pressedNum = 1
    finalResult = 0
    operator = ''
    num1 = ''
    num2 = ''
    Result.config(state= 'normal')
    Result.delete('1.0','end')
    Result.config(state= 'disabled')

def pressNum(x):
    global num1
    global num2
    Result.config(state= 'normal')
    Result.insert('end',x)
    if (pressedNum == 1):
        num1 += x
    elif (pressedNum == 2):
        num2 += x
    print(num1,num2)
    Result.config(state= "disabled")

def pressOp(x):
    global pressedNum
    global num1
    global num2
    global finalResult
    global operator
    operator = x
    Result.config(state= 'normal')
    Result.insert('end'," {} ".format(x))
    pressedNum = 2
    Result.config(state= "disabled")




def pressEqual():
    global pressedNum
    global finalResult
    Result.config(state= 'normal')
    pressedNum = 1
    print(num1,operator,num2)
    if operator == '+':
        finalResult = add(float(num1),float(num2))
    elif operator == '-':
        finalResult = sub(float(num1),float(num2))
    elif operator == '*':
        finalResult = mult(float(num1),float(num2))
    elif operator == '/':
        finalResult = div(float(num1),float(num2))
    Result.insert('end',' = ')
    Result.insert('end',str(finalResult))
    Result.config(state= "disabled")



myFont = ("Comic Sans MS", 10, "bold")



import tkinter as tk

root = tk.Tk()



Result = tk.Text(root,font= myFont, height=3, width= 40,border=10)
Result.grid(row=0, column=0, columnspan= 4)
Result.config(state= "disabled")



button_7 = tk.Button(font= myFont, text="7" ,border= 5,height= 2, width=10, command= lambda : pressNum('7'))
button_7.grid(row=1, column=0)
button_8 = tk.Button(font= myFont, text="8" ,border= 5,height= 2, width=10, command= lambda : pressNum('8'))
button_8.grid(row=1, column=1)
button_9 = tk.Button(font= myFont, text="9" ,border= 5,height= 2, width=10, command= lambda : pressNum('9'))
button_9.grid(row=1, column=2)
button_add = tk.Button(font= myFont, text="+", border= 5, height= 2, width= 10, command= lambda : pressOp('+'))
button_add.grid(row=1, column=3)
button_4 = tk.Button(font= myFont, text="4" ,border= 5,height= 2, width=10, command= lambda : pressNum('4'))
button_4.grid(row=2, column=0)
button_5 = tk.Button(font= myFont, text="5" ,border= 5,height= 2, width=10, command= lambda : pressNum('5'))
button_5.grid(row=2, column=1)
button_6 = tk.Button(font= myFont, text="6" ,border= 5,height= 2, width=10, command= lambda : pressNum('6'))
button_6.grid(row=2, column=2)
button_sub = tk.Button(font= myFont, text="-", border= 5, height= 2, width= 10, command= lambda : pressOp('-'))
button_sub.grid(row=2, column=3)
button_1 = tk.Button(font= myFont, text="1" ,border= 5,height= 2, width=10, command= lambda : pressNum('1'))
button_1.grid(row=3, column=0)
button_2 = tk.Button(font= myFont, text="2" ,border= 5,height= 2, width=10, command= lambda : pressNum('2'))
button_2.grid(row=3, column=1)
button_3 = tk.Button(font= myFont, text="3" ,border= 5,height= 2, width=10, command= lambda : pressNum('3'))
button_3.grid(row=3, column=2)
button_mult = tk.Button(font= myFont, text="*", border= 5, height= 2, width= 10, command= lambda : pressOp('*'))
button_mult.grid(row=3, column=3)
button_0 = tk.Button(font= myFont, text="0" ,border= 5,height= 2, width=10, command= lambda : pressNum('0'))
button_0.grid(row=4, column=0)
button_dot = tk.Button(font= myFont, text="." ,border= 5,height= 2, width=10, command= lambda : pressNum('.'))
button_dot.grid(row=4, column=1)
button_equal = tk.Button(font= myFont, text="=" ,border= 5,height= 2, width=10, command= pressEqual)
button_equal.grid(row=4, column=2)
button_div = tk.Button(font= myFont, text="/" ,border= 5,height= 2, width=10, command= lambda : pressOp('/'))
button_div.grid(row=4, column=3)
button_reset = tk.Button(font= myFont, text="Reset" ,border= 5,height= 2, width=45, command= resetCalc)
button_reset.grid(row=5, column=0,columnspan= 4)





root.mainloop()
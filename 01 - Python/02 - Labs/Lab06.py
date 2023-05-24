UserInput = int(input("Enter 1 to display isdecimal() Function or 2 to display istitle() Fucntion: "))

if UserInput == 1:
    print('''Check if all the characters in a string are decimals (0-9):
    txt = "1234"

    x = txt.isdecimal()

    print(x)''')
    print("",end='    ')
    print("1234".isdecimal())
elif UserInput == 2:
    print('''Check if each word start with an upper case letter: 
    txt = "Hello, And Welcome To My World!"

    x = txt.istitle()

    print(x)''')
    print("",end='    ')
    print("Hello, And Welcome To My World!".istitle())
else:
    print("Invalid Input.")
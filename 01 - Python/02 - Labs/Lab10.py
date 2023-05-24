def add(a,b):
    return a+b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def sub(a,b):
    return a-b

myHistory = open("History.txt","r")
operationID = int(myHistory.readline(1))
myHistory = open("History.txt","a+")

while True:
    operation = input("Please enter the operation: ").split()
    if(operation[0] == "close"):
        myHistory = open("History.txt","r")
        newFile = myHistory.readlines()
        newFile[0] = str(operationID)+'\n'
        myHistory = open("History.txt","w")
        myHistory.writelines(newFile)
        myHistory.close()
        
    elif(operation[1] == '-'):
        operationID += 1
        result = sub(int(operation[0]),int(operation[2]))
    elif(operation[1] == '*'):
        operationID += 1
        result = mult(int(operation[0]),int(operation[2]))
    elif(operation[1] == '/'):
        operationID += 1
        result = div(int(operation[0]),int(operation[2]))
    elif(operation[1] == '+'):
        operationID += 1
        result = add(int(operation[0]),int(operation[2]))
    else:
        print("Invalid operator")


    myHistory.write("Operation "+str(operationID)+": "+" ".join(operation)+" = "+str(result)+"\n")
    

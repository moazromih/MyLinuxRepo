name = input("Please, Enter your name: ")
age = input("Please, Enter your age: ")
major = input("Please, Enter your major: ")

MyText = open("MyText.txt","a+")
MyText.write("Name: "+name+"\n")
MyText.write("Age: "+age+"\n")
MyText.write("Major: "+major+"\n")

MyText = open("MyText.txt","r")
print(MyText.read())

MyText.close()

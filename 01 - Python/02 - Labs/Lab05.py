my_list = [int(a) for a in input("Please enter 5 numbers: ").split()]

check = int(input("Enter the number to check for: "))
if check in my_list:
    print("Yes, it exists.")
else:
    print("No, it doesn't exist")
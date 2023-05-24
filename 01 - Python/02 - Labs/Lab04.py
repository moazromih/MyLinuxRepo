'''
    Define the dict/list
'''
my_dict = {"Sensor1" : 0,"Sensor2" : 0,"Sensor3" : 0}
my_list = []

'''
    Ask for input
'''
my_dict["Sensor1"] = int(input("Enter Sensor 1 Reading : "))
my_dict["Sensor2"] = int(input("Enter Sensor 2 Reading : "))
my_dict["Sensor3"] = int(input("Enter Sensor 3 Reading : "))

my_list.append(my_dict["Sensor1"])
my_list.append(my_dict["Sensor2"])
my_list.append(my_dict["Sensor3"])

my_tuple = (my_list[0],my_list[1],my_list[2])


'''
    Print the values
'''
print("Dictionary :", my_dict)
print("List :", my_list)
print("Tuple :", my_tuple)

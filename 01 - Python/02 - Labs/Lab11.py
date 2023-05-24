import csv

Data = csv.reader(open('names.csv','r+'))

dict_1 = {}

for line in Data:
    dict_1[line[0]] = {'age':line[1], 'major': line[2]}

print(dict_1)
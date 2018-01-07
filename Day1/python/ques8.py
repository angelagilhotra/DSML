#read an input file containing names, roll numbers and marks of 10 students. Each student's details are present in single line separated by comma. After reading the ocntents from the file store in a list of dictionary objects variable
import csv
f = open ("students.txt", "r")
dict = {}
list_of_dict = []
for row in csv.reader(f):
	dict['name'] = row[0]
	dict['rollno'] = row[1]
	dict['marks'] = row[2]
	list_of_dict.append(dict.copy())
f.close()

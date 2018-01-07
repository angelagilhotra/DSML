#randomly change marks of students and store them in a file with details of each student in a single line
import ques8
num = raw_input("Enter a random number from 0 to 9 ")
num2 = raw_input("what would you like to change the marks to? ")
print (ques8.list_of_dict[int(num)]['marks'])
ques8.list_of_dict[int(num)]['marks'] = num2
print "updated marks: "
print (ques8.list_of_dict[int(num)]['marks'])

f = open("students-edited.txt", "w")


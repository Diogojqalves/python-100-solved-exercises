"""
2.13 - Consider that you have the number of students (N) in a course, the list of marks obtained by these students 
in a discipline and the list of numbers of the class to which they belong. Calculate the arithmetic mean of 
the marks obtained by the students in each class. 
(Note: Consider that there is no more than 6 classes) 
Ex: Number of students: 10 
class  1  2  1  3  1  3  3  2  2  3
marks 12 13 10 10 14 16 12 10 10 14
Class
3 13
2 11
1 12
R : Class Mean
"""
from random import randint

n = 0

while n <= 0:
    n = int(input("Enter the number of students: "))
    if n <= 0:
        print("Warning: The number of studentes must be greate rthan zero. Try again.")

list_of_classes = []
list_of_marks = []

for x in range(n):
    list_of_marks.append(randint(0, 20))
    list_of_classes.append(randint(1, 6))

print("Classes:", list_of_classes)
print("Marks:", list_of_marks)

larger_class_number = max(list_of_classes)
print("Class")
for class_number in range(1, larger_class_number + 1):
    arithmetic_mean = 0.0
    number_of_marks = 0
    if class_number in list_of_classes:
        for x in range(len(list_of_marks)):
            if list_of_classes[x] == class_number:
                number_of_marks += 1
                arithmetic_mean += list_of_marks[x]

    if number_of_marks != 0:
        arithmetic_mean = arithmetic_mean // number_of_marks
        print("%d: %d" % (class_number, arithmetic_mean))

  


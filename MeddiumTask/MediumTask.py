grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = list(students)

sorted(list_students)


a = sum(grades[0])
a2 = len(grades[0])
b = sum(grades[1])
b2 = len(grades[1])
c = sum(grades[2])
c2 = len(grades[2])
d = sum(grades[3])
d2 = len(grades[3])
e = sum(grades[4])
e2 = len(grades[4])

average = {
    list_students[0] : a/a2,
    list_students[1] : b/b2,
    list_students[2] : c/c2,
    list_students[3] : d/d2,
    list_students[4] : e/e2
        }

print(average)

name_of_student = input('Write name of your student: ')
print(average[name_of_student])












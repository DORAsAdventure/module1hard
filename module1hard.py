grades = [[5, 3, 3, 5, 4] , [2, 2, 2, 3] , [4, 5, 5, 2] , [4, 4, 3] , [5, 5, 5, 4, 5]]
students = {'Johnny' , 'Bilbo' , 'Steve' , 'Khendrik' , 'Aron'}
students = sorted(list(students))
#print(students)
average_grades = [sum(i) / len(i) for i in grades]
#print(average_grades)
student_journal = dict(zip(students, average_grades))
print(student_journal)
#print(tudent_journal ['Aron'])
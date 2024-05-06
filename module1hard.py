Grades=[[5, 3, 3, 5, 4],[2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],[5, 5, 5, 4, 5]]
Students={'Johnny','Bilbo','Steve','Khendrik','Aron'}
Students=sorted(list(Students))
#print(Students)
Avg_Aron=(sum(Grades[0])/len(Grades[0]))
Avg_Bilbo=(sum(Grades[1])/len(Grades[1]))
Avg_Johnny=(sum(Grades[2])/len(Grades[2]))
Avg_Khendrik=(sum(Grades[3])/len(Grades[3]))
Avg_Steve=(sum(Grades[4])/len(Grades[4]))
Student_journal={'Aron':Avg_Aron, 'Bilbo':Avg_Bilbo, 'Johnny':Avg_Johnny,'Khendrik':Avg_Khendrik,'Steve':Avg_Steve}
print(Student_journal)
#ИЛИ МОЖЕТ ТАК
#Grades=[Avg_Aron, Avg_Bilbo, Avg_Johnny, Avg_Khendrik, Avg_Steve]
#Student_journal1=dict(zip(Students,Grades))
#print(Student_journal1)
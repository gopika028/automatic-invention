student={'name':'','class':'','marks':{'math':0,'science':0,'english':0}}
student['name']=input('Enter the student name:')
student['class']=input('Enter the student class:')
student['marks']['math']=float(input('Enter the student math marks:'))
student['marks']['science']=float(input('Enter the student science marks:'))
student['marks']['english']=float(input('Enter the student english marks:'))
total_marks=sum(student['marks'].value())
percentage=total_marks/300*100
percentage=round(percentage,2)
print("\n\n*****STUDENT MARKSHEET*****")
print('name of the student:',student['Name'])
print('class of the student:',student['class'])
print('math marks:',student['marks']['math'])
print('science marks:',student['marks']['science'])
print('english marks:',student['marks']['english'])
print('Total marks:',total_marks)
print('percentage:',percentage)
print("**********")                                        
                                                                 
                             
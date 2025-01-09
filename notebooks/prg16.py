name=input('Enter the employee \'s name:')
id_number=input('Enter the employee \'s id:')
position=input('enter position:')
monthly_salary=float(input('Enter the employee \'s monthly salary:'))
employee=(name,id_number,position,monthly_salary)
gross_pay=employee[3]*12
pf=gross_pay*0.1
net_pay=gross_pay
print('Name:',employee[0])
print('ID:',employee[1])
print('position:',employee[2])
print('Monthly salary:',employee[3])
print('Gross pay:',gross_pay)
print('PF:',pf)
print('Net pay:',net_pay)
print("****************")
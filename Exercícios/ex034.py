salary = float(input('\nType your salary: '))
print(20*'-')
if salary <= 1250:
   print('Congratulations! your new salary is R${:.2f}.'.format(salary * 1.15))
else:
   print('Congratulations! your new salary is R${:.2f}'.format(salary * 1.10))
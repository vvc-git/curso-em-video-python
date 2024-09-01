print('-'*20)
print('BUYING A NEW HOUSE...')
print('-'*20)
house = float(input('How much does the house cost? R$'))
salary = float(input('What is your salary? R$'))
time = float(input('How long do you plan to pay the house? '))
installment = (house/(time*12))
if installment <= 0.30*salary:
   print('Congratulations! you can buy a new house for {}R${:.2f}{} per month'.format('\033[1;35m', installment, '\033[m'))
else:
   print("I'm sorry, your salary is too low for an installment of {}R${:.2f}{} per month".format('\033[1;35m', installment, '\033[m'))

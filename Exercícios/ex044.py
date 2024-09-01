price = float(input('\nHow much the product cost? '))
way = str(input('What is the way of payment?\na) Money or Cheque\nb) In cash\nc) Pay in two installments\nd) Pay in three or more installments over\n--> ')).upper().strip()
print(68*'-')
if way == 'A' or way == 'MONEY' or way == 'CHEQUE':
   print('Great! You have a discount of 10%. So you only have to pay R${}{:.2f}{}!'.format('\033[1;32m', 0.9*price, '\033[m'))
elif way == 'B' or way == 'IN CASH' or way == 'CASH':
   print('Great! You have a discount of 5%. So you only have to pay R${}{:.2f}{}!'.format('\033[1;33m', 0.95*price, '\033[m'))
elif way == 'PAY IN TWO INSTALLMENTS' or way == '2' or way == 'TWO' or way == 'C':
   print('Ok, each installment will be R${}{:.2f}'.format('\033[1;34m', price/2))
else:
   intallments = int(input('How many intallments do you want? '))
   nprice = 1.20*price
   print('The final price is R${}{:.2f}{} and each installment will be R${}{:.2f}'.format('\033[1;35m', nprice, '\033[m', '\033[1;35m', (nprice/intallments)))

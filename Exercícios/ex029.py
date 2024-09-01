v = float(input('\nWhat was your velocity? '))
print(20*'-')
if v<=80:
   print('Ok, no problem.')
else:
   print('You were too fast! Your fine is R${:.2f}. '.format((v-80)*7))

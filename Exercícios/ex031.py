dist = float(input('\nType the distance: '))
print(25*'=')
if dist <= 200:
   print('Your ticket costs R${}'.format(0.5*dist))
else:
   print('Your ticket costs R${:.2f}'.format(0.45*dist))


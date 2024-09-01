weigh = float(input('\nHow much do you weigh? (KG) '))
height = float(input('How tall are you? (m) '))
imc = weigh / (height ** 2)
print(20*'-')
print('[Your IMC]: {:.1f}'.format(imc))
if imc < 18.5:
   print('You are {}underweight'.format('\033[1;31m'))
elif 18.5 <= imc < 25:
   print("Don't worry! this is the ideal weight")
elif 25 <= imc < 30:
   print('You are {}overweight'.format('\033[1;31m'))
elif 30 <= imc < 40:
   print('You are {}obese'.format('\033[1;31m'))
else:
   print('You are {}morbidly obese'.format('\033[1;31m'))
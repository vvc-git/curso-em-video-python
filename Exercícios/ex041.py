from datetime import date
print('-'*32)
print('VERIFIQUE A SUA CATEGORIA ABAIXO:')
print('-'*32)
year = int(input('Em que ano você nasceu? '))
age = date.today().year - year
print('\nVocê tem {} anos. Então, '.format(age),end='')
if age <= 9:
   print('você é {}MIRIM'.format('\033[1;31m'))
elif 9 < age <= 14:                                         #poderia ser apenas "age<=14", pois se nao for menor que 9. entao ele desce
   print('você é {}INFANTIL'.format('\033[1;32m'))
elif 14 < age <= 19:
   print('você é {}JUNIOR'.format('\033[1;33m'))
elif 19 < age <=20:
   print('você é {}SENIOR'.format('\033[1;34m'))
else:
   print('você é {}MASTER'.format('\033[1;35m'))
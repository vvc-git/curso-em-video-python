print(20*'-')
print('{}Which one is bigger?{}'.format('\033[1;33;41m', '\033[m'))
print(20*'-')
x = int(input('Type a number: '))
y = int(input('Type another number: '))
print('\n')
if x > y:
   print('{}{}{} is bigger than {}{}{}'.format('\033[1;33m', x, '\033[m', '\033[1;31m', y, '\033[m'))
elif x < y:
   print('{}{}{} is bigger than {}{}{}'.format('\033[1;33m', y, '\033[m', '\033[1;31m', x, '\033[m'))
else:
   print('{}{}{} is equal {}{}{}'. format('\033[1;33m', x, '\033[m', '\033[1;33m', y, '\033[m' ))
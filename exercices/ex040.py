print('-*-'*6)
print('{}CHECK YOUR SCORE{}'.format('\033[1;36m','\033[m'))
print('-*-'*6)


t1 = float(input('[T1]: '))
t2 = float(input('[T2]: '))
average = (t1+t2)*0.5
if average < 5:
   print('\n{}{}{} is too low. You {}failed!{}'.format('\033[1;31m', average, '\033[m', '\033[1;31m', '\033[m'))
elif average > 7:
   print('\n{}{:.1f}{} is a great score! You are {}approved!{}'.format('\033[1;36m', average, '\033[m', '\033[1;36m', '\033[m'))
else:
   print('\n{}{:.1f}{} is your score. You are {}approved{}'.format('\033[1;34m', average, '\033[m', '\033[1;34m','\033[m'))

year = int(input('\nWhen were you born? '))
age = 2017 - year
print('=*='*12)
if age > 18:
   print('You are {} years now so you should be enlisted {}{}{} years before.'.format(age, '\033[1;35m', (age-18), '\033[m'))
elif age < 18:
   print('You are {} years now so you have to enlist in {}{}{} years'.format(age, '\033[1;36m', (18-age), '\033[m'))
else:
   print('You have to enlist this year!!!')
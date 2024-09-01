from datetime import datetime
plus = 0
for c in range (1, 8):
   born = int(input('{}.When did you born? '.format(c)))
   if (datetime.today().year - born) > 21:
      plus = plus + (c/c)
print('\n{:.0f} are twenty one.'.format(plus))
print("\n{:.0f} aren't twenty one.".format(7-plus))
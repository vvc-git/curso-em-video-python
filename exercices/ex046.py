from emoji import emojize
from time import sleep
for c in range(10, 0, -1):
   print('\n', c)
   sleep(1)
print(emojize('\n{}HAPPY NEW YEAR!!!{}:fireworks:'.format('\033[1;31m', '\033[m'), use_aliases=True))
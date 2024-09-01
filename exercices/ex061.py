
print('=' * 52)
print('THE FIRST TEN NUMBERS OF ANY ARITHMETIC PROGRESSION')
print('=' * 52)
a1 = int(input('Type the first term: '))
r = int(input('Type the common difference: '))
cont = 1

while cont <= 10:
   print(f'{a1}; ', end='')
   a1 += r
   cont += 1


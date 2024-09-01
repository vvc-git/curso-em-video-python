print('='*52)
print('THE FIRST TEN NUMBERS OF ANY ARITHMETIC PROGRESSION')
print('='*52)
a1 = int(input('Type the first term: '))
r = int(input('Type the common difference: '))
for t in range(1, 11):
   print('a{} = {}'.format(t, (a1+(t-1)*r)),end='; ')


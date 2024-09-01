x = int(input('Write a number: '))
y = int(input('Write the second number: '))
z = int(input('Write the last number: '))
#verifying which one is lower
lower = x
if y < x and y < z:
   lower = y
if z < x and z < y:
   lower = z
#verifying which one is bigger
bigger = x
if y > z and y > x:
   bigger = y
if z > x and z > y:
   bigger = z
print('LOWEST: {}'.format(lower))
print('BIGGEST: {}'.format(bigger))

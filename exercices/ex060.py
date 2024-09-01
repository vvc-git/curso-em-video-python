x = int(input('Digite um valor: '))
n1 = x
f = 1
print(f'{x}! = ', end='')
while x != 0:

   if x != 1:
      print(f'{x} x ', end='')


   else:
      print('1 = ', end='')
      break
   f *= x
   x = x - 1

print(f)
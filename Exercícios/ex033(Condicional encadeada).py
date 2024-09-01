n1 = float(input('\nType the first number: '))
n2 = float(input('Type the second number: '))
n3 = float(input('Type the third number: '))
if n1 > n2:
   if n1 > n3:
      if n2 > n3:
         print('BIGGEST: {}\nLOWEST: {}'.format(n1, n3))
      else:
         print('BIGGEST: {}\nLOWEST: {}'.format(n1, n2))
   else:
      print('BIGGEST: {}\nLOWEST: {}'.format(n3,n2))
else:
   if n1 > n3:
      print('BIGGEST: {}\nLOWEST {}'.format(n2,n3))
   else:
      if n2>n3:
         print('BIGGEST: {}\nLOWEST {}'.format(n2, n1))
      else:
         print('BIGGEST: {}\nLOWES {}'.format(n3, n1))
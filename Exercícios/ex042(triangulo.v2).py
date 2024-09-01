a = float(input('\nType the first length: '))
b = float(input('Type the second length: '))
c = float(input('Type the third length: '))
if a < b + c and b < a + c and c < a + b:
   if a != b and c != a and b != a:  #### a!=b!=c!=a (observe a obrigatoriedade da parcela c!=a)
      print("\nIt's {}Scalene.".format('\033[1;30m'))
   elif a == b and c == a and b == c:      #NAO PRECISA DO c==a!! logica OUUU a==b==c
      print("\nIt's {}Equilateral.".format('\033[1;33m'))
   else:
      print("\nIt's {}Isosceles.".format('\033[1;32m'))
else:
   print("\nYou {}can't{} make a triangle.".format('\033[1;31m', '\033[m'))

n = int(input('Type a number: '))              #todo número é divisivel por 1 e por ele mesmo
s = 0                                          #o primo é SÓ divisível por esses numeros
for g in range (1, n+1):
   if n % g == 0:
      if 1 != g != n:                          # Aqui eu já sabia se 'n' era primo ou nao. POREM, precise encontrar uma maneira de salvar essa informacao de maneira algebrica
         s = s + g
if s != 0:                             #s!=0 é só uma maneira algebrica de reservar a informacao de que "n" nao é primo
   print('It is {}not{} a prime number'.format('\033[2;33m', '\033[m'))
else:
   print('It is a {}prime{} number'.format('\033[3;33m', '\033[m'))
print(8*'-*-')
print('{}NUMBER SYSTEM CONVERTER{}'.format('\033[1;31m', '\033[m'))
print(8*'-*-')

base = str(input('Which number system do you want?\n1. Binary\n2. Octal\n3. Hexadecimal\n{}\n[ANSWER]: '.format(8*'-*-')))
n = int(input("[NUMBER]: "))
print(8*'-*-')
if base == '1':
   print('[BINARY]: {}'.format(bin(n)[2:]))     #fatiamento para tirar a simbologia que vem junto
elif base == '2':                                       #NÃO PODE SER IF
   print('[OCTAL]: {}'.format(oct(n)[2:]))
elif base == '3':                                       #NÃO PODE SER IF
   print('[HEXADECIMAL]: {}'.format(hex(n)[2:]))
else:
   print('Invalid option')
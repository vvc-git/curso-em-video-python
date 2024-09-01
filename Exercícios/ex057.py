sexo = 0
while sexo != 'F' or sexo != 'M': #Não pode: while sexo != 'F' or  'M'
   sexo = input('Escolha seu sexo [M/F]: ').upper().strip()[0]

   if sexo == 'F' or sexo == 'M':
      print('Sex accepted!')
      break
n = ''
more_values = ''
counting = 0
bigger = 0
lower = 99999999999999999999
soma = 0
while more_values != 'N':
   n = int(input('1.Type a value: '))
   more_values = input('2.Do you want to plug more values? ').upper().strip()[0]

   soma += n
   counting += 1

   if counting == 1:
      bigger = n
      lower = n


   else:
      if n > bigger:
         bigger = n

      if n < lower:
         lower = n



print(f'''[BIGGER]: {bigger}
[LOWER]: {lower}
[MÉDIA]: {soma/counting}
''')
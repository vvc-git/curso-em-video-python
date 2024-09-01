num = 0
x = int(input('Type the first value: '))
y = int(input('Type the second value: '))
while not num == 5:
   num = int(input('''What do you want?
[1] PLUS
[2] PRODUCT
[3] BIGGER
[4] NEW VALUES
[5] STOP PROGRAM
-----------------
[ANSWER]: '''))

   if num == 1:
      print(f'Sum: {x+y}')

   elif num == 2:
      print(f'Product: {x*y}')

   elif num == 3:
      if x > y:
         print(f'{x} is bigger than {y}')
      else:
         print(f'{y} is bigger than {x}')

   elif num == 4:
      x = int(input('Type the first value: '))
      y = int(input('Type the second value: '))






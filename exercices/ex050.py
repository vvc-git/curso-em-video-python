sum = 0
contador = 0
for number in range(1, 7):
   number = int(input('{}. Type a number: '.format(number)))
   if (number % 2) == 0:
      sum = sum + number
      contador = contador + 1
if sum == 0:
   print('There are not an even numbers.')
else:
   print(f'You put {contador} even number and the sum of them are {sum}')

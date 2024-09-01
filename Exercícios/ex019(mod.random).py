from random import choice
a1 = str(input('\nName 1: '))
a2 = str(input('Name 2: '))
a3 = str(input('Name 3: '))
a4 = str(input('Name 4: '))
students = [a1, a2, a3, a4] ##lista entre colchetes
print('O escolhido é: {}'.format(choice(students)))

##import random
##a1 = str(input('Pick 4 students: \n[Student1]: '))
##a2 = str(input('[Student2]: '))
##a3 = str(input('[Student2]: '))
##a4 = str(input('[Student3]: '))
##order = [a1, a2, a3, a4] ##lista
##print('The sequence of lecture is: {}'.format(random.sample(order, k=4)))

from random import shuffle
a1 = str(input('First student: '))
a2 = str(input('Second student: '))
a3 = str(input('Third student: '))
a4 = str(input("Fourth student: "))
list = [a1, a2, a3, a4]
s = shuffle(list)
print('The funcking sequence of slides is {}'.format(list)) ## NAO É O S!!



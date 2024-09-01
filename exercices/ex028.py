import random
from time import sleep #para dar ideia de estar carregando o jogando
print(14*'--*--')
think = int(input('I thought a number from 1 to 5. Which number do you think I chose? '))
npc = random.randint(1, 5)
print('Loading...')
sleep(3) #método tempo em segundos
print(14*'--*--')
if npc == think:
   print('Exactly! {} is my number!'.format(npc))
else:
   print('Wrong! I chose {}.'.format(npc))

import random
from time import sleep #para dar ideia de estar carregando o jogando

think = 0
npc = random.randint(1, 5)
contador = 0

while think != npc:
   print(14 * '--*--')
   think = int(input('I thought a number between 1 and 5. Which number do you think I chose? '))
   print('Loading...')
   sleep(1)  # método tempo em segundos
   contador += 1
   if npc > think:
      print('More...')

   elif npc < think:
      print('Less...')


print(f'You win!! You tried {contador}x.')


'''from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior!')
        elif jogador > computador:
            print('Tente um número menor!')
print('Analisando...'), sleep(3)
print('Você acertou com {} tentativas! Parabéns'.format(palpites)) '''
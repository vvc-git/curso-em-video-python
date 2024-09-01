from time import sleep
import random
print(20*'=')
player = str(input('Rock, paper or scissor?\n{}[PLAYER]: {}'.format('\033[0;32m', '\033[m'))).lower().strip()
list = ['rock', 'paper', 'scissor']
machine = random.choice(list)

print(20*'=')
sleep(0.5)
print('JO')
sleep(0.5)
print('QUEM?')
sleep(0.5)
print('PO!!')
print(20*'=')
print('{}[MACHINE]: {}{}'.format('\033[1;31m', machine, '\033[m'))
print(20*'=')
if machine == 'rock' and player == 'paper':
   print('Player {}WON'.format('\033[1;32m'))
elif machine == 'rock' and player == 'scissor':
   print('Machine {}WON'.format('\033[1;31m'))

elif machine == 'paper' and player == 'scissor':
   print('Player {}WON'.format('\033[1;32m'))
elif machine == 'paper' and player == 'rock':
   print('Machine {}WON'.format('\033[1;31m'))

elif machine == 'scissor' and player == 'rock':
   print('Player {}WON'.format('\033[1;32m'))
elif machine == 'scissor' and player == 'paper':
   print('Machine {}WON'.format('\033[1;31m'))
else:
   print("{}It's a tie{}.".format('\033[1;35m','\033[m'))

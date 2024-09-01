print('\033[1;33;41mHello world!\033[m')
name = str(input('Digite seu nome: '))
print('Muito prazer, {}{}{}!'.format('\033[1;34m', name, '\033[m'))
#\033[...m -->> formula
#n1 --> estilo [0,1,4,7]
#n2 --> cor da letra range [30;37]
#n3 --> cor do fundo range [40;47]

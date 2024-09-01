n1 = float(input('Type a number: '))
n2 = float(input('Type another number: '))
s = n1+n2
s2 = n1-n2
p = n1*n2
q = n1/n2
qi = n1//n2
resto = n1%n2
print('\n 1.The sum of {} and {} is: {}.\n 2.The subtraction of {} and {} is: {}.\n 3.The product of {} and {} is: {}.\n 4.The quocient of {} and {} is: {}. \n 5.The interger quocient of {} and {} is: {}.\n 6.The rest of division between {} and {} is {}. '.format(n1, n2, s, n1, n2, s2, n1, n2, p, n1, n2, q, n1, n2, qi, n1, n2, resto))

#another way:
x = float(input('\nType a number: '))
y = float(input('Type another number: '))
s = x+y
s2 = x-y
p = x*y
q = x/y
qi = x//y
rest = x%y
print('\nAll the most common operations between these two number are:\nSum: {} and'.format(s), end='')
print(' Sub: {}'.format(s2))
print('Pro: {} and'.format(p), end='')
print(' Quo: {:.3f}'.format(q))
print('QuoI: {} and '.format(qi), end='')
print('Res: {}.'.format(rest))
print('\n')
print(20*'-')
name = str(input('Type your full name: ')).strip()

clname = len(name)
cspace = name.count(' ')
total = clname - cspace

separa = name.split()
first = separa[0]
lengthf = len(first)

print(20*'-')
print('1.', name.upper())
print('2.', name.lower())
print('3. The total of letters without spaces is {}.'.format(total))
print('4. The first name has {} letter(s).'.format(lengthf))
#### outra forma de fazer 4. é procurar pelo primeiro espaço(tem que usar o strip no começo)
### a contagem começa do zero


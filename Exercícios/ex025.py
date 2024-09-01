print(20*'=')
name = str(input('Type your full name: ')).strip()
capital = name.upper()
separa = capital.split()
find = 'SILVA' in separa
print("It's true that this name has 'SILVA'? It's {}.".format(find))

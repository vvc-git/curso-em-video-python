print(20*'-')
n = str(input("City's name: ")).strip()
u = n.upper() #transforma tudo em maiuscula
d = u.split() #divide cada palavra em uma lista             outra forma é: print(n[:5].lower() == 'santo')
p = d[0]     #pega a primeira palavra da lista
f = 'SANTO' in p #checa se tem santo nessa palavra
print("\nIt's true that there's a Santo in the city's name? It's {}.".format(f))

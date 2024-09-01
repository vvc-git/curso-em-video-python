acumulador = 0
contador = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        acumulador = acumulador + c
        contador = contador + 1

print(f'A soma de todos os ímpares entre 1 a 500 é {acumulador} e o número de termos somados é  {contador}')

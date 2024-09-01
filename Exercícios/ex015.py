d = float(input('\n Q1: Quantos quilômetros foram percorridos? '))
p = float(input(' Q2: Quantos dias o carro ficou alugado? '))
r = 60*p + d*0.15
print("\n R: O preço do aluguel é: R${:.2f}".format(r))

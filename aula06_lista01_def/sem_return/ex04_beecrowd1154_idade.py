"""Faça um algoritmo para ler um número indeterminado
de dados, contendo cada um, a idade de um indivíduo.O último dado, que não
entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a
idade média deste grupo de indivíduos."""

def media(g, y):
    mediaidade = g/y
    print("Média das idades:", mediaidade)

p = 1
x = 0
h = 0
while x >= 0:
    x = int(input("Digite a idade: "))
    if x <= 0:
        p -= 1
    else:
        h += x
        p += 1   
media(h, p)
    
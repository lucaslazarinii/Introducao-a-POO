"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja
ver a tabuada."""

x = int(input("Digite a tabuada desejada: "))

for i in range (0, 11):
    print(x, "X", i, "=", (x*i))
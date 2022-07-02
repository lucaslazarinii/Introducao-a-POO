"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
de números pares e a quantidade de números impares."""

i = 0
p = 0
for x in range (0,10):
    if (int(input("Digite um número: ")) %2 != 0):
        i += 1
    else:
        p += 1        
print("Números ímpares:", i)
print("Números pares:", p)
"""Escreva um programa que leia o sexo das pessoas, mas somente aceite “M” ou “F”.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

r = 0 

while r != 'M' and r != 'F':
    r = input("Digite o sexo [M/F]: ")
else:
    if r == 'M':
        print("Sexo escolhido: Masculino")
    else:
        print("Sexo escolhido: Feminino")
    
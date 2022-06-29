"""Escreva um programa que leia o número de um funcionário,
seu número de horas trabalhadas, o valor que recebe por hora e
calcula o salário desse funcionário. A seguir, mostre o número e o
salário do funcionário, com duas casas decimais."""

nmr = input("Insira o número do funcionário: ")
ht = input("Insira quantidade de horas trabalhadas: ")
rph = input("Insira seu pagamento por hora: ")

ht = float(ht)
rph = float(rph)

S = (ht*rph)

print("NUMBER =", nmr)
print("SALARY = U$", S)
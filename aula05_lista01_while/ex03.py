"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos e qual foi o maior e o
menor valor lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores."""

x = 0
r = "S"
maxi = 0
mini = 0
med = 0
q = 0
s = 0

while r == 'S':
    x = (int(input("Digite um valor: ")))
    r = input("Deseja continuar? [S/N] ").upper()
    s += x
    q += 1
    m = s/q
    if x < mini or mini == 0:
        mini = x
    if (x > maxi):
        maxi = x
    

print("Maior valor lido:", maxi)
print("Menor valor lido:", mini)
print("Média dos valores:", m)
"""Faça um programa que leia dois inteiros: X e Z (devem ser lidos tantos
valores para Z quantos necessários, até que seja digitado um valor maior do
que X para ele). Conte quantos números inteiros devem ser somados em sequência
(considerando o X nesta soma) para que a soma ultrapasse a Z o mínimo possível.
Escreva o valor final da contagem.

A entrada pode conter, por exemplo, os valores 21 21 15 30. Neste caso,
é então assumido o valor 21 para X enquanto os valores 21 e 15 devem ser
desconsiderados pois são menores ou iguais a X. Como o valor 30 está dentro
da especificação (maior do que X) ele será válido e então deve-se processar
os cálculos para apresentar na saída o valor 2, pois é a quantidade de valores
somados para se produzir um valor maior do que 30 (21 + 22)."""

x = int(input("Digite o valor de X: "))
z = int(input("Digite o valor de Z: "))
while (z <= x):
    z = int(input("Digite o valor de Z novamente: "))
def vereficar(a, b):
    soma = 0
    r = 1
    for i in range(a, b):
        soma += i
        if (soma < b):
            r += 1
    print(r)
vereficar(x, z)
            
    
    
    
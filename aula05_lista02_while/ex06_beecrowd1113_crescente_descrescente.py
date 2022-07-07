"""Leia uma quantidade indeterminada de duplas de valores inteiros X e Y.
Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em
ordem crescente ou decrescente."""

x = 0
y = 1


while x != y:
    x, y = (input("Digite dois números: ")).split()
    x = int(x)
    y = int(y)
    if x > y:
        print("Decrescente")
    elif y > x:
        print("Crescente")
    



print("")

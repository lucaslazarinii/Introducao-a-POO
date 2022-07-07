"""Este programa deve ler uma variável inteira X inúmeras vezes
(deve parar quando o valor no arquivo de entrada for igual a zero).
Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e
seu sucessor."""

x = int(input("Digite um número inteiro: "))
while x != 0:
    r = 1
    while (r < x +1):
        if (r == x):
            print(x)
            r += 1
        else:
            print(r, end=" ")
            r += 1
    print()
    x = int(input())
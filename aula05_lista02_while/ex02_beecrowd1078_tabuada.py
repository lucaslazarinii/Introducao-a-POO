"""Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
1 x N = N      2 x N = 2N        ...       10 x N = 10N"""

N = int(input("Digite um número inteiro: "))
while N < 2 or N > 1000:
    print("-----------ERRO------------")
    print("O número deve estar no inveralo (2 < N < 1000)")
    N = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    r = N*i
    print(i, "x", N, "=", r)
    
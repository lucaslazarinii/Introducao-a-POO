"""Leia um conjunto não determinado de pares de valores M e N
(parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a
sequência do menor até o maior e a soma dos inteiros consecutivos entre eles
(incluindo o N e M)."""

M, N = (int(x) for x in input("Digite dois valores: ").split())

while (M != 0 and N != 0):
    s = 0
    if (M < N):
        for i in range (M, N+1):
            s = s + i
            print(i, end=" ")
    else:
        for i in range (N, M+1):
            print(i, end=" ")
            s = s + i
    print("Sum=", s)
    M, N = (int(x) for x in input("Digite dois valores: ").split())
        

n = int(input("Digite a quantidade de testes a serem realizados: "))
while n < 1 or n > 20:
    print("\nA quantidade de testes a serem realizados deve estar entre 1 e 20.")
for i in range(n):
    s = 0
    x = int(input("Digite um número: "))
    while x < 1 or x > 10**8:
        print("\n O número fornecido ao teste deve estar entre 1 e 10^8.")
        x = int(input("Digite um número: "))
    for j in range(1, x):
        if x%j == 0:
            s += j
    if s == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
        

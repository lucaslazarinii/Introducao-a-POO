def leds(sequencia):
    leds = 0
    for i in range(0, len(sequencia)):
        if sequencia[i] == "1":
            leds += 2
        elif sequencia[i] == "2":
            leds += 5
        elif sequencia[i] == "3":
            leds += 5
        elif sequencia[i] == "4":
            leds += 4
        elif sequencia[i] == "5":
            leds += 5
        elif sequencia[i] == "6":
            leds += 6
        elif sequencia[i] == "7":
            leds += 3
        elif sequencia[i] == "8":
            leds += 7
        elif sequencia[i] == "9":
            leds += 6
        elif sequencia[i] == "0":
            leds += 6
    return leds
    
N = int(input("Digite a quantidade de testes: "))
while N < 0 or N > 1000:
    print()
    print("Dados incorretos. A quantidade de testes deve ser um valor entre 1 e 1000.")
    N = int(input("Digite a quantidade de testes novamente: "))
X = int(input("Digite um número: "))
while X < 0 or X > 10**100:
    print()
    print("Dados incorretos. O número deve ser um valor entre 1 e 10^100.")
    X = int(input("Digite o número novamente: "))
X = str(X)
resultado = leds(X)
print(resultado, "leds")
N = int(input("Digite a quantidade de testes: "))
for i in range(0, N):
    x = input("Digite o código: ")
    h = x[2]
    z = x[0]
    if h == z:
        y = int(h)*int(z)
        print(y)
    elif x[1].isupper():
        y = int(h) -int(z)
        print(y)
    elif x[1].islower():
        y = int(h) + int(z)
        print(y)
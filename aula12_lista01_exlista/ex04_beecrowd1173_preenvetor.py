x = []
x.append(int(input("Digite um número: ")))
while x[0] > 50:
    list.clear(x)
    print("\n\nO número inserido deve ser menor ou igual a 50.")
    x.append(int(input("Digite um número novamente: ")))
for i in range(0, 11):
    if i == 0:
        x[0] = x[0]
        print(f"N[{i}] =", x[0])
    else:
        x[0] = x[0]*2
        print(f"N[{i}] =", x[0])


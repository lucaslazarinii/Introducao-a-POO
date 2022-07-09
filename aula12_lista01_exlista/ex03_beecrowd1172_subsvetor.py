x = []
for i in range(0, 11):
    x.append(int(input("Digite um número: ")))
    if x[0] <= 0:
        x[0] = 1
        print(f"X[{i}] =", x[0])
    else:
        print(f"X[{i}] =", x[0])
    list.clear(x)

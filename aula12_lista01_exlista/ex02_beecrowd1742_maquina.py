s = True
p = list(int(x) for x in input("Digite as entradas do conector par: ").split())
while len(p) != 5:
    p.clear()
    print("\n\nA quantidade de entradas deve ser igual a 5.")
    p = list(int(x) for x in input("Digite as entradas do conector par novamente: ").split())
while s == True:
    for i in range(0, 5):
        if p[i] == 1 or p[i] == 0:
            s = True
            if i == 4:
                s = False
                break
        else:
            p.clear()
            print("\n\nSomente são aceitos os números 0 e 1.")
            p = list(int(x) for x in input("Digite as entradas do conector par novamente: ").split())

i = list(int(x) for x in input("Digite as entradas do conector impar: ").split())
while len(i) != 5:
    i.clear()
    print("\n\nA quantidade de entradas deve ser igual a 5.")
    i = list(int(x) for x in input("Digite as entradas do conector ímpar novamente: ").split())
while s == True:
    for i in range(0, 5):
        if p[i] == 1 or p[i] == 0:
            s = True
            if i == 4:
                s = False
                break
        else:
            p.clear()
            print("\n\nSomente são aceitos os números 0 e 1.")
            p = list(int(x) for x in input("Digite as entradas do conector ímpar novamente: ").split())

k = 0
for g in range(0, 5):
    if p[g] != i[g]:
        k += 1
    else:
        k += 0

if k != 5:
    print("N")
else:
    print("Y")
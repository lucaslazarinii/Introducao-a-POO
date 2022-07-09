while True:
    N = int(input("Digite a quantidade de comandos: "))
    a = 0
    while (N < 0 or N > 1000):
        N = int(input("Erro. Digite a quantidade de comandos novamente: "))
    if (N == 0):
        print("Fim.")
        break
    direcao = input("Digite os comandos [D/E]: ")
    if (len(direcao) != N):
        print("Número de comandos e quantidade inseridas não se relacionam.")
        direcao = input("Digite os comandos dados novamente [D/E]: ")

    for i in direcao:
        if (i.upper() == "E"):
            a -= 1
        else:
            a += 1

        if (a == 4 or a == -4):
            a = 0
    if (a == 0):
        print("N")
    elif a == 2 or a == -2:
        print("S")
    elif a > 0:
        print("L")
    else:
        print("O")
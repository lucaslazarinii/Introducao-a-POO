while True:
    soma = 0
    a, nmr = input("Digite a quantidade de algarismos e o respectivo número: ").split()
    a, nmr = int(a), int(nmr)
    while (a<1 or a>10 or nmr<1 or nmr>1000000000 or len(str(nmr)) != a):
        print("\n\nA quantidade de algarismos fornecidos não condiz com o número digitado, tente novamente.")
        a, nmr = input("Digite a quantidade de algarismos e o respectivo número novamente: ").split()
        a, nmr = int(a), int(nmr)
    nmr = str(nmr)
    for i in range(0, len(nmr)):
        soma += int(nmr[i])
    if soma%3 == 0:
        print(soma, "sim")
    else:
        print(soma, "não")
    r = str(input("Deseja continuar? (S/N) ")).upper()
    if r == "S":
        print()
    else:
        break




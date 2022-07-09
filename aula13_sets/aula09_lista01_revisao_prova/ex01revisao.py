r = "S"

while r == "S":
    a, p, c, m, l = (int(x) for x in input("Digite a quantidade de porções: ").split())
    resultado = (a*300 + p*1500 + c*600 + m*1000 + l*150)+225
    print("Gramas necessárias:", resultado)
    r = str(input("Deseja continuar executando? [S/N]").upper())
    
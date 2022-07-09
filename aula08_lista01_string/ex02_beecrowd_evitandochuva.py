N = int(input("Digite a quantidade de dias previstos pelo sistema meteorológico: "))
ultima_previsao = ""
casa = 0
escritorio = 0
for i in range(0, N):
    SD, SN = (str(x) for x in input("Digite a previsão: ").split())
    if escritorio == 0 and ultima_previsao == "chuva":
        escritorio += 1
    ultima_previsao = SN
    if ultima_previsao == "chuva" and SD == "sol":
        escritorio += 1
print(casa, escritorio)
matriz = []
tamanho = 3
L = int(input("Digite a linha desejada: "))
L -= 1
while True:
    O = input("Operação a ser realizada? (S/M) ").upper()
    if O == "S":
        break
    elif O == "M":
        break
    else:
        print()
        True
for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        linha.append(float(input("Digite um número: ")))
    matriz.append(linha)                    
if O == "S":
    soma = 0
    for i in range(tamanho):
        soma += matriz[L][i]
    print(round(soma))
else:
    soma = 0
    for i in range(tamanho):
        soma += matriz[L][i]
    print(round(soma/tamanho))
    

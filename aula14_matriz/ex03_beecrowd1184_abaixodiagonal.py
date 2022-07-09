matriz = []
tamanho = 12
x = 1
y = 2
soma = 0
media = 0
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
        linha.append(input("Digite um número: "))
    matriz.append(linha)
if O == "S":
    for linha in range(1, tamanho):
        for coluna in range(x):
            soma += int(matriz[linha][coluna])
        x += 1
    print(soma)
elif O == "M":
    for linha in range(1, tamanho):
        for coluna in range(x):
            soma += int(matriz[linha][coluna])
            media += 1
        x += 1
    print(soma/media)
           
    
    
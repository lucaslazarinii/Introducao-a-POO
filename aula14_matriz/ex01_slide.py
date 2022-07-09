atual = []
dados = []
pesadas = []
leves = []
acima20 = []
maior = 0
menor = 10**99
while True:
    atual.append(input("Digite o nome da pessoa: "))
    atual.append(int(input("Digite a idade da pessoa: ")))
    atual.append(int(input("Digite o peso da pessoa: ")))
    dados.append(atual[:])
    list.clear(atual)
    
    r = input("Deseja continuar cadastrando? [S/N]").upper()
    if r == "N":
        break
    elif r == "S":
        True
    else:
        r = input("Deseja continuar cadastrando? [S/N]").upper()
for i in range(0, len(dados)):
    if dados[i][2] >= maior:
        maior = dados[i][2]
        list.clear(pesadas)
        pesadas.append(dados[i][0])
    if dados[i][2] <= menor:
        menor = dados[i][2]
        list.clear(leves)
        leves.append(dados[i][0])
    if dados[i][1] > 20:
        acima20.append(dados[i])
print("\nQuantidade de pessoas cadastradas: ", len(dados))
print("Pessoa mais pesada: ", pesadas)
print("Pessoa mais leve: ", leves)
print("Pessoas com mais de 20 anos: ", acima20)


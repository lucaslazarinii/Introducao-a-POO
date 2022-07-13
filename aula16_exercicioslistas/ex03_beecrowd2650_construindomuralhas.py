Q, A = (int(x) for x in input("Digite a quantidade de titãs e a altura da muralha: ").split())
nomes = []
alturas = []
for i in range(Q):
    nome, altura = list(input("Digite o nome e altura do Titan: ").split())
    nomes.append(nome)
    alturas.append(altura)
for i in range(Q):
    if int(alturas[i]) > A:
        print(f"Titan {nomes[i]}")
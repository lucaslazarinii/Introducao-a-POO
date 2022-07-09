t = []
P, S = (int(x) for x in input("Digite a quantidade de pedras e de sapos: ").split())
while P < 1 or S < 1 or P > 100 or S > 100:
    print("\nA quantidade de pedras e sapos deve estar entre 1 e 100. Tente novamente.")
    P, S = (int(x) for x in input("Digite a quantidade de pedras e de sapos: ").split())
for i in range(1, P+1):
    t.append(0)
for i in range(1, S+1):
    l, d = (int(x) for x in input(f"Digite a localização do sapo {i} e sua distância de pulo: ").split())
    g = l -1
    t[g] = 1
    esquerda = g - d 
    direita = g + d 
    while esquerda >= 0:
        t[esquerda] = 1
        esquerda -= d
    while direita < P:
        t[direita] = 1
        direita += d
        

print("\n===== RESULTADO =====")
for i in range(0, P):
    print(t[i])
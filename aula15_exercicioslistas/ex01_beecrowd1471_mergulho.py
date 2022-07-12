while True:
    N, R = (int(x) for x in input("Digite quantos mergulharam e quantos retornaram: ").split())
    total = []
    for i in range(1, N+1):
        total.append(i)
    remover = []
    remover = list(int(x) for x in input("Digite quem retornou: ").split())
    for i in range(0 ,len(remover)):
        total.remove(remover[i])
    if len(total) == 0:
        print("*")
    else:
        print(*total, sep=" ")
    r = input("Deseja continuar? (S/N)").upper()
    if r == "S":
        True
    else:
        break
    

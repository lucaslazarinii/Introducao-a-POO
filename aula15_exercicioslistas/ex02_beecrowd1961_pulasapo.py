n = 0
P, N = (int(x) for x in input("Digite a altura do pulo do sapo e o número de canos: ").split())
while P < 0 or P > 5:
    print("\nO pulo do sapo deve estar entre 1 e 5. Tente novamente.")
    P = int(input("Digite o pulo do sapo: "))
while N < 2 or N > 100:
    print("\nA quantidade de canos deve estar entre 2 e 100. Tente novamente. ")
    N = int(input("Digite a quantidade de canos: "))
canos = list(int(x) for x in input("Digite a altura dos canos da esquerda para direita: ").split())
while len(canos) != N:
    canos = []
    print("\nA quantidade de canos desejados não corresponde com os dados inseridos. Tente novamente.")
    canos.append(int(x) for x in input("Digite a altura dos canos da esquerda para direita: ").split())
for i in range(0, len(canos)):
    if canos[i] < 0 or canos[i] > 10:
        print("\nA altura dos canos deve estar entre 1 e 10.")
        canos[i] = (int(input(f"{canos[i]} não pode ser lido. Digite um substituto: ")))
    if i != len(canos)-1:
        if canos[i+1] - canos[i] >= P:
            n += 1
if n > 0:
    print("GAME OVER")
else:
    print("YOU WIN")
            
        
    
t = [1]
r = []
Q = int(input("Digite a quantidade de células no tabuleiro: "))
while Q < 0 or Q > 50:
    print("\n\nA quantidade de células no tabuleiro deve estar entre 1 e 50.")
    Q = int(input("Digite a quantidade de células no tabuleiro novamente: "))
print("\n\nResponda utilizando os seguintes parâmetros:\n0 = Não há bombas nessa célula.\n 1= Há bombas nessa célula.\n")
for i in range(1, Q+1):
    t.append(int(input((f"Digite o status da célula {i}: "))))






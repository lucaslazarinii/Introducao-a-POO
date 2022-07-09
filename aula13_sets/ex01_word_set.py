def checagem(lista, p1, p2):
    if p1.intersection(p2):
        lista.append(p1.intersection(p2))
        return lista
l =[]
F = set(input("Alunos matriculados no futebol: ").split())
N = set(input("Alunos matriculados na natação: ").split())
V = set(input("Alunos matriculados no vôlei: ").split())
B = set(input("Alunos matriculados no basquete: ").split())

print()
print(f"Alunos que fazem futebol: {F}")
print(f"Alunos que fazem natação: {N}")
print(f"Alunos que fazem vôlei: {V}")
print(f"Alunos que fazem basquete: {B}")
print()

while True:
    r = input("Deseja matricular novos alunos? [S/N]").upper()
    if r == "S":
        print("\nO cadastro de novos alunos deve ser feito de forma individual.\n")
        print("ESPORTES DISPONÍVEIS:\n1 - Futebol\n2 - Natação \n3 - Vôlei \n4 - Basquete")
        c = int(input("Digite o código do esporte desejado para cadastro: "))
        while c > 5 or c < 0:
            print("\nSó estão disponíveis 4 esportes para escolha, tente novamente.")
            c = int(input("Digite o código do esporte desejado para cadastro novamente: "))
        if c == 1:
            F.add(input("Digite o nome a ser cadastrado no futebol:"))
        elif c == 2:
            F.add(input("Digite o nome a ser cadastrado na natação:"))
        elif c == 3:
            F.add(input("Digite o nome a ser cadastrado no vôlei:"))
        elif c == 4:
            F.add(input("Digite o nome a ser cadastrado no basquete:"))
    elif r == "N":
        break
    else:
        print("\nDigite 'S' ou 'N'.")
        True

checagem(l, F, N)
checagem(l, F, V)
checagem(l, F, B)
checagem(l, N, B)
checagem(l, N, V)
checagem(l, V, B)
print("Alunos que possuem desconto:", l)

print()
print(f"Alunos que fazem futebol: {len(F)}")
print(f"Alunos que fazem natação: {len(N)}")
print(f"Alunos que fazem vôlei: {len(V)}")
print(f"Alunos que fazem basquete: {len(B)}")
print(f"Número total de alunos do Centro de Treinamento: {len(B.union(F).union(N).union(V))}")


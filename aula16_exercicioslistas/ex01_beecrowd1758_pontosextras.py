T = int(input("Quantidade de casos teste: "))
while T < 0 or T > 5000:
    print("\nA quantidade de casos teste deve estar entre 1 e 5000. Tente novamente.")
    T = int(input("Quantidade de casos teste: "))
for i in range(T):
    colunas = []
    P, N = (int(x) for x in input("Digite a quantidade de provas realizadas e alunos matriculados: ").split())
    while P < 2 or P > 5:
        print("\nA quantidade de provas deve estar entre 2 e 5. Tente novamente.")
        P = int(input("Digite a quantidade de provas realizadas: "))
    while N < 2 or N > 50:
        print("\nA quantidade de alunos matriculados deve estar entre 2 e 50. Tente novamente.")
        N = int(input("Digite a quantidade de alunos matriculados: "))
    for i in range(N):
        soma = 0
        linhas = list(float(x) for x in input(f"Digite as notas do aluno {i+1}: ").split())
        for g in range(len(linhas)):
            if linhas[g] < 0 or linhas[g] > 10:
                print(f"\n{linhas[g]}, não pode ser lido. As notas devem ser de 0 a 10. Tente novamente. ")
                linhas[g] = (int(input("Digite a nota substituta: ")))            
        while len(linhas) != P:
            linhas = []
            print("\nA quantidade de alunos matriculados não corresponde com os dados inseridos. Tente novamente.")
            linhas.append(float(x) for x in (input(f"Digite as notas do aluno {i+1}: ").split()))
        colunas.append(linhas)
        for j in range(len(linhas)):
            soma += linhas[j]
        media = soma/len(linhas)
        print("Média: {:.2f}".format(media))

    
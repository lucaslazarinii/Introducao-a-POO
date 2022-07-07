"""Este ano tem Copa do Mundo! O país inteiro se prepara para torcer para a equipe
canarinho conquistar mais um título, tornando-se hexacampeã.

Na Copa do Mundo, depois de uma fase de grupos, dezesseis equipes disputam a
Fase final, composta de quinze jogos eliminatórios. A
figura abaixo mostra atabela de jogos da Fase final:

Na tabela de jogos, as dezesseis equipes finalistas são representadas por
letras maiúsculas (de A a P), e os jogos são numerados de 1 a 15. Por exemplo,
o jogo 3 é entre as equipes identificadas por E e F; o vencedor desse jogo
enfrentará o vencedor do jogo 4, e o perdedor será eliminado. A equipe que
vencer os quatro jogos da Fase final será a campeã (por exemplo, para a equipe
K ser campeã ela deve vencer os jogos 6, 11, 14 e 15.

Dados os resultados dos quinze jogos da Fase final, escreva um programa
que determine a equipe campeã."""

for i in range (1, 16):
    M, N = (int(x) for x in input("Digite o resultado do jogo {}: ".format(i)).split())
    while M < 0 or N < 0 or M == N or M > 20 or N > 20:
        print()
        print("Dados incorretos.")
        print("Os resultados devem estar entre 1 e 20 e não podem ser iguais.")
        M, N = (int(x) for x in input("Digite o resultado do jogo {}: ".format(i)).split())
    if (i == 1):
        v1 = ""
        if (M>N):
            v1 = "A"
        else:
            v1 = "B"
    if (i == 2):
        v2 = ""
        if (M>N):
            v2 = "C"
        else:
            v2 = "D"
    if (i == 3):
        v3 = ""
        if (M>N):
            v3 = "E"
        else:
            v3 = "F"
    if (i == 4):
        v4 = ""
        if (M>N):
            v4 = "G"
        else:
            v4 = "H"
    if (i == 5):
        v5 = ""
        if (M>N):
            v5 = "I"
        else:
            v5 = "J"
    if (i == 6):
        v6 = ""
        if (M>N):
            v6 = "K"
        else:
            v6 = "L"
    if (i == 7):
        v7 = ""
        if (M>N):
            v7 = "M"
        else:
            v7 = "N"
    if (i == 8):
        v8 = ""
        if (M>N):
            v8 = "O"
        else:
            v8 = "P"
    if (i == 9):
        v9 = ""
        if (M>N):
            v9 = v1
        else:
            v9 = v2
    if (i == 10):
        v10 = ""
        if (M>N):
            v10 = v3
        else:
            v10 = v4
    if (i == 11):
        v11 = ""
        if (M>N):
            v11 = v5
        else:
            v11 = v6
    if (i == 12):
        v12 = ""
        if (M>N):
            v12 = v7
        else:
            v12 = v8
    if (i == 13):
        v13 = ""
        if (M>N):
            v13 = v9
        else:
            v13 = v10
    if (i == 14):
        v14 = ""
        if (M>N):
            v14 = v11
        else:
            v14 = v12
    if (i == 15):
        v15 = ""
        if (M>N):
            v15 = v13
        else:
            v15 = v14
print("A equipe vencedora é: {}".format(v15))


    
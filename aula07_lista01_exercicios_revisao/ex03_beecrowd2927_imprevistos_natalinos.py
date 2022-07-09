print("Digite o número de alunos, computadores, computadores queimados e computadores sem compilador.")
alunos, computadores, queimados, compilador = (int(x) for x in input("Digite os números: ").split())

disponiveis = (computadores - queimados - compilador) -1

while (compilador > computadores) or (queimados > computadores) or (alunos > computadores) or (computadores > 1000):
    print("")
    print("Dados incorretos, alguma regra não foi seguida:")
    print("1. Mais de 1000 computadores existentes. \n2. Mais alunos do que computadores existentes. \n3. Quantidade de computadores queimados superior a quantidade de computadores existentes.")
    print("4. Quantidade de computadores sem compilador superior a quantidade de computadores existentes")
    alunos, computadores, queimados, compilador = (int(x) for x in input("Digite os números novamente: ").split())

if (alunos>disponiveis):
    if (queimados > compilador/2):
        print("Caio, a culpa eh sua!")
    else:
        print("Igor bolado!")
else:
    print("Igor feliz!")


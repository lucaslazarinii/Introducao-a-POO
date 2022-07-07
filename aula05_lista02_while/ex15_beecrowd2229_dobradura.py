"""Zezinho tem aulas de Iniciação Artística em sua escola, e recentemente
aprendeu a fazer dobraduras em papel. Ele ficou fascinado com as inúmeras
possibilidades de se dobrar uma simples folha de papel.
Como Zezinho gosta muito de matemática, resolveu inventar um quebra-cabeça
envolvendo dobraduras. Zezinho definiu uma operação de dobradura D que consiste
em dobrar duas vezes uma folha de papel quadrada de forma a conseguir um quadrado
com 1/4 do tamanho original, conforme ilustrado na figura."""

"""Depois de repetir N vezes esta operação de dobradura D sobre o papel, Zezinho
cortou o quadrado resultante com um corte vertical e um corte horizontal,
conforme a figura abaixo."""

"""Zezinho lançou então um desafio aos seus colegas:
quem adivinha quantos pedaços de papel foram produzidos?"""

t = 1
d = int(input("Digite a quantidade de dobraduras: "))
p = (d**d)

while d >= 0:
    if (d == 0):
        print("Teste", t)
        print("4")
        t += 1
        print("")
        d = int(input("Digite a quantidade de dobraduras: "))
    if (d == 1):
        print("Teste", t)
        print("9")
        t += 1
        print("")
        d = int(input("Digite a quantidade de dobraduras: "))
    else:
        print("Teste", t)
        t += 1
        r = ((2**d)+1)**2
        print(r)
        print("")
        d = int(input("Digite a quantidade de dobraduras: "))
        
        
    
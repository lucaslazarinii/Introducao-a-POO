"""Leia 6 valores. Em seguida, mostre quantos destes valores digitados
foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores
positivos digitados, com um dígito após o ponto decimal."""

def media(x):
    mediavalores = x/p
    print (mediavalores)

r = 0
p = 0
s = 0
n = 0
while (r < 6):
    g = float(input("Digite um valor: "))
    r += 1
    if g > 0:
        p += 1
        s += g
    else:
        n += 1
print("Quantidade de valores positivos: ", p)
media(s)
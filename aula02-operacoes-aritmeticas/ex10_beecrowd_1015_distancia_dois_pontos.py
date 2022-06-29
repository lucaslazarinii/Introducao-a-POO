"""Leia os quatro valores correspondentes aos eixos x e y de dois pontos
quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles,
mostrando 4 casas decimais após a vírgula, segundo a fórmula:"""

x1, y1 = input("Digite dois valores: ").split()
x2, y2 = input("Digite outros dois valores: ").split()

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

import math

d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print("{:.4f}".format(d))
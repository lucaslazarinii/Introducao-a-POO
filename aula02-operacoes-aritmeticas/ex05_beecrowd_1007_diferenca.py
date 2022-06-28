"""Leia quatro valores inteiros A, B, C e D. A seguir, calcule
e mostre a diferença do produto de A e B pelo produto de C e D
segundo a fórmula: DIFERENCA = (A * B - C * D)."""

a, b, c, d = input("Digite quatro valores inteiros:").split()

a = int(a)
b = int (b)
c = int (c)
d = int (d)

DIFERENCA = ((a*b)-(c*d))

print("DIFERENCA =  {}".format(DIFERENCA))
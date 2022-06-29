"""Leia um valor inteiro, que é o tempo de duração em segundos de um
determinado evento em uma fábrica, e informe-o expresso no formato
horas:minutos:segundos."""

s = float(input("Digite o tempo em segundos: "))

m = (s/60)
h = (m/60)
x = (m%60)
r = (s%60)

print("{horas:.0f}:{restom:.0f}:{resto:.0f}".format(horas=h, restom=x, resto=r))


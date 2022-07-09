"""Leia a hora inicial e a hora final de um jogo.
A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em
um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de
24 horas."""

x, y = (int(x) for x in input("Digite a hora inicial e a hora final do jogo: ").split())

if (y>x):
    t = y-x
elif (y == 0) and (x == 0):
    t = 24
else:
    t = (24-x) + y

print("O JOGO DUROU {} HORA(S)".format(t))
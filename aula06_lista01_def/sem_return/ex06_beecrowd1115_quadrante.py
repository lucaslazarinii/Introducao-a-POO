"""Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada
de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele p
ertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for
NULA (nesta situação sem escrever mensagem alguma).
"""
x = 1
y = 1
while x !=0 and y != 0:
    x, y = (int(x) for x in input("Digite as coordenadas: ").split())

    def quadrante(a, b):
        if a == 0 or b == 0:
            print()
        elif a > 0:
            if b > 0:
                print("primeiro")
            else:
                print("quarto")
        elif b > 0:
            print("segundo")
        elif b < 0:
                print("terceiro")
            
    quadrante(x, y)
print()
    
    

